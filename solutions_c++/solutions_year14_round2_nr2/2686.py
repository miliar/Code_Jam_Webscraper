#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
   int t,T;
   scanf("%d",&T);
   for(t=1;t<=T;t++)
   {
        int a,b,k;
        cin>>a>>b>>k;
        int i,j,ans=0;

        for(i=0;i<a;i++)
            for(j=0;j<b;j++)
                {

                    if((i&j)<k)
                        {
                  //          cout<<i<<" "<<j<<" "<<(i&j)<<endl;
                            ans++;
                        }
                }
        cout<<"Case #"<<t<<": "<<ans<<endl;
   }

return 0;
}
