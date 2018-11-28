#include<iostream>
#include<algorithm>
#include<stdlib.h>
#include<math.h>
using namespace std;

int main()
{
int t,i;
cin>>t;
for(i=1;i<=t;i++)
{
  int n,j,k,d[1005],temp,ans,val;
  cin>>n;
  for(j=0;j<n;j++)
      cin>>d[j];
    sort(d,d+n);
    ans=d[n-1];

    for(val=2;val<d[n-1];val++)
    {

        temp=val;
        for(k=n-1;k>=0 && d[k]>val;k--)
                temp+=ceil((float)d[k]/(float)val)-1;
        if(temp<ans)
            ans=temp;
    }

    cout<<"case #"<<i<<": "<<ans<<"\n" ;
}
return 0;
}
