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
        printf("Case #%d: ",x);
        int n;
        cin>>n;
        
        int a,tot=0;
        vii v;
        for(int i=0;i<n;i++)
        {
            cin>>a;
            v.pb(mp(a,i));
            tot+=a;
        }
        vector<string> ans;
        sort(v.rbegin(),v.rend());
        while(1)
        {
            int t1=v[0].fi;
            int t2=v[1].fi;
            if(t1==0)
                break;
            char c1=v[0].sc+'A';
            char c2=v[1].sc+'A';
            //printf("%c %c\n",c1,c2);
            string a="";
            if(t1==1)
         {
            if(tot%2==0)a+=c1,a+=c2,v[0].fi--,v[1].fi--,tot-=2;
            else a+=c1,v[0].fi--,tot--;
         }
         else
         {
            if(t2<= tot -2- t2)a+=c1,a+=c1,tot-=2,v[0].fi-=2;
            else a+=c1,a+=c2,tot-=2,v[0].fi--,v[1].fi--;
         }

         ans.pb(a);
         sort(v.rbegin(),v.rend());
        }
        for(int i=0;i<ans.size();i++)
            cout<<ans[i]<<' ';
        printf("\n");



    }
 
    return 0;
}
 