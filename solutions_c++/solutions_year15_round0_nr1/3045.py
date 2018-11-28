#include <stdio.h>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <string>
using namespace std;


char tekst[10000];

int main() {
	int id=1;int t;scanf("%d",&t);
	while(t--) {
		scanf("%*d");
		scanf("%s",tekst);
		string dane = string(tekst);
		//printf("%s\n", dane.c_str());
		int res = 0;
		int suma = 0;
		for(int i=0;i<dane.size();i++) {
			int ile = dane[i]-'0';
			res = max(res, i-suma);
			suma+=ile;
		}
		
		printf("Case #%d: %d\n",id++,res);
	}
	return 0;
}
