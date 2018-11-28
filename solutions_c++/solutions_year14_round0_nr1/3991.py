#include <iostream>
#include <algorithm>
#include <cstring>
#include <utility>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
using namespace std;

#define for1(i,n) for(i=0;i<n;i++)
#define for2(i,n) for(i=1;i<=n;i++)
#define all(v) v.begin(),v.end()
#define set(a,b) memset(a,b,sizeof a)
#define cin3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define cin2(a,b) scanf("%d%d",&a,&b)
#define cin1(a) scanf("%d",&a)
#define pb push_back
#define mp make_pair
#define inf  1e8

int main()
{
    int i,j,k,l,loop,ar1[4][4],ar2[4][4],ans1,ans2,count,crd;
    cin1(loop);
    for2(l,loop)
    {
        cin1(ans1);
        for1(i,4)
        {
            for1(j,4)
            {
                cin1(ar1[i][j]);
            }
        }

        cin1(ans2);
        for1(i,4)
        {
            for1(j,4)
            {
                cin1(ar2[i][j]);
            }
        }
        count=0;
        ans1--;
        ans2--;
        for1(i,4)
        {
            //cout<<"AR-1 - "<<ar1[ans1][i]<<endl;
            for1(j,4)
            {
                //cout<<"ARrr-2 - "<<ar2[ans2][j]<<endl;
                if(ar1[ans1][i]==ar2[ans2][j])
                {
                    count++;
                    crd=ar1[ans1][i];
                }
                if(count>1)
                {
                    break;
                }
            }
            if(count>1)
            {
                break;
            }
        }
        if(count==1)
        {
            printf("Case #%d: %d\n",l,crd);
        }
        else if(count==0)
        {
            printf("Case #%d: Volunteer cheated!\n",l);
        }
        else if(count>1)
        {
            printf("Case #%d: Bad magician!\n",l);
        }
    }
    return 0;
}
