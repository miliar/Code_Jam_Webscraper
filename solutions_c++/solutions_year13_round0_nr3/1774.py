#include<cstdio>
#include<cstdlib>

long long index[] = {
0,
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
10000200001LL,
10221412201LL,
12102420121LL,
12345654321LL,
40000800004LL,
1000002000001LL,
1002003002001LL,
1004006004001LL,
1020304030201LL,
1022325232201LL,
1024348434201LL,
1210024200121LL,
1212225222121LL,
1214428244121LL,
1232346432321LL,
1234567654321LL,
4000008000004LL,
4004009004004LL
};

int main(){
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int t,_case;
    while(scanf("%d",&t) != EOF){
        for(int _case = 0; _case < t; ++_case){
            long long a,b;
            scanf("%lld%lld",&a,&b);
            int i,j;
            for(i = 0; i < 40; ++i) if(a <= index[i]) break;
            for(j = 39; j + 1; --j) if(b >= index[j]) break;
            int res = j - i + 1;
            printf("Case #%d: %d\n",_case + 1,res);
        }
    }
    return 0;
}
