#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 101
#define TOL 0.000001


#define max(a,b) ((a) >= (b) ? (a) : (b))
#define min(a,b) ((a) <= (b) ? (a) : (b))

using namespace std;

char mat[N][N];



int main () {

	int t, tst, z, i, j, p, m, n, r, l, l2, c, rez, rcmin, x, y, d, k, sum;
	char s[N], s2[N];
	int v[N][N], av[N];
	
	scanf("%d", &tst);


	for (t = 0; t < tst; t++) {
		scanf("%d", &n);
		rez = 1;
		memset(s2, 0, sizeof(s2));
		memset(v, 0, sizeof(v));
		memset(av, 0, sizeof(av));
		
		scanf("%s", s);
		l = strlen(s);
		m = 1;
		j = i = 0;
		s2[m-1] = s[j];
		v[i][m-1]++;
		for (j = 1; j<l; j++) {
			if (s[j] == s2[m-1]) {
				v[i][m-1]++;
			}
			else {
				m++;
				s2[m-1] = s[j];
				v[i][m-1]++;
			
			}
		}
		l2 = strlen(s2);
		
		for (i = 1; i<n; i++){
			scanf("%s", s);
			if (rez) {
				l = strlen(s);
				m = 1;
				if (s[0] != s2[0])
					rez = 0;
				for (j = 0; j<l && rez; j++) {
					if (s[j] == s2[m-1]) {
						v[i][m-1]++;
					}
					else {
						m++;
						if (s2[m-1] == s[j])
							v[i][m-1]++;
						else 
							rez = 0;
			
					}
				}
				
				if (m != l2)
					rez = 0;
			}
					
		}
		
		printf("Case #%d: ",t+1);
		
		if (rez) {
			//printf("\n%s\n", s2);
			for (j = 0; j<l2; j++) {
				for (i = 0; i<n; i++)
					av[j] += v[i][j];
				av[j] = (int) round((double)av[j]/(double)n);
				
				//printf("%d\n", av[j]);
			}
			
			sum = 0;
			for (j = 0; j<l2; j++) 
				for (i = 0; i<n; i++)
					sum+= abs(v[i][j] - av[j]);
				
			printf("%d\n", sum);	
		}
		
		else
			printf ("Fegla Won\n");
		
		}
		
	
	return 0;

}
