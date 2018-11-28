
#include <iostream>
#include <algorithm>
using namespace std;

FILE *fp_in, *fp_out;
int idx = 0, ret;
int T; // test case #
int N; // size
char s_in[3000]; // char value
char c_in;
int  ia_in[1000]; // int value 
int  i_in;


void init()
{
	fopen_s(&fp_in, "./A-large.in", "r");
	fopen_s(&fp_out, "./A-large.out", "w");

	// test case # T
	ret = fscanf_s(fp_in, "%d\n", &T, sizeof(T));
	if (!ret || ret == EOF)
		cout << "check file format" << endl;
	cout << "Total # : " << T << endl;

}

void read_input()
{
	//// get size N
	//ret = fscanf_s(fp_in, "%d\n", &N, sizeof(N));
	//cout << "N : " << N << endl;

	// get string case
	ret = fscanf_s(fp_in, "%s\n", s_in, sizeof(s_in));
	cout << "str_input : " << s_in << endl;

	//// get int case
	//ret = fscanf_s(fp_in, "%d\n", &i_in, sizeof(i_in));
	//cout << "int_input : " << i_in << endl;

	//for (int i = 0; i < N; i++){
	//	//fscanf_s(fp_in, "%d", iV + i, sizeof(iV[i]));
	//	cout << iV[i] << endl;

	//}



}


int main()
{
	init();

	
	for (int idx = 0; idx < T; idx++)
	{
		read_input();

		// ----------------------------------------------
		char ans[3000]="";

		int cnt_char = 0;
		int cnt_ans = 0;
		int digit[10] = { 0 };

		while (cnt_char != strlen(s_in)){

			//find 0
			for (int i = 0; i < strlen(s_in); i++){
				if (s_in[i] == 'Z'){
					cnt_char += 4;
					ans[cnt_ans++] = '0';
					digit[0]++;
					//break;
				}				
			}

			//find 2
			for (int i = 0; i < strlen(s_in); i++){
				if (s_in[i] == 'W'){
					cnt_char += 3;
					ans[cnt_ans++] = '2';
					digit[2]++;
					//break;
				}
			}

			//find 4
			for (int i = 0; i < strlen(s_in); i++){
				if (s_in[i] == 'U'){
					cnt_char += 4;
					ans[cnt_ans++] = '4';
					digit[4]++;
					//break;
				}
			}

			//find 6
			for (int i = 0; i < strlen(s_in); i++){
				if (s_in[i] == 'X'){
					cnt_char += 3;
					ans[cnt_ans++] = '6';
					digit[6]++;
					//break;
				}
			}

			//find 8
			for (int i = 0; i < strlen(s_in); i++){
				if (s_in[i] == 'G'){
					cnt_char += 5;
					ans[cnt_ans++] = '8';
					digit[8]++;
					//break;
				}
			}

			//find 7
			int cnt6 = 0;
			int cnt7 = 0;
			for (int i = 0; i < strlen(s_in); i++){
				if (s_in[i] == 'S'){
					if (cnt6 < digit[6]){
						cnt6++;
						continue;
					}

					/*if (cnt7 < digit[7]){
						cnt7++;
						continue;
					}*/

					cnt_char += 5;
					ans[cnt_ans++] = '7';
					digit[7]++;


					
				}
			}

			//find 5
			int cnt4 = 0;
			int cnt5 = 0;
			for (int i = 0; i < strlen(s_in); i++){
				if (s_in[i] == 'F'){
					if (cnt4 < digit[4]){
						cnt4++;
						continue;
					}
					/*if (cnt5 < digit[5]){
						cnt5++;
						continue;
					}*/

					cnt_char += 4;
					ans[cnt_ans++] = '5';
					digit[5]++;


					
				}
			}

			//find 3
			int cnt8 = 0;
			int cnt3 = 0;
			for (int i = 0; i < strlen(s_in); i++){
				if (s_in[i] == 'H'){
					if (cnt8 < digit[8]){
						cnt8++;
						continue;
					}
					/*if (cnt3 < digit[3]){
						cnt3++;
						continue;
					}*/
					
					cnt_char += 5;
					ans[cnt_ans++] = '3';
					digit[3]++;
						

				}
			}

			//find 1
			int cnt0 = 0, cnt2 = 0;
			cnt4 = 0;
			int cnt1 = 0;
			for (int i = 0; i < strlen(s_in); i++){
				if (s_in[i] == 'O'){
					if (cnt0 < digit[0]){
						cnt0++;
						continue;
					}
					if (cnt2 < digit[2]){
						cnt2++;
						continue;
					}
					if (cnt4 < digit[4]){
						cnt4++;
						continue;
					}
					/*if (cnt1 < digit[1]){
						cnt1++;
						continue;
					}*/

					cnt_char += 3;
					ans[cnt_ans++] = '1';
					digit[1]++;
					
					

				}
			}

			//find 9
			cnt1 = 0;
			cnt7 = 0;
			int cnt9 = 0;
			for (int i = 0; i < strlen(s_in); i++){
				if (s_in[i] == 'N'){
					if (cnt1 < digit[1]){
						cnt1++;
						continue;
					}
					if (cnt7 < digit[7]){
						cnt7++;
						continue;
					}

					if (cnt9 < digit[9]){
						cnt9++;
						continue;
					}

					cnt_char += 4;
					ans[cnt_ans++] = '9';
					digit[9]++;
					


				}
			}

		}
		// ----------------------------------------------

		sort(ans, ans + cnt_ans);
		ans[cnt_ans] = '\0';
		cout << "Case #" << idx + 1 << ": " << ans << endl;
		fprintf(fp_out, "Case #%d: %s\n", idx + 1, ans);
	}




	fclose(fp_in);
	fclose(fp_out);
}