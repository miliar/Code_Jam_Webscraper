#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <algorithm>

char str[3000];

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);

	for(int iter = 1; iter <= T; iter++){
		printf("Case #%d: ", iter);

		scanf("%s", str);
		int cnt[10] = {0}, al[40] = {0};
		int size = strlen(str);
		vector <int> v;

		for(int i = 0; i < size; i++)
			al[str[i]-'A']++;
		//      .    .      .    .    .  .      .
		// ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE 
		
		for(int i = 0; i < al['X'-'A']; i++){
			v.push_back(6);
			al['S'-'A']--;
			al['I'-'A']--;
		}

		for(int i = 0 ; i < al['Z'-'A']; i++){
			v.push_back(0);
			al['R'-'A']--;
			al['O'-'A']--;
			al['E'-'A']--;
		}

		for(int i = 0; i < al['S'-'A']; i++){
			v.push_back(7);
			al['N'-'A']--;
			al['V'-'A']--;
		}

		for(int i = 0; i < al['W'-'A']; i++){
			v.push_back(2);
			al['O'-'A']--;
		}

		for(int i = 0; i < al['U'-'A']; i++){
			v.push_back(4);
			al['R'-'A']--;
			al['O'-'A']--;
		}

		for(int i = 0; i < al['O'-'A']; i++){
			v.push_back(1);
		}

		for(int i = 0; i < al['R'-'A']; i++){
			v.push_back(3);
		}

		for(int i = 0; i < al['V'-'A']; i++){
			v.push_back(5);
			al['I'-'A']--;
		}

		for(int i = 0; i < al['G'-'A']; i++){
			v.push_back(8);
			al['I'-'A']--;
		}

		for(int i = 0; i <al['I'-'A']; i++)
			v.push_back(9);

		sort(v.begin(), v.end());

		//printf("size = %d\n", size);
		for(int i = 0; i < v.size(); i++)
			printf("%d", v[i]);
		printf("\n");
	}

	return 0;
}