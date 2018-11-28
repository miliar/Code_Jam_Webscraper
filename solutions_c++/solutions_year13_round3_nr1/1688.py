#include<iostream>
#include<algorithm>
using namespace std;
int a[1000002];
int main()
{
       long long int t,i,j,l,n,pos,f=0,c,count=0;
       string s;
       freopen("input.in","r",stdin);
       freopen("output.in","w",stdout);
       cin>>t;
       for(int k=1;k<=t;k++)
       {
              count=0;
              cin>>s>>n;
              int l=s.length();
              for(i=0;i<l;i++)
              {
                            j=i;
                            f=0;
                            c=0;
                            while(j<l)
                            {
                                  if(s[j]=='a' || s[j]=='e' || s[j]=='i' || s[j]=='o' ||s[j]=='u' )
                                   c=0;
                                   else 
                                   c++;
                                   if(c==n)
                                   {
                                          f=1;
                                          pos=j;
                                        //  cout<<"pos "<<pos<<c<<endl;
                                          c=0;
                                          break;
                                   }
                                   j++;
                            }
                            if(f==1)
                            {
                                   count+=l-pos;
                            }
              }
              cout<<"Case #"<<k<<": "<<count<<endl;
                            
       }
        //system("pause");
        return 0;
}      
