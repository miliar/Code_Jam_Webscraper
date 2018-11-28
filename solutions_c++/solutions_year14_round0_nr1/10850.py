#include <cstdio>
#include <iostream>
using namespace std;
int main()
{
    int t,z=0;
    cin>>t;
    while(t--)
    {
              z++;
              int a1,a2,i,c=0,j,ans;
              int a[16],b[16];
              cin>>a1;
              for(i=0;i<16;i++)
              cin>>a[i];
              cin>>a2;
              for(i=0;i<16;i++)
              cin>>b[i];
              a1--;a2--;
              for(i=0;i<4;i++)
              {
                              for(j=0;j<4;j++)
                              {
                                              //cout<<a[4*a1 + i]<<" ";
                                              //cout<<b[4*a2 + j]<<" ";
                                              //cout<<endl;
                                              if(a[4*a1 + i]==b[4*a2+j])
                                              {
                                                        c++;
                                                        ans=a[4*a1+i];
                                                        //cout<<c<<" "<<ans<<endl;
                                              }
                              }
              }
              if(c==1)
              cout<<"Case #"<<z<<": "<<ans<<endl;
              else if(c>1)
              cout<<"Case #"<<z<<": "<<"Bad magician!"<<endl;
              else
              cout<<"Case #"<<z<<": "<<"Volunteer cheated!"<<endl;
    }
    return 0;
}
