#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;
typedef long long LL;
int a[35],sum;
LL s[15];
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("o.out","w",stdout);
	int T,kase=0;
	cin>>T;
//	cout<<T<<endl;
	for (int cas=1;cas<=T;cas++){
		int N,J;
		scanf("%d%d",&N,&J);
		printf("Case #%d:\n",cas);
		for (LL i=0;i<1<<(N-2);i++){
			LL k=i|(1<<(N-2));
		    k = (k<<1)|1;
//		    cout<<k<<endl;
		    for (int t=0;t<N;t++){
				a[t]=k&1;
				k>>=1;
		    }
//			cout<<endl;
			memset(s,0,sizeof(s));
			sum=0;
		    for (int t=2;t<=10;t++){
				LL res=0;
				for (int q=N-1;q>=0;q--)
				    res=res*t+a[q];
				LL d=sqrt(res);
//				cout<<res<<endl;
				for (LL q=3;q<=d;q++){
					if (!(res%q)){
						sum++;
						s[t]=q;
						break;
					}
				}
		    }
		    if (sum==9){
				for (int t=N-1;t>=0;t--)
					cout<<a[t];
				for (int i=2;i<=10;i++)
					printf(" %I64d",s[i]);
		    }
		    else
				continue;
			printf("\n");
			kase++;
//			cout<<kase<<endl;
			if (kase==J) break;
		}
	}
    return 0;
}
