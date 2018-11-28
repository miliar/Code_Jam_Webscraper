#include <cstdio>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#define mod 1000000007
using namespace std;
int f = 0;
bool beg = true;
// char sol[1000000]={'\0'};
bool ordering(int t, int N, int P[], char sol[]){
	int total = 0;
	for(int i = 0; i < N; i++){
		// printf("%d ", P[i]);
		total += P[i];
	}
	// printf("\n");
	if(!beg && t == 2)
	for(int i = 0; i < N; i++){
		if(P[i] && P[i]*2 > total){
			// printf("---%c %d\n", i + 'A', total);
			return false;
		}
	}
	else
		beg = false;		
	if(total == 0)
		return true;

	for(int i = 0; i < N; i++){
		if(P[i]){
			P[i]--;
			if(t == 1){
				f += 2;
				if(ordering(2, N, P, sol)){
					f-=2;
					//printf("%d\n", f);
					sol[f] = 'A'+i;
					sol[f+1] = ' ';
					// printf("%c ", 'A'+i);
					return true;
				}
				f -= 2;
			}
			if(t == 2){	
				f += 1;
				if(ordering(1, N, P, sol)){
					f -= 1;
					//printf("%d\n", f);
					sol[f] = 'A'+i;

					// printf("%c", 'A'+i);
					return true;
				}
				f -= 1;
				f += 2;
				if(ordering(2, N, P, sol)){
					f-=2;
					//printf("%d\n", f);
					sol[f] = 'A'+i;
					sol[f+1] = ' ';
					// printf("%c ", 'A'+i);
					return true;
				}
				f -= 2;					
			}
			P[i]++;			
		}
	}

	return false;		
}
int main(int argc, char const *argv[])
{
	int T = 0;
	scanf("%d", &T);
	for(int t = 0; t < T; t++){
		beg = true;
		char solx[1000000]={'\0'};
		// sol = solx;
		int N;
		int total = 0;
		scanf("%d", &N);
		int P[N];
		for(int n = 0; n < N; n++){
			scanf("%d", &P[n]);
			total += P[n];
		}
		if(ordering(2, N, P, solx))
			printf("Case #%d: %s", t+1, solx);
		// for(int i = 0; i < 1000000; i++)
		// 	printf("%c", sol[i]);
		printf("\n");

	}
	return 0;
}