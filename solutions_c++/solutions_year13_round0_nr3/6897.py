#include<iostream>
#include<cmath>
#include<fstream>
bool palindrome(int);
using namespace std;
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
    freopen("shoutput.txt","w",stdout);
    unsigned long long int t,n,m,i,x,count=0,tcase=1;
    long double root;
    bool result;
    cin>>t;
    while(t--)
    {
              count=0;
    cin>>n>>m;
    for(i=n;i<=m;i++)
    {
                result=palindrome(i);
                if(result==true)
                {
                          root=sqrt(i);
                          if(floor(root)==root)
                          {
                                              x=int(root);
                                              result=palindrome(x);
                                             
                                              if(result==true)
                                              {
                            
                                                         count++;
                                              }
                          }
                }
     }
     cout<<"Case #"<<tcase<<": "<<count<<"\n";
     tcase++;
     }
     return 0;
}
bool palindrome(int i)
{
				int rev=0,q,r;
                q=i;
                while(q>0)
                {
                          r=q%10;
                          rev=rev*10+r;
                          q=q/10;
                }	
                if(rev==i)
                return true;
                else 
				return false;
}
                 
