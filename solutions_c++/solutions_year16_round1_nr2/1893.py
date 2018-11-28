#include <stdio.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <stdlib.h>
#include <math.h>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
 
using namespace std;
 
#define fi first
#define sc second
#define ff first.first
#define fs first.second
#define sf second.first
#define ss second.second
#define pb push_back
#define mp make_pair
#define ll long long
#define dl double
#define ison(a,b) (a&(1<<b))
#define bitcnt __builtin_popcount
#define MOD 1000000007 
#define INF 1000000000
 
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<iii> wadj;


int main(int argc, char const *argv[])
{
//freopen("inp.txt","r",stdin);
 //freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int x=1;x<=t;x++)
    {
        int fre[2600];
        memset(fre,0,sizeof(fre));
        int n;
        cin>>n;
        for(int i=0;i<2*n-1;i++)
        {
            for(int j=0;j<n;j++)
            {
                int a;
                cin>>a;
                fre[a]++;
            }
        }
        vi v;
        for(int i=0;i<=2500;i++)
            if(fre[i]&&fre[i]%2)
                v.pb(i);
            printf("Case #%d: ",x);
            sort(v.begin(),v.end());
            for(auto i : v)
                printf("%d ",i);
            printf("\n");
    }
 
    return 0;
}
 