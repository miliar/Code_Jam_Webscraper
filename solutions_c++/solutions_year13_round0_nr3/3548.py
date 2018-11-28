#include <cstdio>
#include <cmath>
#include <cctype>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <stack>
#include <cstring>
#include <cstdlib>
#include <queue>
#include <map>
using namespace std;
typedef long long ll;
int main()
{
          //SMALL
          freopen("GCJ133.in","r",stdin);
          freopen("GCJ133.out","w",stdout);
          long T,i,j,bp,ok[2001],c,len,d;
          ll A,B;
          char a[50],b[50];
          cin>>T;
          for (i=1; i<=2000; i++) ok[i]=0;
          for (c=1; c<=T; c++)
          {
                    cin>>A>>B;
                    d=0;
                    for (i=1; i<40; i++)
                    {
                              itoa(i,a,10);
                              len=strlen(a);
                              ok[i*i]=1;
                              for (j=1; j<=len/2; j++)
                              {
                                        if (a[j-1]!= a[len-j]) {ok[i*i]=0; break;}
                              }
                              bp=i*i;
                              itoa(bp,a,10);
                              len=strlen(a);
                              //cout<<bp<<"  "<<"len="<<len<<endl;
                              for (j=1; j<=len/2; j++)
                              {
                                        if (a[j-1]!= a[len-j]) {ok[i*i]=0; break;}
                              }
                    }
                    //cout<<ok[25]<<endl;
                    cout<<"Case #"<<c<<": ";
                    for (i=A; i<=B; i++)
                    {
                              if (ok[i]==1) {d++;}
                    }
                    cout<<d<<endl;
          }
          //system("pause");
          return 0;
}
          
