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

int w, h;
bool isPlaced[16][16];
const int INF = 987654321;

int ans = 0;


int put(int pos, int remain)
{
	int y = pos / w;
	int x = pos % w;

	if(remain == 0)
		return ans;

	if(y >= h || x >= w)
		return INF;
	
	int ret = INF;
	
	// �� �ڸ��� ���´�.
	isPlaced[y][x] = true;

	// ������ ���ÿ� �߰��Ǵ� edge���� �˻��Ѵ�.
	if(y-1 >= 0 && isPlaced[y-1][x])
		ans++;
	if(y+1 < h && isPlaced[y+1][x])
		ans++;
	if(x-1 >= 0 && isPlaced[y][x-1])
		ans++;
	if(x+1 < w && isPlaced[y][x+1])
		ans++;

	ret = min(ret, put(pos+1, remain-1));


	isPlaced[y][x] = false;
	if(y-1 >= 0 && isPlaced[y-1][x])
		ans--;
	if(y+1 < h && isPlaced[y+1][x])
		ans--;
	if(x-1 >= 0 && isPlaced[y][x-1])
		ans--;
	if(x+1 < w && isPlaced[y][x+1])
		ans--;

	ret = min(ret, put(pos+1, remain));

	return ret;
}


int main(void)
{
#ifdef USEFILE
	FILE* inf = freopen("B.in", "r", stdin);
	FILE* outf = freopen("B_out.txt.", "w", stdout);
#endif

	int tc;
	cin >> tc;

	for(int testNum = 1; testNum <= tc; testNum++)
	{
		int smiles;
		cin >> h >> w >> smiles;
		memset(isPlaced, 0, sizeof(isPlaced));
		ans = 0;

		cout << "Case #" << testNum << ": " << put(0, smiles) << endl;
	}


#ifdef USEFILE
	fclose(inf);
	fclose(outf);
#endif

	return 0;
}