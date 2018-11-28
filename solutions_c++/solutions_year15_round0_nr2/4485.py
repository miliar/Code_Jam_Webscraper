#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;
int fun(vector<int> P, int time)
{
    sort(P.begin(),P.end());
    int len=P.size();
    int val=P[len-1];
    if(val==0)
    return time;
    else if(val==1)
    return time+1;
    else
    {
        /*
        cout<<"\nP ";
        for(int i=0;i<P.size();i++)
        cout<<P[i]<<" ";
        */
        vector<int> X,Y;
        for(int i=0;i<P.size();i++)
        {
            X.push_back(P[i]-1);
            Y.push_back(P[i]);
        }
        int store=2;
        bool q=0;

        for(int i=2;i<=sqrt(val)&&!q;i++)
        {
            if(val%i==0)
            {
                q=1;
                store=i;
            }
        }
        int temp = val-val/store;
        Y[len-1]/=store;
        Y.push_back(temp);
        /*
        cout<<"\n X ";
        for(int i=0;i<X.size();i++)
        cout<<X[i]<<" ";
        cout<<"\n Y ";
        for(int i=0;i<Y.size();i++)
        cout<<Y[i]<<" ";
        */
        return min(fun(X,time+1),fun(Y,time+1));
    }
}
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int idx=1;
    while(t--)
    {
        int D;
        scanf("%d",&D);
        vector <int> P;
        int a;
        for(int i=1;i<=D;i++)
        {
            scanf("%d",&a);
            P.push_back(a);
        }
        int ans;
        ans = fun(P,0);
        printf("Case #%d: %d\n",idx,ans);
        ++idx;
    }
    return 0;
}
