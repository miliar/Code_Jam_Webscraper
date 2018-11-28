#include<iostream>
#include<math.h>
using namespace std;
unsigned long long FnSno[39]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004,};

unsigned long long FnS(unsigned long long &A,unsigned long long &B)
{
    unsigned long long a=0;
    for(int c=0;c<39;c++)
    {
        if(FnSno[c]>=A&&FnSno[c]<=B)a++;
    }
    return a;
}
int main()
{
    int T;
    cin>>T;
    unsigned long long A,B;
    unsigned long long n;
    for(int t=1;t<=T;t++)
    {
        cin>>A>>B;
        n=FnS(A,B);
        cout<<"Case #"<<t<<": "<<n<<endl;
    }
}
