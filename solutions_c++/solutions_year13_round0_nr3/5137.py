#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
#define MAX     100003

long long pow10[103];

int get(long long n){
    int res=0;
    while(n){
        ++res;
        n/=10;
    }
    return res;
}

int fit(long long n){
    int t=get(n)-1;
    while(t && n){
        if(n%10!=n/pow10[t])
            return 0;
        n-=n%10*pow10[t];
        n/=10;
        t-=2;
    }
    return 1;
}

long long array[1003]={
1LL,
4LL,
9LL,
121LL,
484LL,
10201LL,
12321LL,
14641LL,
40804LL,
44944LL,
1002001LL,
1234321LL,
4008004LL,
100020001LL,
102030201LL,
104060401LL,
121242121LL,
123454321LL,
125686521LL,
400080004LL,
404090404LL,
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
4004009004004LL,
100000020000001LL
};

int cnt;

int main(){
	pow10[0]=1;
    for(int i=1;i<103;++i)
        pow10[i]=pow10[i-1]*10;
	cnt=40;
	freopen("c:\\C-large-1.in","r",stdin);
	freopen("c:\\C_large.out","w",stdout);
	int T;
	long long N,M;
	long long * beg,* end;
	cin>>T;
	for(int t=0;t<T;++t){
		cin>>N>>M;
		beg=lower_bound(array,array+cnt,N);
		end=upper_bound(array,array+cnt,M);
		cout<<"Case #"<<t+1<<": "<<end-beg<<endl;
    }
    return 0;
}
