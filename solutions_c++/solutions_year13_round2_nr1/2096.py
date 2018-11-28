#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int A;
int N;
int tab[100];
bool done;
int R;

void fun(int tempA, int idx, int result) {
	//cout << tempA << "  " << idx << "  " << result << endl;
	if (idx == N) {
		R = min(R,result);
		return;
	}
	else if (tempA > tab[idx]) {
		fun(tempA+tab[idx],1+idx,result);
	}
	else {
		if (tempA > 1)
			fun(tempA*2-1,idx,result+1);
		fun(tempA,idx+1,result+1);
	}
}

int main() {
	int T;
	scanf("%d",&T);
	for (int j=1;j<=T;++j) {
		R = 100*100;
		scanf("%d %d",&A,&N);
		for (int i=0;i<N;++i)
			scanf("%d",&tab[i]);
		sort(tab,tab+N);
		fun(A,0,0);
		printf("Case #%d: %d\n",j,R);
	}
	return 0;
}
