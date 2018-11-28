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

vector<int> a, b;
vector<int> vec;
vector<int> res;
bool numeros[32];

int n;

int lis[32];
int lds[32];

bool check(int pos)
{
    int mn = 0;
    forn(i,n)
    if(vec[i]!=-1)
    {
        mn = i;
        break;
    }
    lis[mn] = 1;
    for(int i=mn+1;i<=pos;i++)
    if(vec[i]!=-1)
    {
        lis[i] = 1;
        for(int j=mn;j<i;j++)
        if(vec[j]!=-1&&vec[j]<vec[i])
            lis[i] = max(lis[i],lis[j]+1);
    }
    if(lis[pos]!=a[pos])
        return false;
    int mx = n-1;
    dforn(i,n)
    if(vec[i]!=-1)
    {
        mx = i;
        break;
    }
    lds[mx] = 1;
    for(int i=mx-1;i>=pos;i--)
    if(vec[i]!=-1)
    {
        lds[i] = 1;
        for(int j=i+1;j<=mx;j++)
        if(vec[j]!=-1&&vec[j]<vec[i])
            lds[i] = max(lds[i],lds[j]+1);
    }
    if(lds[pos]!=b[pos])
        return false;
    return true;
}


void bt(int num)
{
    if(num==n+1)
    {
        if(res.empty())
            res = vec;
        else
        {
            forn(i,res.size())
            if(res[i]<vec[i])
                return;
            else if(res[i]>vec[i])
            {
                res = vec;
                return;
            }
        }
        return;
    }
    forn(i,n)
    if(vec[i]==-1)
    {
        vec[i] = num;
        if(check(i))
            bt(num+1);
        vec[i] = -1;
    }
    return;
}

int main()
{
    freopen("C-small.in","r",stdin);
    freopen("C.out","w",stdout);
	int casos;
	cin >> casos;
	for(int casito=1;casito<=casos;casito++)
	{
	    cin >> n;
	    forn(i,n)
            numeros[i] = false;
	    a.resize(n);
	    b.resize(n);
	    res.clear();
	    forn(i,n)
            cin >> a[i];
        forn(i,n)
            cin >> b[i];
        vec.resize(n);
        forn(i,n)
            vec[i] = -1;
        forn(i,n)
        if(a[i]==1&&b[i]==1)
            vec[i] = 1;
        numeros[1] = true;
        bt(2);
	    cout << "Case #"<<casito<<":";
        forn(i,n)
            cout <<" "<< res[i];
        cout << endl;
	}
}
