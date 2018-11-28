#include <iostream>

using namespace std;

int idx=0;
int T, N, ret, m, last;
int tf[10] = { 0, }, all = 0;

int checkDone()
{
	int all, j;
	for (j = 0; j < 10; j++){
		if (!tf[j]){
			all = 0;
			break;
		}
	}
	
	if (j == 10)
		all = 1;

	return all;
}

void init()
{ 
	m = 1;
	all = 0; 

	for (int j = 0; j < 10; j++){
		tf[j] = 0;
	}

}


int main()
{
	FILE *fp, *fp_out;
	fopen_s(&fp, "./large_input.txt", "r"); 
	fopen_s(&fp_out, "./large_output.txt", "w");

	ret = fscanf_s(fp, "%d\n", &T, sizeof(T));
	cout << "  T : " << T << endl;
	//for (int idx = 0; idx < T; idx++){		
	while (1){

		ret = fscanf_s(fp, "%d\n", &N, sizeof(N));	
		cout << "N : " << N << endl;
		if (ret == EOF || !ret)
			break;

		if (N == 0){
			cout << "Case #1: INSOMNIA" << endl;
			fprintf(fp_out, "Case #1: INSOMNIA\n", idx + 1, last);
		}
		else{
			init();

			while (!all){			
				last = N*m;				
				int digit = last;
				while (digit){					
					tf[digit % 10] = 1;
					digit = digit / 10;
				}
				all = checkDone();
				m = m + 1;
			}

			cout << "Case #" << idx + 1 << ": " << last << endl;
			fprintf(fp_out, "Case #%d: %d\n", idx + 1, last);
		}

		idx++;
	}

	fclose(fp);
	fclose(fp_out);
}