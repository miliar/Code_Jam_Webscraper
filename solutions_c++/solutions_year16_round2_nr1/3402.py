#include <stdio.h>
#include <string.h>
int N;
int alarr[50];
#define MAXSLEN 2008
char str[MAXSLEN];
/*
;  

THREE  

FIVE 

SEVEN

NINE

int alarr[50];
*/
int ans[10];
#define P0 ( (alarr['Z'-'A'] >0 && alarr['E'-'A'] >0 && alarr['R'-'A'] >0 && alarr['O'-'A'] >0 ) )
#define D0 alarr['Z'-'A']--; alarr['E'-'A']--; alarr['R'-'A']--; alarr['O'-'A']--; 

#define P1 ( (alarr['O'-'A']>0 && alarr['N'-'A'] >0 && alarr['E'-'A']>0  ) )
#define D1 alarr['O'-'A']--; alarr['N'-'A']--; alarr['E'-'A']--; 

#define P2 ( (alarr['T'-'A'] >0 && alarr['W'-'A'] >0 && alarr['O'-'A'] >0  ) )
#define D2 alarr['T'-'A']--; alarr['W'-'A']--; alarr['O'-'A']--;

#define P3 ( (alarr['T'-'A'] >0 && alarr['H'-'A'] >0 && alarr['R'-'A'] >0 && alarr['E'-'A'] >=2 ) )
#define D3 alarr['T'-'A']--; alarr['H'-'A']--; alarr['R'-'A']--; alarr['E'-'A']-=2;

#define P4 ( (alarr['F'-'A'] >0 && alarr['O'-'A'] >0 && alarr['U'-'A'] >0 && alarr['R'-'A'] >0 ) )
#define D4  alarr['F'-'A']--; alarr['O'-'A']--; alarr['U'-'A']--; alarr['R'-'A']--;

#define P5 ( (alarr['F'-'A'] >0 && alarr['I'-'A'] >0 && alarr['V'-'A'] >0 && alarr['E'-'A'] >0 ) )
#define D5 alarr['F'-'A']--; alarr['I'-'A']--; alarr['V'-'A']--; alarr['E'-'A']--; 

#define P6 ( (alarr['S'-'A'] >0 && alarr['I'-'A'] >0 && alarr['X'-'A'] >0  ) )
#define D6 alarr['S'-'A']--; alarr['I'-'A']--; alarr['X'-'A']--;

#define P7 ( (alarr['S'-'A'] >0 && alarr['E'-'A'] >=2 && alarr['V'-'A'] >0 && alarr['N'-'A'] >0 ) )
#define D7 alarr['S'-'A']--; alarr['E'-'A']-=2; alarr['V'-'A']--; alarr['N'-'A']--;

#define P8 ( (alarr['E'-'A'] >0 && alarr['I'-'A'] >0 && alarr['G'-'A'] >0 && alarr['H'-'A'] >0 && alarr['T'-'A'] >0  ) )
#define D8 alarr['E'-'A']--; alarr['I'-'A']--; alarr['G'-'A']--; alarr['H'-'A']--; alarr['T'-'A']--; 

#define P9 ( (alarr['N'-'A'] >=2 && alarr['I'-'A'] >0 && alarr['E'-'A'] >0 ) )
#define D9 alarr['N'-'A']-=2; alarr['I'-'A']--; alarr['E'-'A']--; 

int main() {
	int T; 
	//

	scanf("%d", &T);
	for (int ti = 1; ti <= T; ti++) {
		memset(alarr,0,sizeof(alarr));
		memset(ans, 0, sizeof(ans));
	
		memset(str, 0, sizeof(str));

		scanf("%s\n", str);
	
		int i;
		for (i = 0; str[i]; i++) {
			alarr[str[i] - 'A']++;
		}
	
		while (P0) { D0 ans[0]++;}
		while (P2) { D2 ans[2]++;}
		while (P4) { D4 ans[4]++;}
		while (P6) { D6 ans[6]++;}
		while (P8) { D8 ans[8]++;}

		while (P1) { D1 ans[1]++; }
		while (P3) { D3 ans[3]++; }
		while (P5) { D5 ans[5]++; }
		while (P7) { D7 ans[7]++; }
		while (P9) { D9 ans[9]++; }



		printf("Case #%d: ", ti);

		for (int i = 0; i <= 9; i++) {
			for (int j = 0; j < ans[i]; j++) {
				printf("%d", i);
			}
		}
		printf("\n");
	}
	return 0;
}