#include <stdio.h>

using namespace std;

int p[26];
int t;
int tot=0;

int getLargest(){
	int m=0, mm=0;
	for(int i=0;i<t;i++){
		if(p[i] > m){
			m = p[i];
			mm = i;
		}
	}

	if(tot == 2*m){
		for(int i=0;i<t;i++){
			if(p[i] == m && i != mm){
				mm = (mm & 0xff) + i << 8;
			}
		}
	}

	return mm;
}


void cas(int tt){
	tot = 0;
	scanf("%d", &t);
	for(int i=0;i<t;i++){
		scanf("%d", p+i);
		tot += p[i];
	}

	printf("Case #%d: ", tt);

	// make largest party leave
	while(tot > 2){
		int l = getLargest();
		if(l >> 8){
			printf("%c", 'A' + (l >> 8));
			tot --;
			p[l>>8]--;
		}
			
		printf("%c ", 'A' + (l & 0xff));
		p[l&0xff] --;
		tot --;

	}

	// get the last two
	for(int i=0;i<t;i++){
		if(p[i]>0){
			printf("%c", 'A'+i);
		}
	}
	printf(" \n");
}

int main(){
	int n;
	scanf("%d", &n);

	for(int i=1;i<=n;i++){
		cas(i);
	}

	return 0;
}

