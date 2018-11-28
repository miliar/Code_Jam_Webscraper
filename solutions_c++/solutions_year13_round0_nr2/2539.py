
#include<iostream>
#include<string>
using namespace std;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	for (int ct=1;ct<=t;++ct){
		int flag=false;
		int m,n;
		int a[100][100];
		int b[100],c[100];
		cin>>m>>n;
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		memset(c,0,sizeof(c));
		for (int i=0;i<m;++i)
			for (int j=0;j<n;++j){
				cin>>a[i][j];
			}
		for (int i=0;i<m;++i)
			for (int j=0;j<n;++j){
				if (b[i]<a[i][j])b[i]=a[i][j];
				if (c[j]<a[i][j])c[j]=a[i][j];
			}
		for (int i=0;i<m;++i)
			for (int j=0;j<n;++j)
				if (a[i][j]<b[i]&& a[i][j]<c[j])flag=true;
		if (flag==false)cout<<"Case #"<<ct<<": YES"<<endl;
		else cout<<"Case #"<<ct<<": NO"<<endl;


	}

}