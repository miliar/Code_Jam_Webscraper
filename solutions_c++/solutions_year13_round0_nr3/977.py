/*
TASK: Fair and Square
LANG: C++
*/
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<queue>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
using namespace std;
#define X first
#define Y second
#define EPS 1e-9
#define ALL(x) (x).begin(),(x).end()
typedef pair<int,int> PII;
typedef long long LL;

int N,M,T;
int main()
{
    freopen("C-large-1.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
    string a,b;
    long long x;
    vector<long long> v;
    vector<long long>::iterator it;
    for(i=1;i<=10000000;i++)
    {
        stringstream ss;
        ss << i;    ss >> a;
        b=a;    reverse(ALL(b));
        if(a!=b)   continue;
        x=i;    x*=i;
        stringstream ss2;
        ss2 << x;    ss2 >> a;
        b=a;    reverse(ALL(b));
        if(a==b)   v.push_back(x);
    }
    scanf("%d",&T);
    long long p,q;
    int ii=0;
    while(T--)
    {
        cin >> p >> q;
        k=0;
        for(i=0;i<v.size();i++)
            if(p<=v[i] && v[i]<=q)
                k++;
        printf("Case #%d: %d\n",++ii,k);
    }
}
