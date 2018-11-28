#include <cstdio>
#include <cstring>

using namespace std;

#define _DEBUG
#undef _DEBUG

#ifdef _DEBUG

#endif

int main(int argc, char const *argv[])
{
	char s[1001];
	int max, people;
	int repeat;
	int Sm;
	int L;

	scanf("%d", &repeat);

	for(int r = 0; r < repeat; ++r){

		scanf("%d", &Sm);
		scanf("%s", s);

		L = strlen(s);

		max = 0;
		people = 0;

		/*
		If max is not sufficient to reach current level, 
		then add people to meet the level
		*/

		for(int j = 0; j < L; ++j){
			// wrong code
			// if (max < s[j] - 48) {
			// 	people += (max - s[j] + 48);
			// 	max = s[j] - 48;
			// }

			if (s[j] > 48) {
				if (max < j) {
					people += j - max;
					max = j;
				}
				max += (s[j] - 48);
			}


		}

		printf("CASE #%d: %d\n", r + 1, people);


#ifdef _DEBUG
		printf("string is %s\n", s);
#endif

	}

	return 0;
}