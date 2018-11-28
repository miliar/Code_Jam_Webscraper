#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <cmath>
using namespace std;
typedef long long LL;
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("o.out","w",stdout);
    int T,kase=1;
    cin>>T;
    while (T--){
		int K,C,S;
		scanf("%d%d%d",&K,&C,&S);
		printf("Case #%d:",kase++);
		LL cnt=1;
		for (int i=1;i<=C;i++) cnt=cnt*K;
		LL step=cnt/K;
//		cout<<"!"<<step<<endl;
		for (LL i=1;i<=cnt;i+=step)
			printf(" %I64d",i);
		printf("\n");
    }
    return 0;
}
