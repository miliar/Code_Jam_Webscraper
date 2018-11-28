#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<stack>
#include<cmath>
#include<map>
using namespace std;
typedef pair<int,int> PI;
typedef long long LL;
typedef double D;
#define FI first
#define SE second
#define MP make_pair
#define PB push_back
#define R(I,N) for(int I=0;I<N;I++)
#define F(I,A,B) for(int I=A;I<B;I++)
#define FD(I,N) for(int I=N-1;I>=0;I--)
#define make(A) scanf("%d",&A)
#define MAX 101
int n;
char z[MAX];
vector<char> sk;
vector<int> d[MAX];
void test(){
	static int test_nr = 0;test_nr++;
	printf("Case #%d: ",test_nr);
	make(n);
	bool xxx=0;
	sk.clear();
	R(i,n){
		scanf(" %s",z);
		int il = 1;
		char os = z[0];
		int j = 1,kt=0;
		while(z[j-1]){
			if(z[j] == os){
				il++;
			}else{
				if(i == 0){
					d[kt].clear();
					sk.PB(os);
				}else
					if(sk[kt]!=os)xxx=1;
				d[kt].PB(il);
				il = 1;
				os = z[j];
				kt++;
			}
			j++;
		}
		if(kt!=sk.size())
			xxx=1;
	}
	if(xxx){
		printf("Fegla Won\n");
		return;
	}
	int wyn = 0;
	R(i,sk.size()){
		sort(d[i].begin(),d[i].end());
		R(j,d[i].size()){
			wyn += abs(d[i][n/2] - d[i][j]);
		}
	}
	printf("%d\n",wyn);
}
main(){
	int _;make(_);while(_--)test();
}
