#include<iostream>
using namespace std;

void quick(double input[], int i, int j){
    double temp;
    int N = j, low = i, high = j - 1;
    if(i < j){
	while(high >= low){
	    while(input[N] > input[low]){
                low++;
            }
            while(input[N] < input[high]){
                high--;
            }
	    if(low < high){
                temp = input[low];
                input[low] = input[high];
                input[high] = temp;
	    }
        }
        temp = input[low];
        input[low] = input[N];
        input[N] = temp;
        quick(input, i, low - 1);
        quick(input, low + 1, j);
    }
}

 
int main(){
    int T, N, i, j, count1, count2, k;
    
    cin >> T;
    for(i = 1; i <= T; i++){
        cin >> N;
        double input1[N], input2[N];
        for(j = 0; j < N; j++){
            cin >> input1[j];
        }
        for(j = 0; j < N; j++){
            cin >> input2[j];
        }
        quick(input1, 0, N - 1);
        quick(input2, 0, N - 1);
        count1 = 0;
	count2 = N;
	k = 0;
	for(j = 0; j < N; j++){
	    if(k >= N){
		break;
	    }
	    while(input1[j] > input2[k] && k < N){
		k++;
		count1++;
	    }
	    if(k >= N){
		break;
	    }
	    if(input1[j] < input2[k]){
		k++;
	    }
	}
	k = 0;
	for(j = 0; j < N; j++){
	    if(input1[j] < input2[k]){
		count2--;
	    }
	    else{
		k++;
	    }
	    if(k >= count2){
		break;
	    }
	}
	cout << "Case #" << i << ": " << count2 << " " << count1 << endl;
    }
    return 0;
}

		
