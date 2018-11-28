#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;
int floor(int a,int b)
{
    if(a%b)
        return (a/b)+1;
    else
        return (a/b);

}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t; cin>>t;
    for(int kase=1;kase<=t;++kase)
    {
        int m; cin>>m;
        vector<int> ms;
        for(int i=0;i<m;++i)
        {
            int x; cin>>x;
            ms.push_back(x);
        }
        int res1 = 0;
        for(int i=0;i<(m-1);++i)
        {
            if(ms[i]>ms[i+1])
                res1+=(ms[i]-ms[i+1]);


        }
        int rate2 = 0;
        for(int i=0;i<(m-1);++i)
        {
            if(ms[i]>ms[i+1])
                rate2 = max(rate2,ms[i]-ms[i+1]);
        }
        int res2 = 0,cur=0;
        for(int i=0;i<(m-1);++i)
        {

            cur=ms[i];
            res2+=min(cur,rate2);
            cur-=min(cur,rate2);

        }

        cout<<"Case #"<<kase<<": "<<res1<<" "<<res2<<"\n";


    }
}
