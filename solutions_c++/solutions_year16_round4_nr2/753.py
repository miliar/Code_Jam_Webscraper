#include <stdio.h>

double chance[18];
int N, K;
double cha;
double best;

void Doagain(int bit1, int bit2){
	//printf("bit %d %d\n", bit1, bit2);
	int tbit = bit2;
	int ct=0;
	
	while(tbit){
		if(tbit & 1) ct++;
		tbit >>= 1;
	}
	
	if(ct != K/2) return;
	
	double now = 1;
	
	ct=0;
	while(bit1){
		if(bit1 & 1){
			//use this person
			if(bit2 & 1){ //yes
				now *= chance[ct];
			}else{ //no
				now *= (1-chance[ct]);
			}
			bit2 >>= 1;
		}
		ct++;
		bit1 >>= 1;
	}
	
	cha += now;
	//printf("now = %lf\n", now);
}

void Dowork(int bit){
	int tbit = bit;
	int ct=0;
	
	while(tbit){
		if(tbit & 1) ct++;
		tbit >>= 1;
	}
	
	if(ct != K) return;
	
	cha = 0;
	for(int i=0; i<(1<<K); i++){
		Doagain(bit, i);
	}
	
	if(cha > best) best = cha;
}

int main(){
	int jcase;
	
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	
	scanf("%d", &jcase);
	for(int icase=0; icase<jcase; icase++){
		scanf("%d %d", &N, &K);
		
		for(int i=0; i<N; i++){
			scanf("%lf", &chance[i]);
		}
		
		best = 0;
		for(int i=0; i<(1<<N); i++){
			Dowork(i);
		}
		
		printf("Case #%d: %.7lf\n", icase+1, best);
	}
	
	return 0;
}
