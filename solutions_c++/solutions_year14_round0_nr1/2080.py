#pragma warning(disable:4996)
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
#define LL long long
#define mod 1000000007
int map[4][4],map2[4][4];
int a[17],b[17];
int main(){
	//freopen("in.in","r",stdin);
	//freopen("out","w",stdout);
	int cas = 0,t;
	int n,m,ans = 1;
	cin>>t;
	while(t--){
		cin>>n;
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin>>map[i][j];
				if(i == n-1)a[map[i][j]] = 1;
			}
		}
		cin>>m;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin>>map2[i][j];
				if(i == m-1)b[map2[i][j]] = 1;
			}
		}
		int num = 0;
		for (int i = 1; i < 17; i++)
		{
			if(a[i] && b[i])num++;
		}
		cout<<"Case #"<<++cas<<": ";
		if(num > 1)cout<<"Bad magician!"<<endl;
		else if(num == 0)cout<<"Volunteer cheated!"<<endl;
		else {
			for (int i = 1; i < 17; i++)
			{
				if(a[i] && b[i]){cout<<i<<endl;break;}
			}
		}
	}
	return 0;
}