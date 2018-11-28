#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int i = 0;i< t;i++)
    {
        int n;
        cin>>n;
        pair<int,int> p[n];
        for(int i = 0;i< n;i++)
        {
            int c;
            cin>>c;
            p[i].first = c;
            p[i].second = i;

        }
        sort(p,p+n);
        int sz = n;
        cout<<"Case #"<<i+1<<": ";
        while(p[0].first != 0)
        {
            sort(p,p+sz);
            if(p[sz-1].first == p[sz-2].first)
            {
                if(sz-3>=0&&p[sz-2].first == p[sz-3].first)
                {
                        cout<<char(p[sz-1].second+65)<<" ";
                        p[sz-1].first--;
                        if(p[sz-1].first == 0)
                        {
                            sz--;
                        }
                }
                else
                {
                     cout<<char(p[sz-1].second+65)<<char(p[sz-2].second+65)<<" ";
                     p[sz-1].first--;
                     p[sz-2].first--;
                     if(p[sz-1].first == 0)
                     {
                         sz-=2;
                     }
                }
            }
            else
            {
                        cout<<char(p[sz-1].second+65)<<" ";
                        p[sz-1].first--;
                        if(p[sz-1].first == 0)
                        {
                            sz--;
                        }
            }
        }
        cout<<endl;
    }
}
