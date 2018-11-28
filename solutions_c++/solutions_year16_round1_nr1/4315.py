#include <iostream>
#include<string.h>
#include<stdlib.h>


using namespace std;

int main()
{
    char c[1000],a[3000];
    int t,s=1500, e=1500,l,i,p;
    cin>>t;p=t;
    while(t--)
    {
      cin>>c;
      l=strlen(c);
      s=1500;e=1500;
      a[s]=c[0];
      for(i=1;i<l;i++)
      {
        if(c[i]>=a[s])
        {
            a[--s]=c[i];
        }
        else
        {
            a[++e]=c[i];
        }
      }
      cout<<"Case #"<<p-t<<": ";
      for(i=s;i<=e;i++)
        cout<<a[i];
      cout<<endl;
    }
    return 0;
}
