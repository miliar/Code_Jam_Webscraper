#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;
vector<int> a,b,c,d;
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("output-dlarge.out","w",stdout);
    int t,cc=1;
    scanf("%d",&t);
    while(cc<=t)
    {
        a.clear();
        b.clear();
        c.clear();
        d.clear();
        double r,s;
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
                scanf("%lf",&r);
                int temp=ceil(r*1000000.0);
                a.push_back(temp);
                c.push_back(temp);
        }
        for(int i=0;i<n;i++)
        {
                scanf("%lf",&s);
                int temp=ceil(s*1000000);
                b.push_back(temp);
                d.push_back(temp);
        }
        sort(a.rbegin(),a.rend());
        sort(b.rbegin(),b.rend());
        sort(c.rbegin(),c.rend());
        sort(d.rbegin(),d.rend());
        /*cout<<"a="<<endl;
        for(int i=0;i<n;i++)
                cout<<a[i]<<" ";
        cout<<endl;
        cout<<"b="<<endl;
        for(int i=0;i<n;i++)
                cout<<b[i]<<" ";
        cout<<endl;
        */int cnt1=0,f,pos,cnt2=0;
        for(int i=0;i<n;i++)
        {
                f=0;
                for(int j=0;j<b.size();j++)
                {
                if(b[j]<a[i])
                {
                f=1;
                pos=j;
                break;
                }
                }
                if(f)
                {
                b.erase(b.begin()+pos);
                cnt1++;
                }
        }
        for(int i=0;i<n;i++)
        {
                f=0;
               //cout<<"for ="<<d[i]<<endl;
                for(int j=0;j<c.size();j++)
                {
                if(c[j]<d[i])
                {
                f=1;
                pos=j;
                break;
                }
                }
                if(f)
                {
                //cout<<"shikar ="<<c[pos]<<endl;
                c.erase(c.begin()+pos);
                cnt2++;
                }
                
        }
       // cout<<cnt2<<endl;
        printf("Case #%d: %d %d\n",cc,cnt1,n-cnt2);
        cc++;    
    }
    return 0;
}
