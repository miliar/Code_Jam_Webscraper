#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define f(i,st,en)for(int i=st;i<en;i++)
#define fi(i,st,en)for(int i=st;i<=en;i++)
typedef vector<int>vi;
ll conv(string str)
{
  stringstream ss(str);
  ll i;
  ss >> i;
  return i;
}
bool allequal(vector<pair<int,int> >v)
{
 int l=v[0].first;
  for(int i=1;i<v.size();i++)
     {
        if(l!=v[i].first)return false;
     }
     return true;
}
bool comp(pair<int,int>a,pair<int,int>b)
{
  return b.first<a.first;
}
int main()
{



    freopen("in-small3","r",stdin);
    freopen("out","w",stdout);

    int t;
    scanf("%d",&t);
     int n;
      map<int,char>m;
       char ch='A';
       f(i,0,30){m[i]=ch;ch++;}

    for(int test=1;test<=t;test++)
    {
      printf("Case #%d: ",test);
      scanf("%d",&n);
      vector<pair<int,int> >v(n);
       f(i,0,n)
         {
           cin>>v[i].first;
           v[i].second=i;
         }
       /*f(i,0,n)
       cout<<v[i].first<<" ";
       cout<<endl;*/

        int i=0;
        if(v.size()<=2)
        {
          if(v[i].first==v[i+1].first)
            {
                 while(v[i].first--)
                    {
                     cout<<"AB"<<" ";
                     v[i+1].first--;
                    }
            }
          else
            {
               if(v[i].first>v[i+1].first)
                  {
                  //cout<<"afaf"<<endl;
                     while(v[i].first!=v[i+1].first)
                        {
                         cout<<"A"<<" ";
                         v[i].first--;
                        }
                         while(v[i].first--)
                    {
                     cout<<"AB"<<" ";
                     v[i+1].first--;
                    }
                  }
                else
                   {
                   //cout<<"adfaf"<<endl;
                       while(v[i+1].first!=v[i].first)
                          {
                           cout<<"B"<<" ";
                           v[i+1].first--;
                          }
                           while(v[i].first--)
                    {
                     cout<<"AB"<<" ";
                     v[i+1].first--;
                    }
                   }
            }
            cout<<endl;
            continue;

        }


 sort(v.begin(),v.end(),comp);
           while(v[i].first>0)
             {

                if(allequal(v))
                  {
                    cout<<m[v[i].second];
                    v[i].first--;
                    //cout<<"11111"<<endl;
                  }
                else if(v.size()>=2)
                  {

                    if(v[i].first>v[i+1].first)
                    {
                        if(v[i].first==v[i+1].first+1)
                        {
                           cout<<m[v[i].second];
                           v[i].first--;
                        }
                        else
                          {
                            cout<<m[v[i].second]<<m[v[i].second];
                            v[i].first-=2;
                          }
                    }
                    else
                      {
                        cout<<m[v[i].second]<<m[v[i+1].second];
                        v[i].first--;
                        v[i+1].first--;
                      }
                     /*cout<<m[v[i].second]<<m[v[i+1].second];
                     v[i].first--;
                     v[i].second--;*/
                     //cout<<"2222"<<endl;
                  }
                  else
                    {
                       char h=m[v[i].second];
                         while(v[0].first)
                            {
                             int c=0;
                             while(v[i].first--)
                                {
                                 if(c==2)break;
                                 cout<<h;
                                 c++;
                                }
                                //cout<<"33333"<<endl;
                                cout<<" ";
                            }

                    }
                  cout<<" ";
                  sort(v.begin(),v.end(),comp);
             }
         cout<<endl;
    }
    return 0;
}
