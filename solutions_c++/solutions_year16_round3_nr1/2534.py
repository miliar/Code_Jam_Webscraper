#include<bits/stdc++.h>
using namespace std;
#define ll long long
int sum(int a[],int n){
	int sum=0;
	for(int i=0;i<n;i++)
	sum+=a[i];
	return sum;
}
int max(int a[],int n){
	int max=-1;int pos=0,i;
	for(i=0;i<n;i++){
		if(max<a[i]){
			max=a[i];	
			pos=i;
		}
	}
	return pos;
}
int find(int a[],int n,int m){
	int smax=-1,sp=0;
	for(int i=0;i<n;i++){
		if(i!=m&&a[i]>smax){
			smax=a[i];
			sp=i;
		}
	}
	return sp;
}
int check(int a[],int n){
	int f=0;
	for(int i=0;i<n;i++)
	if(a[i]!=0)
	f++;
	return f;
}
int main(){
	#ifndef ONLINE_JUDGE
    	freopen("inp.txt","r",stdin);
    	freopen("out.txt","w",stdout);
    #endif
	int t,s,ss,n,a[1005],m,sm,f=1;
	cin>>t;
	s=t;
	while(t--){
		cin>>n;
		f=1;
		for(int i=0;i<n;i++)
		cin>>a[i];
		char ch='A';
		cout<<"Case #"<<s-t<<": ";
		while(f){
			m=max(a,n);
			sm=sum(a,n);
			//cout<<m<<" "<<sm<<" ";
			if(sm==2){
				for(int i=0;i<n;i++){
					if(a[i]!=0)
					cout<<(char)(ch+i);
				}
				break;
			}
			if(a[m]>sm/2&&a[m]!=1){
				cout<<(char)(ch+m)<<(char)(ch+m)<<" ";
				a[m]-=2;
			}
			else if(a[m]==sm/2&&a[m]!=1){
				ss=find(a,n,m);
				cout<<(char)(ch+m)<<(char)(ch+ss)<<" ";
				a[m]-=1;
				a[ss]-=1;
			}
			else{
				cout<<(char)(ch+m)<<" ";
				a[m]-=1;
			}
			f=check(a,n);
			
		}
	cout<<endl;
	}
	return 0;
}

