#include <iostream>
#include<algorithm>
using namespace std;

int main() {
    int t;
    cin>>t;
    for(int j=1;j<=t;j++)
     {
        int d;
        cin>>d;
        int a[10005]={0},m=0,ans=100005;
        for(int i=0;i<d;i++)
          {
            cin>>a[i];
            if(a[i]>m)
             m=a[i];
          }
        for(int i=1;i<=m;i++)
          {
            int brk=0,eat=0;
            for(int k=0;k<d;k++)
             {
                if(a[k]>i)
                 {
                    brk+=(a[k]/i)-1;
                    if(a[k]%i!=0)
                      brk++;
                 }
             }
            ans=min(ans,i+brk);
          }
          ans=min(ans,m);
          cout<<"Case #"<<j<<": "<<ans<<"\n";
     }

}
