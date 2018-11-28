#include <stdio.h>
#include <iostream>

using namespace std;

int main(){
	
	int TC=0,tc;
	int N,x,sum,add;
	cin >>tc;
	char ch;
	while (tc--){
		cin >> N;
		sum=0,add=0;

		for (int i=0;i<N+1;i++){
			cin >> ch;	
			x = ch-'0';
			if (i==0){
				sum=x;
				continue;
			}
			if (x){
				if (i>sum){
					add+=i-sum;
					sum+=i-sum;
				}
				sum+=x;
			}
		}

		cout << "Case #" << ++TC << ": " << add << endl;
	}

}
