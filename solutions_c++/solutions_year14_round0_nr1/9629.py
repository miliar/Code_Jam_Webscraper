// GCJ1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdlib>
#include <cstdio>
#define BUFFER_SIZE 512

using namespace std;
int _tmain(int argc, _TCHAR* argv[])
{
	FILE *f;
	char buffer[512];
	unsigned int T, g1, g2, gr1[4][4], gr2[4][4];
	fopen_s(&f, "a.txt","r");
	fgets(buffer, 512, f);
	T = atoi(buffer);
	//printf("%d\n", T); 
	for (unsigned int g = 0; g < T; g++){
		fgets(buffer, 512, f);
		g1 = atoi(buffer);
		//printf("Guess1: %d\n", g1);
		for (unsigned j = 0; j < 4; j++){
			fgets(buffer, 512, f);
			unsigned int k = 0, l=0;
			char *temp;
			temp = buffer;
			while (l<4){
				if (buffer[k] == ' ' || buffer[k] == '\0'){
					buffer[k] = '\0';
					gr1[j][l] = atoi(temp);
					temp = buffer + k+1;
					//printf("%d ", gr1[j][l]);
					l++;
				}
				k++;
			}
			//printf("\n");
		}
		fgets(buffer, 512, f);
		g2 = atoi(buffer);
		//printf("Guess2: %d\n", g2);
		for (unsigned j = 0; j < 4; j++){
			fgets(buffer, 512, f);
			unsigned int k = 0, l = 0;
			char *temp;
			temp = buffer;
			while (l<4){
				if (buffer[k] == ' ' || buffer[k] == '\0'){
					buffer[k] = '\0';
					gr2[j][l] = atoi(temp);
					temp = buffer + k + 1;
					//printf("%d ", gr2[j][l]);
					l++;
				}
				k++;
			}
			//printf("\n");
		}
		//case read - Now Process it!
		//Answer==gr1[guess1] intersection gr2[guess2]
		g1--;
		g2--;
		//printf("Solving...\n");
		int answer = 0, count = 0;
		for (unsigned int i = 0; i < 4; i++){
			for (unsigned int j = 0; j < 4; j++){
				if (gr1[g1][i] == gr2[g2][j]){
					count++;
					answer = gr1[g1][i];
					//printf("t: %u %u \n", gr1[g1][i], gr2[g2][j]);
				}
				else{
					//printf(".");
				}
			}
		}
		printf("Case #%u: ",g+1);
		if (count > 1) printf("Bad magician!\n");
		else if (count == 0) printf("Volunteer cheated!\n");
		else printf("%u\n", answer);
	}
	fclose(f);
	return 0;
}

