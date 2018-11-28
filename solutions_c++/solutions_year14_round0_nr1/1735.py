#include <fstream>
#include <iostream>
#include <stdio.h>
using namespace std;

int T, R;
int cards[4];
int trash[4];
int ans[4];
int realAns[4];
int match;

int main(){
	FILE* in = fopen("C:\\Users\\Jinhyuk\\Desktop\\CodeJam 2014\\Qual\\A-small-attempt0.in", "r");
	FILE* out = fopen("C:\\Users\\Jinhyuk\\Desktop\\CodeJam 2014\\Qual\\testResult.txt", "w");
	
	fscanf(in, "%d", &T);
	for(int i=0; i<T; i++){
		match = 0;
		fscanf(in, "%d", &R);
		for(int j=0; j<4; j++){
			if(j+1 == R)
				fscanf(in, "%d %d %d %d", &ans[0], &ans[1], &ans[2], &ans[3]);
			else
				fscanf(in, "%d %d %d %d", &trash[0], &trash[1], &trash[2], &trash[3]);
		}

		fscanf(in, "%d", &R);
		for(int j=0; j<4; j++){
			if(j+1 == R)
				fscanf(in, "%d %d %d %d", &cards[0], &cards[1], &cards[2], &cards[3]);	
			else
				fscanf(in, "%d %d %d %d", &trash[0], &trash[1], &trash[2], &trash[3]);
		}
		for(int j=0; j<4; j++){
			for(int k=0; k<4; k++){
				if(ans[j] == cards[k]){
					realAns[match++] = ans[j];
				}
			}
		}
		if(match == 0)
			fprintf(out, "Case #%d: Volunteer cheated!\n", i+1);
		else if(match == 1)
			fprintf(out, "Case #%d: %d\n", i+1, realAns[0]);
		else
			fprintf(out, "Case #%d: Bad magician!\n", i+1);


	}
	fclose(in);
	fclose(out);
	return 0;
}

