#include "bits/stdc++.h"

using namespace std;

int score(char a, char b){
	if (a!=b) return 1;
	return 0;
}

int main()
{
	int T,N,c,cnt, ind1,ind2;
	char a[101],b[101];
	scanf("%d", &T);
	bool flag;
	c = 1;
	while(T--){
		ind1 = ind2 = cnt = 0;
		flag = false;
		scanf("%d",&N);
		scanf("%s\n%s", a,b);
		while(a[ind1] != '\0' && b[ind2] != '\0'){
			if(a[ind1] == b[ind2]){
				if (a[ind1+1] == b[ind2+1]){
					ind1++; ind2++; continue;
				}
				while(a[ind1+1] == b[ind2]){ cnt++;ind1++;}
				while(b[ind2+1] == a[ind1]){ cnt++;ind2++;}
				ind1++; ind2++;
			}
			else {
				flag = true;
				break;
			}
		}
		if (a[ind1] != b[ind2]) flag = true;
		printf("Case #%d: ", c++);
		if (flag) printf("Fegla Won\n");
		else printf("%d\n", cnt);
	}
	return 0;
}