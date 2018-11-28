#include<iostream>
#include<cstdio>
#include<utility>
#include<bits/stdc++.h>

using namespace std;


int arr[1000010];
int getAns(int x)
{
	int flag[10]={0},cnt=0;
	for(int i=1;;i++){
		int num=i*x;
		while(num!=0){
			if(flag[num%10]==0){
				cnt++;
				flag[num%10]=1;
			}
			num/=10;
		}
		if(cnt==10)
			return i*x;
	}
}
int main()
{
	int T,N=1000000;
	freopen("IN.txt","r",stdin);
	freopen("output.txt","w",stdout);

	for(int i=1;i<=N;i++){
		arr[i]=getAns(i);
		//cout<<arr[i]<<endl;
	}
	cin>>T;
	for(int t=1;t<=T;t++){
		int num;
		cin>>num;
		if(num==0)
			cout<<"Case #"<<t<<": "<<"INSOMNIA"<<endl;
		else
			cout<<"Case #"<<t<<": "<<arr[num]<<endl; 
	}
	return 0;
}