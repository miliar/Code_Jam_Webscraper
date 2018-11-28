#include <cstdio>
#include <utility>
using namespace std;

int main(){
	int cases;
	scanf("%d", &cases);
	for(int caseno=1;caseno<=cases;++caseno){
		int ans=0, A, B, K;
		scanf("%d%d%d", &A, &B, &K);
		for(int i=0;i<A;++i)
			for(int j=0;j<B;++j)
				if((i&j)<K)
					++ans;
		printf("Case #%d: %d\n", caseno, ans);
	}
}
