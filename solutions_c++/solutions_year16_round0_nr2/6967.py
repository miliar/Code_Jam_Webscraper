#include <iostream>
#include <vector>

using namespace std;

int tab[10], n, t;
string s;

vector<int> wek;

int main()
{
	ios_base::sync_with_stdio(0);
	cin>>n;
	for (int i = 1; i <= n; i++){
		cin>>s;
		for (int j = 0; j < s.size(); j++){
			if (s[j] == '-') wek.push_back(j);
		}
		wek.push_back(s.size() + 2);
		
		int wynik = 0;
		for (int j = 1; j < wek.size(); j++){
			if (wek[j - 1] + 1 != wek[j]) wynik += 2;
		}
		if (wek[0] == 0) wynik--;
		cout<<"CASE #"<<i<<": "<<wynik<<"\n";
		wek.resize(0);
	}
	return 0;
}
