#include<stdio.h>
#include<vector>

using namespace std;

int map[4][4];
int map1[4];
int map2[4];

int main()  {
	int t, i, j, k;
	long double count, C, F, X;
	long double rate;
	FILE* f = fopen("B-Large.in", "r+");
	FILE*f1 = fopen("B-Large.out", "w+");
	fscanf(f, "%d", &t);
	for (i = 0; i < t; i++){
		fscanf(f,"%lf %lf %lf", &C, &F, &X);
		count = 0;
		rate = 2;
		while (true) {
			if (X / rate > X / (rate + F) + C / rate) {

				count += C / rate;
				rate += F;
			}
			else {
				count += X / rate;
				break;
			}
		}
		fprintf(f1,"Case #%d: %Lf\n", i+1,count);
	}
	fclose(f);
	fclose(f1);




	return 0;

}

