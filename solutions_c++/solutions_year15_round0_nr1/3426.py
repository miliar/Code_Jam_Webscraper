#include <iostream>
#include <string>
#include <fstream>

using namespace std;
#define	FILE_OUTPUT	0
int main()
{
	int T, S_max, friends, allAud;
	string	input;
	char nowAud[2];
	nowAud[1] = '\n';

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

#if FILE_OUTPUT
	ofstream output("output.txt");
#endif

	cin >> T;
	for (int i = 1; i <= T; ++i)
	{

		//--- init
		friends = 0;
		allAud = 0;
		cin >> S_max;
		cin >> input;
		//printf("S_max:%d InputString:%s\n", S_max, input.c_str());
		string::iterator itr = input.begin();

		//int preAud = atoi((const char*)input[0]);
		nowAud[0] = *itr;
		int preAud = atoi((const char*)nowAud);
		for (int j = 1; j < S_max+1 ; ++j)
		{
			nowAud[0] = *(++itr);
			int curAud = atoi((const char*)nowAud);
			//printf("%d\t", curAud);

			if (j > preAud && curAud != 0) {
				// Friend is needed..
				curAud += j - preAud;
				friends += j - preAud;
				
			}
			preAud += curAud;
		}
		//printf("\n");

		printf("Case #%d: %d\n", i, friends);
#if FILE_OUTPUT
		output << "Case #" << i << ": " << friends << endl;
#endif
	}
#if FILE_OUTPUT
	output.close();
#endif
	return 0;
}