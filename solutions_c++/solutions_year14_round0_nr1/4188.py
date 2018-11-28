#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
void fun()
{
	vector<vector<int> > v(4, vector<int>(4, 0));
	string s[2] = {"Bad magician!", "Volunteer cheated!"};
	int T;
	cin >> T;
	int first_answer, second_answer;
	for(int i= 1; i <= T; ++i)
	{
		cin >> first_answer;
		for(int j = 0; j < 4; ++j)
			for(int k = 0; k < 4; ++k)
				cin >> v[j][k];
		vector<int> t1 = v[first_answer - 1];
		cin >> second_answer;
		for(int j = 0; j < 4; ++j)
			for(int k = 0; k < 4; ++k)
				cin >> v[j][k];
		vector<int> t2 = v[second_answer - 1];
		sort(t1.begin(), t1.end());
		sort(t2.begin(), t2.end());
		vector<int> t1_t2_intersection;
		int j = 0, k = 0;
		while(j < 4 && k < 4)
		{
			if(t1[j] < t2[k])
			{
				++j;
			}
			else if(t1[j] > t2[k])
			{
				++k;
			}
			else
			{
				t1_t2_intersection.push_back(t1[j]);
				++j;
				++k;
			}
		}
		cout << "Case #" <<i<<": ";
		if(t1_t2_intersection.size() == 1)
		{
			cout << t1_t2_intersection[0] <<endl;
		}
		else if(t1_t2_intersection.size() > 1)
		{
			cout << s[0] <<endl;
		}
		else
		{
			cout << s[1] <<endl;
		}
	}
}
int main()
{
	fun();
}
