#include <iostream>
#include <cstring>
using namespace std;
char strRaw[1000];
int main()
{
	int T;cin>>T;
	for(int TT = 1; TT <= T; TT++)
	{
		printf("Case #%d: ",TT);
		scanf("%s",strRaw);
		int ptri = 0,ptrj = 0;
		while(strRaw[ptrj])
		{
			while(strRaw[ptrj] && strRaw[ptrj] == strRaw[ptri]) ptrj++;
			if(strRaw[ptrj])
			{
				strRaw[++ptri] = strRaw[ptrj];
			}
		}
		strRaw[++ptri] = '\0';
		int len = strlen(strRaw);
		if(strRaw[len - 1] == '+')
			cout << len - 1 << endl;
		else cout << len <<endl;
	}
	return 0;
}