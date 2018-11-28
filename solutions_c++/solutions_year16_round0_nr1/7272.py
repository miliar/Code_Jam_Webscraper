#include<bits/stdc++.h>
#define ll long long 

using namespace std;
ll t, Ans[1000009] = {0};


int main(){

	cin>> t;

	for(int j =0; j< t; j++){
	ll n, A[10]= {0},k =0, m =1, now;
	cin>>n;
	now  =n;
	cout<<"case #"<< j+1<<": ";
	if(n== 0){
		cout<<"INSOMNIA"<<endl;
		continue;
	}
	if(Ans[n]){
		cout<<Ans[n] <<endl;
		continue;
	}
	while(k<10){
		m++;
		while(now){
			if(!A[now%10]){k++;
			//cout<<now%10<<" is detected in "<<n*(m-1)<<endl;
			A[now%10]  =1;}
			now/=10;
		}
		now = n*(m);
	}
	cout<< n *(m-1)<<endl;
	Ans[n] = n*(m-1);
	}
	return 0;
}
