#include<bits/stdc++.h>
using namespace std;
pair<int,char>p[26];
int main()
{
    freopen("input4.in","r",stdin);
    freopen("output4.txt","w",stdout);
    int a,b,d,e,f,g,h,i,j,k,l;
    cin>>a;
    for(i=1;i<=a;i++)
    {
        cin>>b;
        e=0;
        char c='A';
        for(j=0;j<b;j++)
        {
            cin>>d;
            e+=d;
            p[j]=make_pair(d,c);
            c++;
        }
        cout<<"Case #"<<i<<": ";
        while(e>0)
        {
            sort(p,p+b);
            cout<<p[b-1].second;
            p[b-1].first--;
            e--;
            sort(p,p+b);
            //for(j=0;j<b;j++)
              //  cout<<p[j].first<<p[j].second<<" ";
            if((e-1)/2>=p[b-2].first)
            {
                cout<<p[b-1].second;
                p[b-1].first--;
                e--;
            }
            cout<<" ";
        }
        cout<<"\n";
    }
    return 0;
}
