#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

long long a[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004,0};

int T;
long long A,B;

int solve(long long A,long long B){
    int i=0,ans=0;
    while (a[i]){
        if (A<=a[i]&&a[i]<=B)
            ans++;
        i++;
    }
    return ans;
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    int cas=0;
    while (T--){
        cin>>A>>B;
        printf("Case #%d: %d\n",++cas,solve(A,B));
    }
}
