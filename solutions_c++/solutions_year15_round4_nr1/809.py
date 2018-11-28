#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(i=a;i<b;++i)
#define repi(i,a,b) for(int i=a;i<b;++i)
#define F first
#define S second
#define mp(a,b) make_pair(a,b)
#define pii pair<int,int>
#define ppi pair<pii,int>
#define ppp pair<pii,pii>
#define vi vector<int>
#define sc(a) scanf("%d",&a)
#define pb(a) push_back(a)
int r,c;

string a[100];
bool change[100][100];
int check()
{
	for(int i=0;i<r;++i)for(int j=0;j<c;++j)change[i][j]=false;
	
	for(int i=0;i<r;++i)
	{
		for(int j = 0;j<c;++j)
		{
			if(a[i][j]=='.')continue;
			
			if(a[i][j]=='v')
			{
				int ii;
				for(ii=i+1;ii<r;++ii)
					if(a[ii][j]!='.')break;
				if(ii==r)
					change[i][j]=true;
			}
			if(a[i][j]=='>')
			{
				int jj;
				for(jj=j+1;jj<c;++jj)
					if(a[i][jj]!='.')break;
				if(jj==c)
					change[i][j]=true;
			}
			if(a[i][j]=='<')
			{
				int jj;
				for(jj=j-1;jj>=0;--jj)
					if(a[i][jj]!='.')break;
				if(jj==-1)
					change[i][j]=true;
			}
			if(a[i][j]=='^')
			{
				int ii;
				for(ii=i-1;ii>=0;--ii)
					if(a[ii][j]!='.')break;
				if(ii==-1)
					change[i][j]=true;
			}
		}
	}
	int numchange=0;
	for(int i=0;i<r;++i) for(int j=0;j<c;++j)if(change[i][j]==true)
	{
		++numchange;
		int numb=0;
		for(int ii=0;ii<r;++ii)
		{
			if(a[ii][j]!='.')++numb;
		}
		//cout<<i<<" "<<j<<" "<<numb<<endl;
		for(int jj=0;jj<c;++jj)
		{
			if(a[i][jj]!='.')++numb;
		}
		//cout<<i<<" "<<j<<" "<<numb<<endl;
		if(numb==2)return -1;
	}
	return numchange;
}
int main() {
	// your code goes here
	int cases;
	cin>>cases;
	for(int case_t = 1; case_t<=cases;++case_t)
	{
		cout<<"Case #"<<case_t<<": ";
		cin>>r>>c;
		for(int i = 0; i<r; ++i)cin>>a[i];
		int ans = check();
		if(ans==-1)cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;
	}
	return 0;
}