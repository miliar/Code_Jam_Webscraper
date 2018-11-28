#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <cstring>
#include <cmath>
#include <queue>
#include <set>
#include <map>
using namespace std;

#define USEFILE


// 1ijk <-> 0123
const string res[4] = {"0123", "1032", "2301", "3210"};
const string signChg[4] = {"0000", "0101", "0110", "0011"};


int main(void)
{

#ifdef USEFILE
	FILE* inf = freopen("C.in", "r", stdin);
	FILE* outf = freopen("C_out.txt.", "w", stdout);
#endif

	int tc;
	cin >> tc;

	for(int testNum = 1; testNum <= tc; testNum++)
	{
		int l, x;		// large input : long long
		cin >> l >> x;

		string temp;
		cin >> temp;

		string line;
		for(int i = 0; i < x; i++)
			line += temp;


		int result = line[0] - 'i' + 1;
		int phase = 1;
		int idx = 1;
		bool isPositive = true;

		for(	;	idx < line.size(); idx++)
		{
			//printf("idx : %d , result : %d\n", idx, result);

			if(result == 1 && isPositive)	
				break;
			
			int tmpResult = res[result][line[idx]-'i'+1] - '0';
			if(signChg[result][line[idx]-'i'+1] == '1')
				isPositive = !isPositive;

			result = tmpResult;
		}
		
		if(result != 1 || !isPositive || idx == line.size())
		{
			printf("Case #%d: NO\n", testNum);
			continue;
		}

		/*if(idx != line.size())
			cout << "i를 찾았습니다. idx : " << idx << endl;*/



		phase = 2;
		result = line[idx] - 'i' + 1;
		idx++;
		for(	;	idx < line.size(); idx++)
		{
			//printf("idx : %d , result : %d\n", idx, result);

			if(result == 2 && isPositive)	
				break;
			
			int tmpResult = res[result][line[idx]-'i'+1] - '0';
			if(signChg[result][line[idx]-'i'+1] == '1')
				isPositive = !isPositive;

			result = tmpResult;
		}

		if(result != 2 || !isPositive || idx == line.size())
		{
			printf("Case #%d: NO\n", testNum);
			continue;
		}



		phase = 3;
		result = line[idx] - 'i' + 1;
		idx++;
		for(	;	idx < line.size(); idx++)
		{
			//printf("idx : %d , result : %d\n", idx, result);			
			int tmpResult = res[result][line[idx]-'i'+1] - '0';
			if(signChg[result][line[idx]-'i'+1] == '1')
				isPositive = !isPositive;

			result = tmpResult;
		}

		if(result != 3 || !isPositive)
			printf("Case #%d: NO\n", testNum);
		else
			printf("Case #%d: YES\n", testNum);

		
	}


#ifdef USEFILE
	fclose(inf);
	fclose(outf);
#endif

	return 0;
}