#include <stdio.h>
#include <string.h>

int T;
int smax;

char s[1050];

int len, ap, scum;
int diff;

void main(){

	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	scanf("%d\n", &T);
//	printf("%d\n", T);

	for (int i = 1; i <= T; i++){
		scanf("%d\n", &smax);
		scanf("%s\n", s);		
	//	printf("%d ", smax);
	//	printf("%s\n", s);
		
		len = strlen(s);
		ap = scum = 0;

		for (int j = 0; j < len; j++){			
			if (j>0){
				diff = j - scum;
				if (diff > 0){
					ap += diff;
					scum += diff;
				}
			}
			scum += s[j] - '0';
		}

		printf("Case #%d: %d\n", i, ap);

	}


}