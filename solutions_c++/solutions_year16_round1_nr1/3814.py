#include <bits/stdc++.h>
using namespace std;
int main(int argc, char const *argv[])
{
	string s, s1;
	
	int n;
	cin >> n;
	for (int k = 0; k < n; ++k)
	{
		cin >> s;
		int end = 1000;
		int ben = 1000;
		char ant = 	s[0];
		char f [20001];
		f[1000] = s[0];	
		for (int i = 1; i < s.length(); ++i)
		{
			//cout << (int)s[i] << " " << (int)ant << endl;
			if((int)s[i]>=(int)ant){
				f[--ben] = s[i];
				ant = f[ben];
			}else{
				f[++end] = s[i];
			}

		}
		cout << "Case #"<< k+1 <<": ";
		for (int i = ben; i <= end; ++i)
		{
			cout << f[i];
		}
		cout << endl;
	}
	return 0;
}