#include<bits/stdc++.h>
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<map>
#include<stack>
#include<queue>
#include<set>
#include<vector>
#include<set>
#include<deque>
#include<utility>
#include<algorithm>
#include<bitset>
#include<climits>
#include <sstream>
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define PB push_back
#define MP make_pair
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define INF 1000000000
#define M 1000000007
typedef long long int LL;
typedef long long               ll;
typedef unsigned int            uint;
typedef unsigned long long int     ull;
#define mem(a,b) memset(a,b,sizeof a)
using namespace std;
vector<LL> V[20];
LL ans[20][20];
int main()
{
    LL T;
    ans[0][0]=0;ans[0][2]=2;ans[0][4]=4;ans[0][6]=6;ans[2][0]=2;ans[2][2]=1;ans[2][4]=6;ans[2][6]=5;
    ans[4][0]=4;ans[4][2]=7;ans[4][4]=1;ans[4][6]=2;ans[6][0]=6;ans[6][2]=4;ans[6][4]=3;ans[6][6]=1;
    ifstream filein("input.in");
    ofstream fileout("output.txt");
    filein>>T;
    string tmp,str="";
    for(LL t=1;t<=T;t++)
    {
        fileout<<"Case #"<<t<<": ";
        LL l,x;
        LL sum[40005];
       filein>>l>>x;
        for(LL i=0;i<20;i++)
            V[i].clear();
        filein>>tmp;
        str="";
        for(LL i=0;i<min((LL)4,x);i++)
            str+=tmp;
        int mark[5]={0},j=1;
        sum[0]=(str[0]=='i'?2:(str[0]=='j'?4:6));
        if((0%l==l-1)){
                if(sum[0]==1)
                    mark[j]=1;
                j++;
            }
        V[sum[0]].push_back(0);
        for(LL i=1;i<l*min((LL)4,x);i++)
        {
            LL p=(str[i]=='i'?2:(str[i]=='j'?4:6));
            if(sum[i-1]&1){
            sum[i]=ans[sum[i-1]-1][p];
            if(sum[i]&1)
                sum[i]-=1;
            else
                sum[i]+=1;
            }
            else
            {
                sum[i]=ans[sum[i-1]][p];
            }
            V[sum[i]].push_back(i);
            if(i%l==l-1){
                if(sum[i]==1)
                    mark[j]=1;
                j++;
            }
        }
        LL temp=(x-1)%4+1;
        if(mark[temp]==0)
        {
             fileout<<"NO\n";
             continue;
        }
        int chk=0;
        int minsz=V[1].size();
        int isz=V[2].size();
        int ksz=V[6].size();

            if(isz>0 && ksz>0)
            {
               if(upper_bound(V[6].begin(),V[6].end(),V[2][0])!=V[6].end())
                chk=1;
               else
               {
                    LL p=V[6][0];
                    LL block=p/l+1;
                    if(block+4<=x)
                        chk=1;
                    else
                        chk=0;
               }
            }
               else
                chk=0;
        if(chk==1)
             fileout<<"YES\n";
        else
            fileout<<"NO\n";
    }
    return 0;
}
