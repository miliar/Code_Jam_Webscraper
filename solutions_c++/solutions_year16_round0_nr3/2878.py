#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;

long long pw[11][17];
int a[20];
int stk[11],top;
bool check(int id)
{
	long long x=1;
	x+=pw[id][16];
	for(int i=2;i<=15;i++) x+=pw[id][i]*a[i];
	
	for(int k=2;(long long)k*k<=x;k++)
		if(x%k==0){stk[id]=k;return 1;}
	return 0;
}

int main()
{
	freopen("cs.out","w",stdout);
	for(int i=2;i<=10;i++) pw[i][1]=1;
	for(int i=2;i<=10;i++)
	{
		for(int j=2;j<=16;j++) pw[i][j]=(long long)pw[i][j-1]*i;
	}
	int cnt=0,T;int x,y;
	cin>>T>>x>>y;
	cout<<"Case #1:\n";
	for(a[2]=0;a[2]<=1;a[2]++)
	for(a[3]=0;a[3]<=1;a[3]++)
	for(a[4]=0;a[4]<=1;a[4]++)
	for(a[5]=0;a[5]<=1;a[5]++)
	for(a[6]=0;a[6]<=1;a[6]++)
	for(a[7]=0;a[7]<=1;a[7]++)
	for(a[8]=0;a[8]<=1;a[8]++)
	for(a[9]=0;a[9]<=1;a[9]++)
	for(a[10]=0;a[10]<=1;a[10]++)
	for(a[11]=0;a[11]<=1;a[11]++)
	for(a[12]=0;a[12]<=1;a[12]++)
	for(a[13]=0;a[13]<=1;a[13]++)
	for(a[14]=0;a[14]<=1;a[14]++)
	for(a[15]=0;a[15]<=1;a[15]++)
	{
		bool f=1;
		if(cnt==50) goto loop;
		for(int i=2;i<=10;i++)
			if(!check(i)) {f=0; break;}
		if(f) 
		{cnt++;cout<<1;for(int i=15;i>=2;i--) cout<<a[i];cout<<1<<' ';for(int i=2;i<=10;i++) cout<<stk[i]<<' ';cout<<endl;}
	}
	loop:
	return 0;
}
