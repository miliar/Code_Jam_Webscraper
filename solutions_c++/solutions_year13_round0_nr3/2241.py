#include<iostream>
using namespace std;

 
 
using namespace std;
bool ispal(long long x);
 
int main()
{
    ios_base::sync_with_stdio(false);
 
    freopen("C.txt", "r", stdin);
    freopen("Cans.txt", "w", stdout);
 
    long long T,cases=1;
    cin>>T;
    long long sq[]={
    1,
    4,
    9,
    121,
    484,
    10201,
    12321,
    14641,
    40804,
    44944,
    1002001,
    1234321,
    4008004,
    100020001,
    102030201,
    104060401,
    121242121,
    123454321,
    125686521,
    400080004,
    404090404,
    10000200001llu,
    10221412201llu,
    12102420121llu,
    12345654321llu,
    40000800004llu,
    1000002000001llu,
    1002003002001llu,
    1004006004001llu,
    1020304030201llu,
    1022325232201llu,
    1024348434201llu,
    1210024200121llu,
    1212225222121llu,
    1214428244121llu,
    1232346432321llu,
    1234567654321llu,
    4000008000004llu,
    4004009004004llu
    };
 
    for(long long h=0;h<T;h++){
 
    long long a,b,c=0;
    cin>>a>>b;
 
 
    for(long long k=0;k<39;k++){
 
    if( sq[k] >=a && sq[k] <=b  ){
  
    c++;
    }
 
    }
    cout<<"Case #"<<cases<<": "<<c<<endl;
    cases++;
    }
 
    return 0;
}
 

 

 
