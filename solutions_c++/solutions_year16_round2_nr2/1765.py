#include<bits/stdc++.h>
#include<string>
using namespace std;
int main()
{
   freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int x=1;x<=t;x++)
    {
        vector<string> v;
        vector<string> vc,vs;
  string c,s;
    cin>>c>>s;
    v.push_back(c);
    for(int i=0;i<v.size();i++)
    {
        bool flag=false;
for(int j=0;j<v[i].size();j++)
        {
        if(v[i][j]=='?')
        {
            flag=true;
            for(int k=0;k<=9;k++)
            {
                v[i][j]=k+48;
                v.push_back(v[i]);
            }
        }
        }
        if(!flag)
            vc.push_back(v[i]);
    }
    v.clear();
    v.push_back(s);
    for(int i=0;i<v.size();i++)
    {
        bool flag=false;
        for(int j=0;j<v[i].size();j++)
        {
        if(v[i][j]=='?')
        {
            flag=true;
            for(int k=0;k<=9;k++)
            {
                v[i][j]=k+48;
                v.push_back(v[i]);
            }
        }
        }
        if(!flag)
            vs.push_back(v[i]);
    }
    int min=INT_MAX,minc=INT_MAX,mins=INT_MAX,a,b;
    for(int i=0;i<vc.size();i++)
    {
        for(int j=0;j<vs.size();j++)
        {
            a=atoi(vc[i].c_str());
            b=atoi(vs[j].c_str());
            if(a-b>0)
            {
                if(a-b<min)
                {
                    min=a-b;
                    minc=a;
                    mins=b;
                }
                else if(a-b==min)
                {
                    if(minc>a)
                        minc=a,mins=b;
                    else if(minc==a)
                    {
                        if(mins>b)
                            mins=b,minc=a;
                    }
                }
            }
            else if(b-a>=0)
            {
                if(b-a<min)
                {
                    min=b-a;
                    minc=a;
                    mins=b;
                }
                else if(b-a==min)
                {
                    if(minc>a)
                        minc=a,mins=b;
                    else if(minc==a)
                    {
                        if(mins>b)
                            mins=b,minc=a;
                    }
                }
            }
        }
    }
    int l1=0,l2=0,c1=0,c2=0,tmp1=minc;
    while(tmp1>0)
    {
        tmp1/=10;
        l1++;
    }
    tmp1=mins;
    while(tmp1>0)
    {
        tmp1/=10;
        l2++;
    }
    cout<<"Case #"<<x<<": ";
    if(minc==0)
    {
        for(int i=0;i<c.size();i++)
            cout<<"0";
            cout<<" ";
    }
    else
    {
    while(c1<c.size()-l1)
        cout<<"0",c1++;
    cout<<minc<<" ";
    }
    if(mins==0)
    {
        for(int i=0;i<c.size();i++)
            cout<<"0";
            cout<<"\n";
    }
    else
    {
    while(c2<s.size()-l2)
        cout<<"0",c2++;
    cout<<mins<<"\n";
    }
    }
    return 0;
}
