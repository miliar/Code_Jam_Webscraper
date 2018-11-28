#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <math.h>
#include <string>

using namespace std;

int main(){
	long int t, tt, n, dif, grad, method2;
	int m[1001];
	string r;
	cin>>t;
	tt=0;
	while(tt++ < t){
		cin>>n;
		dif = 0;
		grad = 0;
		method2 = 0;
		cin>>m[0];
		for(int i = 1; i<n; i++){
			cin>>m[i];
			if((m[i-1]-m[i]) > grad){
				grad = (m[i-1] - m[i]);
			}
		}
		for(int i = 1; i<n; i++){
			if(m[i-1] > m[i]){
				dif += m[i-1] - m[i];
			}
		}
		for(int i = 0; i<n-1; i++){
			if(m[i] > grad){
				method2 += grad;
			} else{
				method2 += m[i];
			}
		}
		// for(int i = 0; i<n; i++){
		// 	cout<<m[i]<<endl;
		// }
		
		cout<<"Case #"<<tt<<": "<<dif<<" "<<method2<<endl;
	}
	return 0;
}