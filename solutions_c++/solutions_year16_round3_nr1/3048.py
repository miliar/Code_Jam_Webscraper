#include <cmath>
#include <cstdio>
#include <map>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <numeric>
using namespace std;
#define REP(I,N)   FOR(I,0,N)
#define pb push_back
#define LL long long
LL limit=500000;
struct mn
{
    int m;
    int p;
};
int main()
{

    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        int n;
        cin>>n;
        int arr[n];
        vector<mn>pt;
        for(int j=0; j<n; j++)
        {
            mn x;
            x.m=j;
            int xr;
            cin>>xr;
            x.p=xr;
            pt.push_back(x);
        }

        vector<string>v;
        int f=n;
        while(1)
        {
            int k=0;
            for(int j=0; j<f; j++)
                if(pt[j].p<=0)
                    k++;
            if(k==f)
                break;
            sort(begin(pt),end(pt),[](const mn &m,const mn &n)
            {
                return n.p <= m.p;
            });
            /*  for(int j=0;j<pt.size();j++)
                 cout<<pt[j].m<<" "<<pt[j].p<<endl;*/
            int a=0;
            for(int j=0; j<pt.size(); j++)
            {
                if(pt[j].p>0)
                    a++;

            }
            string s="";
            int st=0;
            for(int j=0; j<pt.size(); j++)
                st+=pt[j].p;
            if(a==2)
            {
                if(pt[0].p==pt[1].p)
                {
                    s+=('A'+pt[0].m);
                    s+=('A'+pt[1].m);
                    pt[0].p-=1;
                    pt[1].p-=1;
                }
                /*else if(abs(pt[0].p - pt[1].p) == 1 && pt[0].p > pt[1].p )
                {
                    s+=('A'+pt[0].m);
                    pt[0].p-=1;
                }
                else if(abs(pt[0].p - pt[1].p) == 1 && pt[1].p > pt[0].p )
                {
                    s+=('A'+pt[1].m);
                    pt[1].p-=1;
                }
                else if(abs(pt[0].p - pt[1].p) >= 2 && pt[1].p > pt[0].p )
                {
                    s+=('A'+pt[1].m);
                    s+=('A'+pt[1].m);
                    pt[1].p-=2;
                }
                else if(abs(pt[0].p - pt[1].p) >= 2 && pt[0].p > pt[1].p )
                {
                    s+=('A'+pt[0].m);
                    s+=('A'+pt[0].m);
                    pt[0].p-=2;
                }*/
                v.push_back(s);

            }
            else
            {

                while(pt[0].p!=pt[1].p)
                {
                    string s="";
                    if(abs(pt[0].p - pt[1].p)>=2)
                    {
                        s+=('A'+pt[0].m);
                        s+=('A'+pt[0].m);
                        pt[0].p-=2;
                    }
                    else
                    {
                        s+=('A'+pt[0].m);
                        pt[0].p-=1;
                    }
                    v.push_back(s);
                }

                while(pt[2].p!=0)
                {
                    string s="";
                    if( pt[2].p - 2>=0)
                    {
                        s+=('A'+pt[2].m);
                        s+=('A'+pt[2].m);
                        pt[2].p-=2;
                    }
                    else if(pt[2].p - 1>=0)
                    {
                        s+=('A'+pt[2].m);
                        pt[2].p-=1;
                    }
                    v.push_back(s);
                }

                /*  int j=0;
                  for(; j<pt.size(); j++)
                  {
                      if(pt[j].p!=pt[j+1].p)
                          break;
                  }
                  if(j==pt.size()-1)
                  {
                      if(pt[0].p >=2)
                      {
                          pt[0].p-=2;
                          s+=('A'+pt[0].m);
                          s+=('A'+pt[0].m);
                      }
                      else
                      {
                          pt[0].p-=1;
                          s+=('A'+pt[0].m);
                      }
                  }
                  else
                  {
                      //cout<<j<<endl;
                      if(pt[j].p - pt[j+1].p >=2)
                      {
                          pt[j].p-=2;
                          s+=('A'+pt[j].m);
                          s+=('A'+pt[j].m);
                      }
                      else
                      {
                          pt[j].p-=1;
                          s+=('A'+pt[j].m);
                      }

                  }
                  v.push_back(s);*/
            }
        }
        cout<<"Case #"<<i<<": ";
        for(int j=0; j<v.size(); j++)
            cout<<v[j]<<" ";
        cout<<endl;
    }
    return 0;

}
