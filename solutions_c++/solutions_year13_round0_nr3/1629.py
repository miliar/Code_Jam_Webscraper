#include<iostream>
#include<stdio.h>

using namespace std;

int main(){
 freopen("c.in", "r", stdin);
    freopen("cc.out", "w", stdout);
    unsigned long long arr[]={1,
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
10000200001,
10221412201,
12102420121,
12345654321,
40000800004,
1000002000001,
1002003002001,
1004006004001,
1020304030201,
1022325232201,
1024348434201,
1210024200121,
1212225222121,
1214428244121,
1232346432321,
1234567654321,
4000008000004,
4004009004004};
int t;
    unsigned long long a,b,count=0;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        count=0;
        scanf("%lld",&a);
        scanf("%lld",&b);
        for(int j=0;j<39;j++){
            if(arr[j]>=a && arr[j]<=b)
                count++;
        }
        printf("Case #%d: %lld\n",i,count);
    }
    return 0;
}
