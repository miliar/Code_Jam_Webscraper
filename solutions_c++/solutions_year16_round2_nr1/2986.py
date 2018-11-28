#include<bits/stdc++.h>
#define ll long long 
#define pb push_back
#define mp make_pair
#define si(i) scanf("%d",&i)
#define fs first
#define sc second
#define pii pair<int,int>
#define psi pair<string,int>
#define FOR(i,j,k) for(int i=j;i<k;i++)
#define REP(i,k) for(int i=0;i<k;i++)
#define FORR(i,j,k) for(int i=n;i>=k;i--)
#define MOD 1000000007
using namespace std;
int main()
{
	int t,c=1;
	si(t);
	while(t--)
	{
		string s;	
		int arr[127]={0};
		int f[10]={0};
		cin	>> s;
		int l =s.length();
		FOR(i,0,l)
		{
			arr[s[i]]++;
		}
		if(arr['Z'])
		{
			f[0] = arr['Z'];
			arr['Z']=0;
			arr['E']-=f[0];
			arr['O']-=f[0];
			arr['R']-=f[0];
		}
		if(arr['W'])
		{
			f[2] = arr['W'];
			arr['W'] = 0;
			arr['T']-=f[2];
			arr['O']-=f[2];
		}
		if(arr['X'])
		{
			f[6] = arr['X'];
			arr['X'] =0;
			arr['S']-=f[6];
			arr['I']-=f[6];
		}
		if(arr['U'])
		{
			f[4] = arr['U'];
			arr['U'] = 0;
			arr['F']-=f[4];
			arr['R']-=f[4];
			arr['O']-=f[4];
		}
		if(arr['G'] > 0)
		{
			f[8] = arr['G'];
			arr['E']-=f[8];
			arr['I']-=f[8];
			arr['G']-=f[8];
			arr['H']-=f[8];
			arr['T']-=f[8];
		}
		if(arr['R'] > 0)
		{
			f[3] = arr['R'];
			arr['T']-=f[3];
			arr['R']-=f[3];
			arr['H']-=f[3];
			arr['E']-=2*f[3];
		}
		if(arr['S'])
		{
			f[7] = arr['S'];
			arr['S']-=f[7];
			arr['E']-=2*f[7];
			arr['V']-=f[7];
			arr['N']-=f[7];
		}
		if(arr['F'])
		{
			f[5] = arr['F'];
			arr['F']-=f[5];
			arr['I']-=f[5];
			arr['V']-=f[5];
			arr['E']-=f[5];
		}
		if(arr['O'])
		{
			f[1] = arr['O'];
			arr['O']-=f[1];
			arr['N']-=f[1];
			arr['E']-=f[1];
		}
		if(arr['N'])
		{
			f[9] = arr['N']/2;
		}
		printf("Case #%d: ",c++);
		FOR(i,0,10)
		{
			while(f[i]){
				cout << i;
				f[i]--;
			}
		}
		cout << endl;
	}
	return 0;
}