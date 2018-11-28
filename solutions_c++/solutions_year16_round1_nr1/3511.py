#include <bits/stdc++.h>
#define lli long long int
#define s(x) scanf("%lld", &x)

using namespace std;

string aa, bb, cc;

string func(int stt, int ett)
{
	if (ett < stt) {
		cc = "";

		return cc;
	}

	if (stt == ett) {
		cc = aa[stt];
		return cc;
	}

	int i,j,k;
	char a,b,c;

	a = aa[stt];
	j = stt;

	for (i = stt+1; i <= ett; ++i) {
		if (aa[i] >= a) {
			a = aa[i];
			j = i;
		}
	}
	
	cc = aa[j] + func(stt, j-1) + aa.substr(j+1, ett-j);	

	return cc;
}

int main()
{
	lli tt,tcase,i,j,k,ans,temp;

	s(tcase);
	tt = 1;

	while (tcase--) {
		cout << "Case #" << tt << ": ";
		++tt;

		cin >> aa;
/*		bb = "";

		bb =  aa[0];
		
//		cout << bb << endl;

		for (i = 1; i < aa.length(); ++i) {
			 if (aa[i] > bb[0]) {
				bb = aa[i] + bb;
			 } else {
				bb = bb + aa[i];
			}
		}*/

		cout << func(0, aa.length()-1) << endl;
	}

	return 0;
}
