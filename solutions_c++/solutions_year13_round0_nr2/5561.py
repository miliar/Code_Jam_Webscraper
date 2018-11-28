#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;
int main()
{
		ifstream fin("C:\\Users\\sesir_000\\Documents\\C++ stuff\\A.in");
	ofstream fout("C:\\Users\\sesir_000\\Documents\\C++ stuff\\C.out");
	
	int n,p,q,i,j,c[200][200],b[200][200];
	fin>>n;
	for(int a=1;a<=n;a++){
	for(i=0;i<200;i++)for(j=0;j<200;j++)b[i][j]=100;
	fin>>p>>q;
	for(i=0;i<p;i++)for(j=0;j<q;j++)fin>>c[i][j];
	for(i=0;i<p;i++)
	{
		int m=0;
		for(j=0;j<q;j++)
		if(c[i][j]>m)m=c[i][j];
		for(j=0;j<q;j++)
		b[i][j]=m;
	}
	for(j=0;j<q;j++)
	{
		int m=1000,flag=0;
		for(i=0;i<p;i++)
		if(c[i][j]<m&&c[i][j]!=b[i][j]){m=c[i][j];flag=1;}
		if(flag==1){
		for(i=0;i<p;i++)
		b[i][j]=m;}
	}
	int fl=1;
	for(i=0;i<p;i++)
	for(j=0;j<q;j++)
	{
	if(b[i][j]!=c[i][j])fl=0;
	}
	if(fl==0)fout<<"Case #"<<a<<": "<<"NO"<<endl;
	else fout<<"Case #"<<a<<": "<<"YES"<<endl;
}
	return 0;
}

