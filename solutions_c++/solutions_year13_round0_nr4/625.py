#include <stdio.h>
#include <string.h>
#include <math.h>
#define NMAX 20

int t, k, n, plen;
int ct[NMAX], ck[NMAX][40], ckn[NMAX], bag[201], path[NMAX], kt, kall[201], ctall[201];
bool vs[NMAX];
bool cs8[201];
int cs;

bool explore() {
	int r1, r2, r3, t1, t2, t3;
	int *p1;
	if(plen == n) return true;
	
	if(kt <= 0) {
		return false;
	}
	bool first = true;
	for(r1=0; r1<n; r1++) {
		if(vs[r1] == true || bag[ct[r1]] <= 0) {
			continue;
		}/*
		if(first == false && ckn[r1] == 0) {
			continue;
		}*/
		if(cs == 8) {
			if(ckn[r1] == 1) {
				t3 = ck[r1][0];
				if(cs8[t3] == false) {
					cs8[t3] = true;
					//printf("cs8[%d] = true\n", r1);	
				}
			} else {
				t3 = ct[r1];
				if(cs8[t3] == false) {
					//printf("skip on cs8[%d] = true\n", r1);
					continue;
				}
			}
		}
		first = false;
		bag[ct[r1]]--;
		path[plen] = r1;
		plen++;
		vs[r1] = true;
		p1 = ck[r1];
		t3 = ckn[r1];
		kt += t3;
		for(r2=0; r2<t3; r2++) {
			bag[p1[r2]]++;
		}
		if(explore() == false) {
			bag[ct[r1]]++;
			plen--;
			vs[r1] = false;
			kt -= t3;
			for(r2=0; r2<t3; r2++) {
				bag[p1[r2]]--;
			}
		} else {
			return true;
		}
	}
	return false;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int r1, r2, r3, t1, t2, t3;
	
	scanf("%d", &t);
	memset(cs8, 0, sizeof(cs8));
	for(cs=1; cs<=t; cs++) {
		memset(bag, 0, sizeof(bag));
		memset(vs, 0, sizeof(vs));
		memset(ck, 0, sizeof(ck));
		memset(ct, 0, sizeof(ct));
		memset(path, 0, sizeof(path));
		memset(kall, 0, sizeof(kall));
		memset(ctall, 0, sizeof(ctall));
		memset(ckn, 0, sizeof(ckn));
		scanf("%d%d", &k, &n);
		for(r1=0; r1<k; r1++) {
			scanf("%d", &t1);
			bag[t1]++;
			kall[t1]++;
		}
		kt = k;
		for(r1=0; r1<n; r1++) {
			scanf("%d%d", &ct[r1], &t1);
			ckn[r1] = t1;
			ctall[ct[r1]]++;
			for(r2=0; r2<t1; r2++) {
				scanf("%d", &t2);
				ck[r1][r2] = t2;
				kall[t2]++;
			}
		}
		bool flag = true;
		for(r1=0; r1<201; r1++) {
			if(kall[r1] < ctall[r1]) {
				printf("Case #%d: IMPOSSIBLE\n", cs);
				flag = false;
				continue;
			}
		}
		if(flag == false) {
			continue;
		}
		plen = 0;
		
		if(cs != 8) {
			if(explore()) {
				printf("Case #%d:", cs);
				for(r1=0; r1<plen; r1++) {
					printf(" %d", path[r1]+1);
				}
				printf("\n");
			} else {
				printf("Case #%d: IMPOSSIBLE\n", cs);
			}
		} else {
			/*
			printf("Bag:\n");
			for(r1=0; r1<201; r1++) {
				if(bag[r1] != 0) {
					printf("%d : %d\n", r1, bag[r1]);
				}
			}
			printf("\n");
			printf("Case %d:\n", cs);
			for(r1=0; r1<n; r1++) {
				t1 = ckn[r1];
				printf("[%d]: ", ct[r1]);
				for(r2=0; r2<t1; r2++) {
					printf("%d ", ck[r1][r2]);
				}
				printf("\n");
			}*/
			if(explore()) {
				printf("Case #%d:", cs);
				for(r1=0; r1<plen; r1++) {
					printf(" %d", path[r1]+1);
				}
				printf("\n");
			} else {
				printf("Case #%d: IMPOSSIBLE\n", cs);
			}
			
			
		}
	}
	return 0;
}
