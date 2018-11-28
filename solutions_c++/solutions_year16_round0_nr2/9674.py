#include <bits/stdc++.h>

using namespace std;

string S;

int counting(int pos,bool plus)
{
	int sz=S.size();
	if (pos==sz) return 0;
	int pos2=pos;

	char cur = (plus ? '+' : '-');

	while (pos2<sz && S[pos2]==S[pos]) pos2++;

	if (S[pos]==cur) return counting(pos2,plus);
	else return 1+counting(pos2,!plus);

}


int main()
{

	int tc,TC=0;
	cin >> tc;

	while (tc--){
		cin >> S;
		reverse(S.begin(),S.end());
		cout << "Case #" << ++TC << ": " << counting(0,true) << endl;
	}

	return 0;
}