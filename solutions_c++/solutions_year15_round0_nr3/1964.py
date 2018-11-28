#include <bits/stdc++.h>
using namespace std;
int mult(int a,int b){
	int x=0,c;
	if(a<0)x=(x+1)%2,a*=-1;
	if(b<0)x=(x+1)%2,b*=-1;
	if(a==1||b==1)c=a*b;
	else if(a==b)c=-1;
	else if(a==2){
		if(b==3)c=4;
		else c=-3;
	}
	else if(a==3){
		if(b==2)c=-4;
		else c=2;
	}
	else if(a==4){
		if(b==2)c=3;
		else c=-2;
	}
	if(x%2==1)c*=-1;
	return c;
}
int main(){
	int t,te,i,j,k,n,x,arr[10001];
	cin>>t;
	string s,ss;
	for(te=0;te<t;te++){
		cin>>n>>x;
		cin>>ss;
		for(i=0,s="";i<x;i++)s+=ss;
		n*=x;
		for(i=0;i<n;i++){
			if(s[i]=='i')arr[i]=2;
			if(s[i]=='j')arr[i]=3;
			if(s[i]=='k')arr[i]=4;
		}
		for(i=0,j=1;i<n;i++)j=mult(j,arr[i]);
		if(j!=-1){
			cout<<"Case #"<<(1+te)<<": NO\n";
			continue;
		}
		for(i=0,j=1;i<n;i++){
			j=mult(j,arr[i]);
			if(j==2)break;
		}
		if(i==n){
			cout<<"Case #"<<(1+te)<<": NO\n";
			continue;	
		}
		j=i;
		for(i=n-1,k=1;i>=0;i--){
			k=mult(arr[i],k);
			if(k==4)break;
		}
		if(i<0){
			cout<<"Case #"<<(1+te)<<": NO\n";
			continue;
		}
		k=i;
		cout<<"Case #"<<(1+te)<<": ";
		if(j<k)cout<<"YES\n";
		else cout<<"NO\n";
	}
	return 0;
}