#include <cstdio>
#include <iostream>
using namespace std;


long long data[]={0ll,1ll,4ll,9ll,121ll,484ll,
10201ll,12321ll,14641ll,40804ll,44944ll,1002001ll,
1234321ll,4008004ll,  100020001ll,102030201ll,104060401ll,
121242121ll,123454321ll,125686521ll,400080004ll,404090404ll,
10000200001ll,10221412201ll,12102420121ll,12345654321ll,
40000800004ll,1000002000001ll,1002003002001ll,
1004006004001ll,1020304030201ll,  1022325232201ll,
1024348434201ll,1210024200121ll,1212225222121ll,1214428244121ll,
1232346432321ll,1234567654321ll,4000008000004ll,4004009004004ll,
100000020000001ll,100220141022001ll,102012040210201ll,102234363432201ll,
121000242000121ll,121242363242121ll,123212464212321ll,123456787654321ll};
int main()
{
    freopen("C-large-1.in", "r", stdin);
    freopen("hh.out", "w", stdout);
    int cas; scanf("%d", &cas);
    for (int I=1; I<=cas; ++I){
        long long a, b; //scanf("%lld%lld", &a, &b);
        cin >> a >> b;
        int l=-1, r=-1;
        for (int i=0; i<48; ++i)
        {
            if(data[i]<a)l=i+1;
            if(r==-1)if(data[i]>b)r=i;
        }
        printf("Case #%d: ", I);
        cout << r - l << endl;
    }
    return 0;
}
