#include <stdio.h>
#include <string.h>

char mat[5][5];
int N;
int cost;
int best;

bool mach[5];
bool pers[5];

void Test(){
	for(int i=0; i<N; i++){ 
		mach[i] = false;
		pers[i] = false;
	}
		
	for(int i=0; i<N; i++){
		if(pers[i]) continue;
		 
		int nmac=0;
		for(int j=0; j<N; j++){
			if(mat[i][j] == '1') nmac++;
		}
		pers[i] = true;
		
		for(int j=i+1; j<N; j++){
			if(strcmp(mat[i], mat[j]) == 0){
				pers[j] = true;
				nmac--;
			}
		}
		
		if(nmac != 1) return;
		for(int j=0; j<N; j++){
			if(mat[i][j] == '1') mach[j] = true;
		}
	}
	
	for(int i=0; i<N; i++){
		if(!pers[i]) return;
		if(!mach[i]) return;
	}
	
	if(cost < best) best = cost;
}

void Rec(int id){
	if(id == N*N){
		Test();
		return;
	}

	int row = id/N;
	int col = id - row*N;
	Rec(id+1);
	if(mat[row][col] == '0'){
		mat[row][col] = '1';
		cost++;
		Rec(id+1);
		mat[row][col] = '0';
		cost--;
	}
}

int main(){
	int jcase;
	
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	
	scanf("%d", &jcase);
	for(int icase=0; icase<jcase; icase++){
		scanf("%d", &N);
		
		for(int i=0; i<N; i++){
			scanf("%s", mat[i]);
		}
		
		cost = 0;
		best = 900;
		Rec(0);
		
		printf("Case #%d: %d\n", icase+1, best);
	}
	
	return 0;
}
