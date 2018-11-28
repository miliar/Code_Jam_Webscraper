#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstdio>
 
#define FOR(k,x,n) for(long long k=x;k<n;k++)
#define SORT(x) sort(x.begin(),x.end())
 
using namespace std;
bool checkpal(long long peep){
    long long answer=peep;
    long long result=1;
    result=1;
    while(answer>0){
        result+=answer%10;
        answer/=10;
        if(answer>0)
        result*=10;
    } 
    if(result==peep)
        return true;
    return false;
}
int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
 
    long long Test,count=1;
    cin>>Test;
    long long sqpal[]={
    1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,
    404090404,10000200001LL,10221412201LL,12102420121LL,12345654321LL,40000800004LL,1000002000001LL,1002003002001LL,1004006004001LL,1020304030201LL,
    1022325232201LL,1024348434201LL,1210024200121LL,1212225222121LL,1214428244121LL,1232346432321LL,1234567654321LL,4000008000004LL,4004009004004LL
    };
 
    for(long long i=0;i<Test;i++){
        long long x,y,z=0;
        cin>>x>>y;
        for(long long k=0;k<39;k++){
        if( sqpal[k] >=x && sqpal[k] <=y  ){
            z++;
        }
    }
    cout<<"Case #"<<count<<": "<<z<<endl;
    count++;
    }
    return 0;
}
 

