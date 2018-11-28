#include <iostream>
#include <stdio.h>
using namespace std;
int ar[1009];
int main()
{
    freopen("A-large.in","rt",stdin);
    freopen("A-large.txt","w",stdout);
    int  t,n;
    cin>>t;
  for(int x=1; x<=t; x++){
        int sum=0,dif=0,s2=0;
    cin>>n;
    for(int z=0; z<n; z++)
        cin>>ar[z];
    ar[n]=ar[n-1];
     for(int z=0; z<n; z++){
        if(ar[z]>ar[z+1])sum+=ar[z]-ar[z+1];
    dif=max(dif,ar[z]-ar[z+1]);}

    for(int z=0; z<n-1; z++){
    s2+=min(ar[z],dif);
    }
    cout<<"Case #"<<x<<": "<<sum<<" "<<s2<<endl;
  }
    return 0;
}
