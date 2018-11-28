#include <bits/stdc++.h>
using namespace std;

#define mp(x, y) make_pair((x), (y))

typedef long long ll;

const char st[10][42]={
"ZERO", "WTO", "UFOR", "XSI", "GEIHT", "ONE", "FIVE", "HTREE", "SEVEN", "INNE"
};
const int m[10]={0, 2, 4, 6, 8, 1, 5, 3, 7, 9};

int q;
char s[2005];
int oc[555];
int n[42];

int main()
{
	scanf("%d\n", &q);
	for(int x=1; x<=q; x++) {
		scanf("%s\n", s);
		for(int i='A'; i<='Z'; i++) oc[i]=0;
		for(int i=0; i<=9; i++) n[i]=0;
		for(int i=0; s[i]; i++) {
			oc[s[i]]++;
		}
		for(int i=0; i<=9; i++) {
			n[m[i]]=oc[st[i][0]];
			oc[st[i][0]]=0;
			for(int j=1; st[i][j]; j++) oc[st[i][j]]-=n[m[i]];
		}
		printf("Case #%d: ", x);
		for(int i=0; i<=9; i++) for(int j=0; j<n[i]; j++) printf("%c", '0'+i);
		printf("\n");
	}

	return 0;
}
