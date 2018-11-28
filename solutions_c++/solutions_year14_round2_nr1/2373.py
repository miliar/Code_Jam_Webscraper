#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
using namespace std;
#define MOD 10000007
int main()
{
       int t,n,i,l;
       cin>>t;
       for(int ans=1;ans<=t;ans++)
       {
               cin>>n;
               string s1,s2;
              cin>>s1>>s2;
               int l1=s1.size();
               int l2=s2.size();
               int count=0,j=0;
               i=0;
               bool flag=true;
               while(i<l1&&j<l2&&flag)
               {
                       if(s1[i] != s2[j])
                       {
                               if(i>0 && s1[i-1]==s1[i])
                               {
                                       while(i<l1 && s1[i-1] == s1[i])
                                       {
                                               i++;
                                               count++;
                                       }
                               }
                               else if(s2[j-1] == s2[j])
                               {
                                       while(j<l2 && s2[j-1] == s2[j])
                                       {
                                               j++;
                                               count++;
                                       }
                               }

                               if(s1[i]!=s2[j])
                                       flag=false;
                       }
                       i++;j++;
                       if(i==l1&&flag)
                       {
                               while(j<l2 && s1[i-1]==s2[j])
                               {
                                       j++;
                                       count++;
                               }
                               if(j!=l2)
                                       flag=false;
                       }
                       else if(j==l2&&flag)
                       {
                               while(i<l1 && s1[i]==s2[j-1])
                               {
                                       i++;
                                       count++;
                               }
                               if(i!=l1)
                                       flag=false;
                       }
               }
               if(flag)
                       printf("Case #%d: %d\n",ans,count);
               else
                       printf("Case #%d: Fegla Won\n",ans);
       }
       return 0;
}
