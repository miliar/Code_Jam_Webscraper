#include <iostream>
using namespace std;

int solve(int num, int s[]){
	int sum=0, res=0;
	bool flag = false;
	for(int i = 0; i <= num; i++){
		if(s[i]==0){
			flag = true;
		}else{
			if(flag){
				if(sum < i) {
					res+= i-sum;
					sum = i;
				}
			}
			sum+=s[i];
			flag = false;
		}
	}
	return res;
}

int main(){
	int T = 0;
	cin>>T;
	for(int i = 0; i < T; i++){
		int num;
		cin>>num;
		int *s = new int[num+1];
		cin.get();
		for(int j = 0; j <= num; j++)
			s[j]= (cin.get()-'0');
		cout<<"Case #"<<i+1<<": "<<solve(num,s)<<endl;
		delete []s;
	}
	return 0;
}
