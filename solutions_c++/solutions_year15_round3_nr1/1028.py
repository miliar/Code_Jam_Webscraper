#include<string>
#include<iostream>
#include<algorithm>

using namespace std;

int main(){

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int ntc,r,c,w,res;
	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){
		cin >> r >> c >> w;
		res = c/w;
		res *= r;
		res += w-(c%w==0);
		cout << "Case #" << tc << ": " << res << endl;
	}

	return 0;
}