#include <iostream>

using namespace std;
int sleep(int N){
	int i, temp, temp2, count = 0; 
	bool flag[10];
	for(i = 0;i<10;i++)
		flag[i] = false;
	i=1;
	while(count < 10){
		temp = N*i; 		
		while(temp > 0){
			temp2 = temp%10; 
			if(flag[temp2] == false){
				flag[temp2] = true;
				count++;
			}
			temp = temp/10;
		}
		i++;
	}
	return N*(i-1);
}

int main(){
	int N, i, num;
	cin >> N;
	
	for(i=0; i<N; i++){
		cin >> num;
		if(num == 0)
			cout << "case #" << i+1 <<": INSOMNIA\n";
		else
			cout <<"case #" << i+1 <<": " << sleep(num) << endl;
	}
	return 0;
}