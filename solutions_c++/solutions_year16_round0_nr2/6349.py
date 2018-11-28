#include <iostream>

using namespace std;

int idx = 0;
int T, N, ret, ans;
char S[200];


void init()
{
	ans = 0;
}


int main()
{
	FILE *fp, *fp_out;
	fopen_s(&fp, "./B-large.in", "r");
	fopen_s(&fp_out, "./large_out.txt", "w");

	ret = fscanf_s(fp, "%d\n", &T, sizeof(T));
	cout << "  Test Case # : " << T << endl;
		
//	while (1){
	for (int k = 0; k < T; k++){

		//ret = fscanf_s(fp, "%d\n", &N, sizeof(N));
		//cout << "N : " << N << endl;
		ret = fscanf_s(fp, "%s\n", S, sizeof(S));
		cout << "S : " << S << endl;
		//
		//if (ret == EOF || !ret)
		//break;

		//else{
		
		init();
			
		int len = strlen(S);
		int pos = 0;
		int j;
		for (j = len-1; j>-1; j--){
			if (S[j] == '-'){
				pos = j;
				break;
			}
		}
		if (j == -1){
			ans = 0;
		}

		else{
			char pre = S[0];
			ans = 1;
			for (int j = 1; j < pos+1; j++)
			{
				if (S[j] != pre){
					ans++;						
				}
				pre = S[j];
			}			
		}
			//cout << "Case #" << idx + 1 << ": " << ans << endl;
			//fprintf(fp_out, "Case #%d: %d\n", idx + 1, ans);
			cout << "Case #" << k + 1 << ": " << ans << endl;
			fprintf(fp_out, "Case #%d: %d\n", k + 1, ans);
			
	}

		

	fclose(fp);
	fclose(fp_out);
}