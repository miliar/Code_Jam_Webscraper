#include<iostream>
#include<string.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int c=0;
    while(t--)
    {
              c++;
              int n,ans=0,f=0;
              cin>>n;
              string s1,s2;
              cin>>s1>>s2;
              int l1=s1.length();
              int l2=s2.length();
              
              int ind1=0,ind2=0;
              while(ind1<l1 && ind2<l2)
              {
                      char c1=s1[ind1];
                      char c2=s2[ind2];
                      int cnt1=1,cnt2=1;
                      ind1++;
                      ind2++;
                      if(c1!=c2)
                      {
                                f=1;
                                break;
                      }
                      while(s1[ind1]==c1 && ind1<l1)
                      {
                                        cnt1++;
                                        ind1++;
                      }
                      while(s2[ind2]==c2 && ind2<l2)
                      {
                                        cnt2++;
                                        ind2++;
                      }
                      
                      if(cnt1>cnt2)
                      ans+=cnt1-cnt2;
                      else
                      ans+=cnt2-cnt1;
              }
              cout<<"Case #"<<c<<": ";
              if(ind1<l1 || ind2<l2)
              f=1;
              if(f==0)
              cout<<ans<<endl;
              else
              cout<<"Fegla Won"<<endl;
    }
    return 0;
}
