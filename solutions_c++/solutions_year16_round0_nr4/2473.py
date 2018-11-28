#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[]){
	freopen("C:\\Users\\Paramdeep Singh\\Desktop\\D-small-attempt0.in","r",stdin);
	freopen("C:\\Users\\Paramdeep Singh\\Desktop\\output.txt","w",stdout);
	int cases;
	scanf("%d", &cases);

	for(int c=1; c<=cases; c++) {
		int k, cc, s;
		cin >> k >> cc >> s;
		printf("Case #%d: ", c);
		for(int i=1; i<=k; i++) {
			printf("%d ", i);
		}
		printf("\n");
	}
	return 0;
}