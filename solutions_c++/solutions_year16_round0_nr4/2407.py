#include<iostream>
#include<vector>

using namespace std;

int main()
{
	int T,t;
	cin >> T;

	t = 1;
	while (t <= T)
	{
		int K, C, S;
		cin >> K >> C >> S;

		vector<int> res_list;

		if (C == 1 || K == 1)
			res_list.push_back(1);
		
		for (int i = 1; i < K; i++)
			res_list.push_back(i + 1);

		cout << "Case #" << t << ": ";
		for (int i = 0; i < res_list.size(); i++)
			cout << res_list[i] << " ";
		cout << endl;
		t++;
	}
}