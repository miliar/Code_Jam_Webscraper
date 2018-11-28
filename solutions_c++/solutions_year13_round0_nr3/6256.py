#include<iostream>
#include<map>
#include<math.h>
#include<stdlib.h>
using namespace std;
int pal(int x)
{
    int t=x,r=0,n;
    while(t!=0)
    {
               n=t%10;
               t=t/10;
               r=10*r+n;
    }
               if(r==x) return 1;
               else return 0;
}
int main()
{map<int,int>x;
         //for(int i=1;i<=10000;i++) x[i]=0;
         //int a1[100]={1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400,441,484,529,576,625,676,729,784,841,900,961,1024,1089,1156,1225,1296,1369,1444,1521,1600,1681,1764,1849,1936,2025,2116,2209,2304,2401,2500,2601,2704,2809,2916,3025,3136,3249,3364,3481,3600,3721,3844,3969,4096,4225,4356,4489,4624,4761,4900,5041,5184,5329,5476,5625,5776,5929,6084,6241,6400,6561,6724,6889,7056,7225,7396,7569,7744,7921,8100,8281,8464,8649,8836,9025,9216,9409,9604,9801,10000};
         //for(int i=0;i<100;i++)
        // x[a1[i]]=i+1;
        freopen("input2.txt","r",stdin);
         freopen("output1.txt","w",stdout);
         int t;
        cin>>t;
        for(int l=1;l<=t;l++)
        {unsigned long long a,b;
        cin>>a>>b;
         int c=0;
        for(int i=a;i<=b;i++)
        {if(sqrt(i)==(int)(sqrt(i)))
                {if(pal(i)==1&&pal((int)sqrt(i))==1)
                            c++;}
        }
        cout<<"Case #"<<l<<": "<<c<<endl;
        }
return 0;
}
