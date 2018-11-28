#include <fstream>
#include <fstream>
#include <math.h>
#include <string>
#include <algorithm>
#define long long long
using namespace std;
ifstream cin("C-small-attempt0.in");
ofstream cout("output.txt");
long p[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};

int main()
{
  /*  for (long i=0;i<45;i++){

    cout<<(long)
    sqrt(p[i])<<endl;
    long h;
    cin>>h;
    if (h==1)
    out<<p[i]<<",";
    }
*/
    long a,b,t;
    cin>>t;
    for (long i=0;i<t;i++){
    cin>>a>>b;
    cout<<"Case #"<<i+1<<": ";
    long ans=upper_bound(p,p+55,b)-lower_bound(p,p+55,a);
    cout<<ans<<endl;
    }
    return 0;
}
