#include<cstdio>
#include<set>
using namespace std;
typedef long long i64;

int R, N, M, K;
i64 V[12];

int main()
{
	scanf("%*d%d%d%d%d", &R, &N, &M, &K);

	puts("Case #1:");
	for(int i=0;i<R;i++){
		//product of N integers between 2 and M
		for(int j=0;j<K;j++) scanf("%lld", V+j);

		if(N==3){
			for(int j=2;j<=5;j++){
				for(int k=2;k<=5;k++){
					for(int l=2;l<=5;l++){
						set<int> st;
						st.clear();
						st.insert(1);
						st.insert(j);
						st.insert(k);
						st.insert(l);
						st.insert(j*k);
						st.insert(k*l);
						st.insert(l*j);
						st.insert(j*k*l);

						bool flg = true;
						for(int t=0;t<K;t++) if(st.count(V[t])==0) flg = false;

						if(flg){
							printf("%d%d%d\n", j, k, l);
							goto nex;
						}
					}
				}
			}
nex:
			continue;
		}
	}

	return 0;
}
