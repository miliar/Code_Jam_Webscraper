#include <iostream>
#include <fstream>
using namespace std;


int main()
{
	int n;
	int ans = 0;
	ifstream ist("input3.in");
	ofstream ost("input3.out");
	int l,r;
	ist >>n;
	for (int i = 1;i<=n;i++)
	{
		ans = 0;
		ist>>l>>r;
		if (l == 1) ans ++;
		if ((l<=4)&&(r>=4)) ans ++;
		if ((l<=9)&&(r>=9)) ans ++;
		if ((l<=121)&&(r>=121)) ans ++;
		if ((l<=484)&&(r>=484)) ans ++;
		ost<<"Case #"<<i<<": "<<ans<<endl;
	}
}