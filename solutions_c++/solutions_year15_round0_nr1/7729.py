#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
#include <cstdio>
#include <vector>
#include <bitset>
#include <limits>
#include <fstream>
#include <cstring>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
using namespace std;

#define nmax 1010
#define mod 1000007
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define inf numeric_limits<int>::max()
#define forv(v,it) for (vector<int>::iterator it=v.begin();it!=v.end();it++)

int tst,rez,n,pers,more,nr;
char s[nmax];

int main()
{
    int i,j;
    cin>>tst;
    for (j=1;j<=tst;j++)
    {
        cin>>n;cin>>s;
        pers+=s[0]-'0';
        for (i=1;s[i];i++)
        {
            nr=s[i]-'0';
            if (i>pers && nr) {more+=i-pers;pers=i+nr;}
            else pers+=nr;
        }
        cout<<"Case #"<<j<<": "<<more<<'\n';
        more=pers=0;
    }
}
