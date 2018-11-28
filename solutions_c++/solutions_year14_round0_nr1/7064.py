#define _USE_MATH_DEFINES
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <set>
#include <vector>
#include <algorithm>
#include <queue>
#include <list>
#include <map>
#include <cmath>

using namespace std;

int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int T;
	cin >> T;
	int mp[2][4][4];
	for(int step=1; step<=T; ++step)
	{
		int ans[2];
		for(int l=0; l<2; ++l)
		{
			cin >> ans[l];
			--ans[l];
			for(int i=0; i<4; ++i)
				for(int j=0; j<4; ++j)
				{
					cin >> mp[l][i][j];
				}
		}
		int cnt=0, aa=0;
		for(int i=0; i<4; ++i)
			for(int j=0; j<4; ++j)
				if(mp[0][ans[0]][i]==mp[1][ans[1]][j]){
					++cnt;
					aa=mp[0][ans[0]][i];
				}
		cout << "Case #"<<step<<": ";
		if(cnt==0)
			cout << "Volunteer cheated!" << endl;
		if(cnt==1)
			cout << aa << endl;
		if(cnt>1)
			cout << "Bad magician!" << endl;
	}
	//fclose(stdin);
	//fclose(stdout);
}
