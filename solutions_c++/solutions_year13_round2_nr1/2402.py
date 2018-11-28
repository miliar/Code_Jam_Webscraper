#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
int i,j,k,n,t,s,x,ans=0,in=0;
ofstream fo;
ifstream fi;
fi.open("in.txt");
fo.open("out.txt");
fi>>t;
while(t--)
{
          fi>>x>>n;
          in++;
          vector<int> y;
          ans=0;
          for(i=0;i<n;i++)
          {
                          fi>>j;
                          y.push_back(j);
          }
          sort(y.begin(),y.end());
          s=x;
          j=0;
          while(1)
          {
                  if(j>=n)
                  break;
                 if(y[j]<s) 
                 s+=y[j++];
                 else if(y[j]>=s)
                 {
                      k=0;
                      if(s==1)
                      {ans+=(n-j);
                      break;}
                      while(s<=y[j])
                      {
                                   s+=(s-1);
                                   k++;
                      }
                      if((n-j)>k)
                      {
                                 ans+=k;
                                 s+=y[j++];
                      }
                      else
                      {
                          ans+=(n-j);
                          break;
                      }
                 }
          }
          fo<<"Case #"<<in<<": ";
          fo<<ans<<"\n";
}
fi.close();
fo.close();
}         
