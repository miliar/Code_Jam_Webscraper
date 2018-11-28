/* In the name of ALLAH, most gracious, most merciful */
#include <iostream>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <ios>
#include <map>
#include <set>
#include <algorithm>
#include <cstring>
#include <ctime>
#include <queue>
#include <cassert>
#include <cmath>
#include <string>
#include <stack>

using namespace std;

typedef long long ll;
/*
int reverse(int a)
{
	int ret=0;
	while(a)
	{
		ret*=10;
		ret+=a%10;
		a/=10;
	}
	return ret;
}
int dp[1000009];
int solve(int n)
{
	if(n==1)
		return dp[1]=1;
	int &ret=dp[n];
	if(ret!=-1)
		return ret;
	ret=1+solve(n-1);
	int t=reverse(n);
	if(n%10!=0 && t<n)
	{
		ret=min(ret,1+solve(t));
	}
	return ret;
}

bool check(int n)
{
	if(n<10)return 1;
	//cout<<n<<endl;
	vector<int> v;
	while(n){
		v.push_back(n%10);
		n/=10;
	}
	int s=0;
	int e=v.size()-1;
	while(s<=e)
	{
		if(v[e]!=1)
		  return v[s]==1;
		if(v[s]!=1)
			return 0;
		s++;
		e--;
	}
	//cout<<n<<endl;
	return 0;
}
int solve2(int n)
{
	int ret=0;

	while(n>0)
	{
		//cout<<n<<endl;
		while(!check(n)) { n--;ret++;}
		//cout<<n<<endl;
		int t=reverse(n);
		if(n>10 && n%10!=0 && t<n && (n-t) > 1)
		{
			n=t;
		}
		else
			n--;

		ret++;
	}
	return ret;
}
*/
int r,c,n;

int arr[29][29];

int sx[]={0,1};
int sy[]={1,0};


int get_v(int k)
{
	int h=0;
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			arr[i][j]=(k>>h)&1;
			h++;
		}
	}
	int ret=0;
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			for(int d=0;d<2;d++)
			{
				int nx=i+sx[d];
				int ny=j+sy[d];
				if(nx< r && ny <c)
				{
					ret+=(arr[i][j] & arr[nx][ny]);
				}

			}
		}
	}

	return ret;

}
int C(int n)
{
	int ret=0;
	for(int i=0;i<30;i++)
		ret+=((n>>i)&1);
	return ret;
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("2.in", "r", stdin);
	freopen("2.out", "w", stdout);
#endif
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int tc;
    cin>>tc;
    int ic=1;
    while(tc--)
    {
    	cin>>r>>c>>n;
    	int k=r*c;
    	int ret=1<<30;
    	for(int i=0;i<(1<<k);i++)
    	{
    		if(C(i)==n)
    		{
    			ret=min(ret,get_v(i));
    		}
    	}

    	cout<<"Case #"<<ic++<<": "<<ret<<endl;
    }


    return 0;
}
