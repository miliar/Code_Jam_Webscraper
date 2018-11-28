#include <cstdio>
#include <cstring>
using namespace std;

int T;
int possible[17];
int ans1 , ans2;

FILE *fin = fopen("A-small.in" , "r");
FILE *fout = fopen("A-small.out" , "w");

int main(){
	fscanf(fin , "%d" , &T);
	for(int t = 1 ; t <= T ; t++){
		memset(possible , 0 , sizeof(possible));
		fscanf(fin , "%d" , &ans1);
		for(int i = 1 ; i <= 4 ; i++){
			for(int j = 1 ; j <= 4 ; j++){
				int x;
				fscanf(fin , "%d" , &x);
				if(i == ans1)
					possible[x] = 1;
			}
		}
		fscanf(fin , "%d" , &ans2);
		for(int i = 1 ; i <= 4 ; i++){
			for(int j = 1 ; j <= 4 ; j++){
				int x;
				fscanf(fin , "%d" , &x);
				if(i == ans2)
					possible[x]++;
			}
		}
		int res;
		int cnt = 0;
		for(int i = 1 ; i <= 16 ; i++)
			if(possible[i] == 2){
				res = i;
				cnt++;
			}
		fprintf(fout, "Case #%d: " , t);
		if(cnt > 1) fprintf(fout, "Bad magician!\n");
		if(cnt == 0) fprintf(fout, "Volunteer cheated!");
		if(cnt == 1) fprintf(fout, "%d\n" , res);
	}
	return 0;
}