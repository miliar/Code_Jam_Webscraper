#include<iostream>
#include<stdio.h>
#include<map>
using namespace std;
int dp[11000];
char str[11000];
int ins[300][300];
int ans[3] = { 'i', 'k', -1 };
int T, L, X;
int main(){
	FILE* fp1 = fopen("C-small-attempt0.in", "r");
	FILE* fp2 = fopen("output.txt", "w");
	ins[1][1] = 1; ins[1]['i'] = 'i'; ins[1]['j'] = 'j'; ins[1]['k'] = 'k';
	ins['i'][1] = 'i'; ins['j'][1] = 'j'; ins['k'][1] = 'k';
	ins['i']['i'] = -1; ins['i']['j'] = 'k'; ins['i']['k'] = -'j';
	ins['j']['i'] = -'k'; ins['j']['j'] = -1; ins['j']['k'] = 'i';
	ins['k']['i'] = 'j'; ins['k']['j'] = -'i'; ins['k']['k'] = -1;

	fscanf(fp1,"%d", &T);
	for (int t = 0; t < T; t++){
		int aindex = 0;
		fscanf(fp1, "%d %d\n", &L, &X);
		for (int x = 0; x < X; x++){
			for (int l = 0; l < L; l++){
				char temp;
				if (l == 0 && x == 0){
					fscanf(fp1, "%c", &temp);
					str[l] = temp;
					dp[0] = temp;
				}
				else if(x == 0){
					fscanf(fp1, "%c", &temp);
					str[l] = temp;
					if (dp[l-1] < 0)
						dp[l] = -ins[(-dp[l-1])][temp];
					else
						dp[l] = ins[dp[l - 1]][temp];
				}
				else if (x != 0){
					temp = str[l];
					if (dp[l + (x*L) - 1] < 0)
						dp[l + (x*L)] = -ins[-dp[l + (x*L) - 1]][temp];
					else
						dp[l + (x*L)] = ins[dp[l + (x*L) - 1]][temp];

				}
				if (ans[aindex] == dp[l + (x*L)]){
					if (aindex == 2 && l + (x*L) == X*L - 1)
						aindex++;
					else if (aindex != 2)
						aindex++;
				}
				//printf("str[%d] : %c ", l, temp);
				//printf("%d: %d!\n", l + (x*L), dp[l + (x*L)]);
			}
		}
		if (aindex == 3)
			fprintf(fp2,"Case #%d: YES\n",t+1);
		else
			fprintf(fp2,"Case #%d: NO\n", t + 1);
	}
}