#include<iostream>
#include<vector>
#include<cstdio>
#include<algorithm>
#include<set>
#include<map>
#include<string>
#include<string.h>
#define all(c) c.begin(),c.end()
#define present(container,element) (conatiner.find(element)!=container.end())
#define cpresent(container,element) (find(all(container),element)!=container.end())
#define tr(container,it) for(typeof(container.begin()) it=container.begin();it!=container.end();it++)
#define MAX(a,b) (a)>=(b)?(a):(b)
#define MIN(a,b) (a)<=(b)?(a):(b)
#define MOD 1000000007
using namespace std;
//int a[101][4500000];
int n;
vector<int>v;
map<pair<int,long long int>,int>  mp;
int solve(int index,long long int sum)
{
    int i,j,ans;
    if(index==n)
        return 0;
    if(mp.find(make_pair(index,sum))==mp.end())
    {
        if(v[index]<sum)
        {
            ans=solve(index+1,sum+v[index]);

        }
        else
        {
            ans=1+solve(index+1,sum);
            if(2*sum-1>v[index])
                ans=min(ans,1+solve(index+1,v[index]+2*sum-1));
            else if(2*sum-1!=sum)
                ans=min(ans,1+solve(index,2*sum-1));
        }

       mp[make_pair(index,sum)]=ans;
    }

    return mp[make_pair(index,sum)];

}

int main()
{
    int i,j,k,A,t,cnt;
    scanf("%d",&cnt);
    t=1;
    while(t<=cnt)
    {
        scanf("%d%d",&A,&n);
    v.clear();
   /*for(i=0;i<=n+1;i++)
        for(j=0;j<=4444444;j++)
        a[i][j]=-1;*/
  mp.clear();

    for(i=0;i<n;i++)
        {scanf("%d",&j);
        v.push_back(j);
        }
        sort(v.begin(),v.end());
        printf("Case #%d: %d\n",t,solve(0,A));
       t++;
    }

 return 0;
}
