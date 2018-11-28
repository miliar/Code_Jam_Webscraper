#include <iostream>

using namespace std;

int main(){
	int t;
	cin >> t;
	for(int k=1;k<=t;k++){
		int c = 1;
		int s_max;
		cin >> s_max;
		//int input[s_max+1];
		int* input = new int[s_max+1];
		int zeroes = 0;
        int overhead = 0;
        string in;
		cin >> in;
		for(int i=0; i<=s_max; i++){
			int temp =  in[i] - '0';
			//cout << temp;
			input[i] = temp;
			if(temp == 0){
				if(overhead > 0){
					overhead--;
				}
				else{
					zeroes += 1;
				}
			}
		    if(temp >1){
				overhead += (temp-1);
			}
		}

		cout <<"Case #" << k << ": " << zeroes << endl;
		c++;
	}
	return 0;
}
