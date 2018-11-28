#include <cstdio>
#include <iostream>
#include <string>
using namespace std;
int T,N,sum,friends;
int main()
{
    freopen("ProblemA.in","r",stdin);
    freopen("ProblemB.out","w",stdout);
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        string s;
        cin>>N>>s;
        sum=0;friends=0;
        for(int j=0;j<=N;j++)
        {
            if(sum<j)
            {
                friends+=j-sum;
                sum=j;
            }
            sum+=int(s[j])-48;
        }
        printf("Case #%d: %d\n",i,friends);
    }
    return 0;
}
