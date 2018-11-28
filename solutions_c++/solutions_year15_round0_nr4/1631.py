#include <iostream>
#include <string>
#include <algorithm>
#define G "GABRIEL"
#define R "RICHARD"

using namespace std;

string ans[500];

void pre()
{
	ans[111] = G; ans[112] = R; ans[113] = R; ans[114] = R;
	ans[121] = G; ans[122] = G; ans[123] = R; ans[124] = R;
	ans[131] = G; ans[132] = R; ans[133] = R; ans[134] = R;
	ans[141] = G; ans[142] = G; ans[143] = R; ans[144] = R;
	ans[221] = G; ans[222] = G; ans[223] = R; ans[224] = R;
	ans[231] = G; ans[232] = G; ans[233] = G; ans[234] = R;
	ans[241] = G; ans[242] = G; ans[243] = R; ans[244] = R;
	ans[331] = G; ans[332] = R; ans[333] = G; ans[334] = R;
	ans[341] = G; ans[342] = G; ans[343] = G; ans[344] = G;
	ans[441] = G; ans[442] = G; ans[443] = R; ans[444] = G;
}

int main()
{
	int T;
	cin >> T;
	pre();
	for(int t = 1; t <= T; ++t){
		int x, r, c;
		cin >> x >> r >> c;
		if(r > c)
			swap(r,c);
		cout << "Case #" << t << ": " << ans[r*100 + c*10 + x] << endl;
	}
	return 0;
}