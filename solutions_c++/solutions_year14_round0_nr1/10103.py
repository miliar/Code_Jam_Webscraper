
#include <cassert>
#include <iostream>
#include <vector>
#include <algorithm> 

using std::cin;
using std::cout;
using std::endl;
using std::vector;


struct T
{
	vector<vector<int>> arrangment;
	int ans;
};
void magic_trick(vector<T> t, int n)
{
	vector<int> ans;

	for (int j = 0; j < 4; ++j)
	{
		std::vector<int>::iterator it = std::find(t[1].arrangment[t[1].ans - 1].begin(), t[1].arrangment[t[1].ans - 1].end(), t[0].arrangment[t[0].ans - 1][j]);
		if (it != t[1].arrangment[t[1].ans-1].end())
		{
			ans.emplace_back(*it);
		}
	}
	
	if (ans.size() > 1)
	{
		cout << "Case #" << n << ": Bad magician!" << endl;
	}
	else if (ans.size() == 1)
	{
		cout << "Case #" << n << ": " << ans[0] << endl;
	}
	else
	{
		cout << "Case #" << n << ": Volunteer cheated!" << endl;
	}
}
int main() {

	int n = 0, a = 0, b = 0, c = 0, d = 0; 
	cin >> n;
	
	

	for (int i = 0; i < n; ++i)
	{
		vector<T> t;
		T u1;
		cin >> u1.ans;
		for (int j = 0; j < 4; ++j)
		{
			cin >> a >> b >> c >> d;
			u1.arrangment.emplace_back(vector<int>{ a, b, c, d });
		}
		t.emplace_back(u1);
		T u2;
		cin >> u2.ans;
		for (int j = 0; j < 4; ++j)
		{
			cin >> a >> b >> c >> d;
			u2.arrangment.emplace_back(vector<int>{ a, b, c, d });
		}
		t.emplace_back(u2);
		magic_trick(t, i+1);
	}

	return 0;
}