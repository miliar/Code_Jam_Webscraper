#include "include\preCompile\KL_PreCompile.hpp"

#define INPUT_FILE_PATH "D:\\DUMP\\input.in"
#define OUTPUT_FILE_PATH "D:\\DUMP\\output.out"

using namespace kewl_Library;
void init()
{
}

int main(){
	clock_t time1;
	time1 = clock();

#if 1
	freopen(INPUT_FILE_PATH, "r", stdin);
	freopen(OUTPUT_FILE_PATH, "w", stdout);
#endif	

	int T;
	scanf("%d", &T);

	int N, X, s[10005];
	for (LLI caseNum = 1; caseNum <= T; caseNum++){
		if (caseNum== 2)
		{
			int d = 0;
		}
		scanf("%d%d", &N, &X);

		KL_FOR_DEF(i, N){
			scanf("%d", &s[i]);
		}


		sort(s, s+N);

		int endIndex = N-1;
		int totCount = 0;
		KL_FOR_DEF(i, N){

			int j = endIndex;

			if (i > j){ break;}

			while ( s[i] + s[j] > X && i < j) {
				--j;
				totCount++;
			}


			if (i >= j){
				++totCount;

				break;
			}
			if (s[i] + s[j] <= X ){
				++totCount;

				endIndex = j-1;
			}

		}
		printf("Case #%d: ", caseNum);
		cout << totCount << endl;


	}


#if 0
	clock_t time2, timeTaken;
	time2 = clock();
	timeTaken = time2 - time1;
	long long int seconds = timeTaken/CLOCKS_PER_SEC;
	long long int minutes = seconds/60;
	seconds %= 60;

	/*	-------- BEWARE - DON'T cout while doing freopen()	-------- 	*/
	cout << minutes << "min" << seconds << "sec";
#endif
}
