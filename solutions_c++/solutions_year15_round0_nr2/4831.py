#include<bits/stdc++.h>
using namespace std;
#define INF 1000000

int cal(map<int,int> &m,int stall)
{
    if(m.size()==1 && m.find(1)!=m.end())
    {
        return stall+1;;
    }

    map<int,int>::iterator it;
    it=m.end();
    it--;
    int n=it->first;
    int freq=it->second;
    int minm=stall+it->first;

    for(int i=2;i<=n;i++)
    {
        map<int,int> temp;
        map<int,int>::iterator start,last;
        start=m.begin();
        last=m.end();last--;

        while(start!=last)
        {
            temp[start->first]=start->second;
            start++;
        }

        if(i>n/2)
        {
            if(n-i)
            temp[2]+=n-i;
            temp[1]+=2*i-n;
        }

        else
        {
            if(n%i==0)
            {
                temp[n/i]+=freq*i;
            }
            else
            {
                int part=n/i;
                int left=n%i;
                int part2=part+1;
                int freq2=freq*left;
                int freq1=freq*(i-left);
                temp[part]+=freq1;
                temp[part2]+=freq2;
            }
        }
        minm=min(minm,cal(temp,stall+((i-1)*freq)) );
    }
    return minm;
}
int main()
{
    int t;
    scanf("%d",&t);
    int cases=1;
    while(t--)
    {
        int n;
        scanf("%d",&n);
        map<int,int> m;

        for(int i=0;i<n;i++)
        {
            int temp;
            scanf("%d",&temp);
            m[temp]++;
        }

        int ans=cal(m,0);
        printf("Case #%d: %d\n",cases,ans);
        cases++;
    }
}
