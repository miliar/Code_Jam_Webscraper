#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>
#include <string.h>
#include <map>
#include <algorithm>    // std::sort

const int N = 20002;

using namespace std;

char s[N];

int main() {
	
	vector <pair<int, int> > v;
	int n, i, j, k, np, mij;
	char c1, c2;
	
	//string s1, s2;
	int tst;
	scanf("%d", &tst);

	//printf ("%c %c %c %c\n", sv[0][3], sv[3][2], sv[5][2], sv[8][4]);//o e v t
	for (int t = 0; t < tst; t++) {
		
		scanf("%d", &n);
		v.clear();
		v.resize(n);
		np = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d", &k);
			v[i].first = k;
			v[i].second = i;
			np += k;
		}	
		
		printf("Case #%d: ", t+1);
		
		while (np) {
			//printf("\nnp %d\n", np);
			c2 = -1;			
			mij = np/2;
			sort(v.begin(), v.end());
			c1 = v[n-1].second;
			v[n-1].first--;
			np--;

			sort(v.begin(), v.end());
			mij = np/2;
			k = v[n-1].first;
			if (k > mij) {
				c2 = v[n-1].second;
				v[n-1].first--;
				np--;			
			}
			
			printf("%c", c1+'A');
			if (c2 >= 0)
				printf("%c", c2+'A');
			printf(" ");			
			//printf("\nnp %d\n", np);				
		}
		printf("\n");	
	}
	
	return 0;
}
