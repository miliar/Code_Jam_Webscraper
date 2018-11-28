#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,c=0;
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        int n,x,i;
        cin>>n;
        int a[n];
        priority_queue<int>q;
        for(i=0;i<n;i++)
        {
            cin>>a[i];
            q.push(a[i]);
        }
        int ans=0,m1,an=1e8;
        int mm=q.top();
        int tmp=mm;
        while(mm)
        {
            ans=mm;
            for(x=0;x<n;x++)
            {
                if(a[x]>mm)
                ans=ans+((a[x]-mm)/mm);
                if(a[x]>mm && a[x]%mm)
                ans++;
            }
            mm--;
            an=min(an,ans);
        }
        c++;
       cout<<"Case #"<<c<<": "<<an<<endl;
        while(!q.empty())
            q.pop();
        }

    return 0;
}

