#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<utility>
using namespace std;

#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define pob pop_back
#define ll long long
#define MAX_SIZE 200005
#define MOD 1000000007
#define S(x) scanf("%d",&x)
#define SL(x) cin>>x
#define SC(x) scanf("%c",&x)
#define SS(x) scanf("%s",x)
#define SZ(x) x.size()
#define IT iterator
#define PI pair<int,int>
#define PL pair<ll,ll>
#define VI vector<int>
#define VL vector<ll>
#define VVI vector< VI >
#define VVL vector< VL >
#define VVP vector< PI >
#define READ() freopen("/Users/home/Desktop/input.txt","r",stdin)
#define WRITE() freopen("/Users/home/Desktop/output.txt","w",stdout)
#define dump() SC(dump_char)
int dump_char;

int main()
{
    READ();
    WRITE();
    int k,t,arr[4][4],i,j,ch;
    S(t);
    
    for(k=1;k<=t;k++)
    {
        set<int> s;
        
        S(ch);
        ch--;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                S(arr[i][j]);
        
        for(i=0;i<4;i++)
            s.insert(arr[ch][i]);
        
        int cnt=0,ans;
        
        S(ch);
        ch--;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                S(arr[i][j]);
        
        for(i=0;i<4;i++)
        {
            if(s.find(arr[ch][i])!=s.end())
            {
                cnt++;
                ans=arr[ch][i];
            }
        }
        printf("Case #%d: ",k);
        if(cnt==0)
            printf("Volunteer cheated!");
        else if(cnt==1)
            printf("%d",ans);
        else
            printf("Bad magician!");
        printf("\n");
    }
    return 0;
}