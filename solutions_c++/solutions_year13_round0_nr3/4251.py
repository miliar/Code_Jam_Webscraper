#include<cstdio>
#include<limits.h>
#include<string>
#include<vector>
#include<iostream>
#include<cstdlib>
#include<math.h>
#include<algorithm>
using namespace std;
int main()
{
    freopen("C-large-1.in","r",stdin);
  freopen("output.txt","w",stdout);
  int t,max1,z=0;
  scanf("%d",&t);
  while(t--)
  {
            z++;
            int i;
            long long int ar[39]={1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002};
            long long int x,c=0;
            long long int a,b;
            cin>>a>>b;
            for(i=0;i<39;i++)
            {
                             x=ar[i]*ar[i];
                             if(x>=a && x<=b)
                             c++;
            }
            cout<<"Case #"<<z<<": "<<c<<endl;
  }
  return 0;
}
