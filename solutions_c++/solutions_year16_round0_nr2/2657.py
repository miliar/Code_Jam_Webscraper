#include <iostream>


using namespace std;

int main(){
	int t;
	cin >> t;
	string s;
	for (int i = 1; i <= t; ++i)
	{
		cin >> s;
		int cnt =0;
		for (int j = s.size()-1; j >= 0; --j)
		{
			if(s[j]=='-'){
				cnt++;
				for (int k = j-1; k >= 0; --k)
				{
					if(s[k]=='-')
						s[k]='+';
					else
						s[k]='-';

				}
			}
		}
		cout << "Case #" << i << ": " << cnt << endl;
	}
}