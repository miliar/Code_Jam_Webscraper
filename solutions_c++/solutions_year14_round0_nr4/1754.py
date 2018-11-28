#include<iostream>
#include<vector>
#include<cstdio>
#include<iomanip>
#include<algorithm>
using namespace std;
int main()
{
    int t;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n;
        cin>>n;
        vector<double> a,b,b1;
        double p;
        int p1=0,p2=0;
        for(int j=0;j<n;j++){cin>>p;a.push_back(p);}
        for(int j=0;j<n;j++){cin>>p;b.push_back(p);b1.push_back(p);}
        sort(a.begin(),a.end());
        for(int j=0;j<n;j++)
        {
            for(int o=0;o<b1.size();o++)
                if(a[j]>b1[o])
                {
                    b1.erase(b1.begin()+o);
                    p1++;break;
                }
        }
        sort(b.begin(),b.end());
        for(int j=0;j<n;j++)
        {
            bool can=0;
            for(int o=0;o<b.size();o++)
                if(a[j]<b[o])
                {
                        b.erase(b.begin()+o);
                        can=1;break;
                }
            if(can==0)p2++;
        }
        cout<<"Case #"<<i+1<<": "<<p1<<" "<<p2<<endl;
    }
    return 0;
}
