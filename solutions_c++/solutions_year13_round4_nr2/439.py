#include<algorithm>
#include<cmath>
#include<cstdio>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<string>
#include<vector>

#define forn(i,n) for(int i=0;i<(int)n;i++)
#define dforn(i,n) for(int i=(int)n-1;i>=0;i--)
#define all(v) v.begin(),v.end()

using namespace std;

long long calc1(long long k, long long n, long long teams)
{
    if(k%2==0)
        return k/2-1;
    else
        return k/2;
}

bool ganaSeguro(long long k, long long n, long long teams, long long p)
{
    if(k==0)
        return true;
    if(n==1&&k==1)
    {
        if(p==1)
            return false;
        if(p==2)
            return true;
    }
    if(p<=teams/2)
        return false;
    p-=teams/2;
    long long k2 = calc1(k,n,teams);
    return ganaSeguro(k2,n-1,teams/2,p);
}

long long calc2(long long k, long long n, long long teams)
{
    if(k%2==0)
        return k/2;
    else
        return k/2+1;
}

bool ganaMaybe(long long k, long long n, long long teams, long long p)
{
    if(k==0)
        return true;
    if(n==1&&k==1)
    {
        if(p==1)
            return false;
        if(p>1)
            return true;
    }
    if(p>=teams)
        return true;
    if(k==teams-1)
        return false;
    long long k2 = calc2(k,n,teams);
    return ganaMaybe(k2,n-1,teams/2,min(p,teams/2));
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
	int casos;
	cin >> casos;
	for(int casito=1;casito<=casos;casito++)
	{
	    long long teams, n, p;
	    cin >> n >> p;
	    teams = (1LL<<n);
	    long long maxWin = teams;
	    long long minWin = 0;
	    while(maxWin-minWin>1)
	    {
	        long long k = (maxWin+minWin)/2;
	        if(ganaSeguro(k,n,teams,p))
                minWin = k;
            else
                maxWin = k;
	    }
	    long long maxCan = teams;
	    long long minCan = 0;
	    while(maxCan-minCan>1)
	    {
	        long long k = (maxCan+minCan)/2;
	        if(ganaMaybe(k,n,teams,p))
                minCan = k;
            else
                maxCan = k;
	    }
	    cout << "Case #"<<casito<<": "<< minWin <<" "<< minCan << endl;
	}
}
