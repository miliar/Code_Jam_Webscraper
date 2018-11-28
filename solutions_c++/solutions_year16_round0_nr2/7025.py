#include<bits/stdc++.h>
using namespace std;
int a[201]={0};
void reverseAndChange(int i,int j){
	for(int k=i,l=j;k<=l;k++,l--){
		a[k]=!a[k];
		if(k!=l){
			a[l]=!a[l];
			swap(a[k],a[l]);
		}
	}
}
void print(int i,int j){
	for(int s=i;s<=j;s++)
		cout<<a[s];
	cout<<'\n';
}
int st=0;
void Count(int s,int e){
	//~ cout<<"Count "<<s<<' '<<e<<'\n';
	//~ cin.get();
	//~ print(s,e);
	int flag=1;
	for(int i=s;i<=e;i++)
		if(a[i]==0)
			flag=0;
	
	if(flag==1)
		return;
	
	if(a[s]!=0){
		int f=s;
		while(a[f]!=0) f++;
		st++;
		reverseAndChange(s,f-1);
	}
	//~ cout<<s<<','<<e<<'\n';
	//~ print(s,e);
	reverseAndChange(s,e);
	st++;
	//~ print(s,e);
	//~ cin.get();
	int l=e;
	
	while(a[l]==1 && (l-1)>=s)
		l--;
	flag=1;
	for(int i=s;i<=e;i++)
		if(a[i]==0)
			flag=0;
	
	if(flag==1)
		return;	
	//~ print(s,e);
	Count(s,l);
}

int main(){
	cout.sync_with_stdio(0);
	cin.tie(0);
	int t,te=1;
	cin>>t;
	while(t--){
		string b;
		cin>>b;
		st=0;
		for(int i=0;i<(int)b.length();i++)
			if(b[i]=='+')
				a[i]=1;
			else
				a[i]=0;
		
		int s=0,e=b.length()-1;
		int l=e;
		while(a[l]==1 && (l-1)>=s)
			l--;
		Count(s,l);
		cout<<"Case #"<<te++<<": "<<st<<'\n';
	}
}
