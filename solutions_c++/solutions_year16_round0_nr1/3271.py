#include <stdio.h>
#include <set>

using namespace std;

#define MAXSTEP 100

int main(){
	int t;
	scanf("%d",&t);
	for (int tc = 1; tc <= t; tc++){
		int n;
		scanf("%d",&n);
		set<int>S;
		int step = 1;
		int result = 0;
		while (step <= MAXSTEP){
			int m = n*step;
			while (m > 0){
				S.insert(m%10);
				m/=10;
			}
			if (S.size() == 10) break;
			result++;
			step++;
		}
		if (result < MAXSTEP){
			printf("Case #%d: %d\n",tc,n*step);
		}
		else{
			printf("Case #%d: INSOMNIA\n",tc);
		}
		
	}
}