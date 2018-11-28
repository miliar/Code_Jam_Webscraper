#include <bits/stdc++.h>
using namespace std;
#define MAX 1000001
int a, b, c;

int main()
{
	int n, cont=0;
	scanf("%d", &n);
	while(++cont <= n){
		vector<int> v;
		scanf("%d %d %d", &a, &b, &c);
		if(a == 1){printf("Case #%d: 1\n", cont); continue;}
		int i;
		if(b == 1) i = 1;
		else i = 2;
		for(; i<=a; i++){
			v.push_back(i);
			c--;
		}
		if(c>=0){
			printf("Case #%d:", cont);
			for(int i=0; i<v.size(); i++){
				printf(" %d", v[i]);
			}
			puts("");
		}
		else
			printf("Case #%d: IMPOSSIBLE\n", cont);
	}
    
    return 0;
}