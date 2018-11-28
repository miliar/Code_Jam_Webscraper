#include<iostream>
#include<cstdio>
using namespace std;
class koro	{
public:
	int ara[1010];
	int shy_level;
	void get_inp()	{
		cin >> shy_level;
		for (int i = 0; i <= shy_level; i++)	{
			scanf("%1d", &ara[i]);
			//cout << ara[i] << " ";
		}
		count();
	}
	void count()	{
		int number_of_person = 0;
		int ans = 0;
		for (int i = 0; i <= shy_level; i++)	{
			if (i > number_of_person)	{
				int temp_person = i - number_of_person;
				ans += temp_person;
				number_of_person += temp_person;
				/*ans++;
				number_of_person++;*/
			}
			number_of_person += ara[i];
		}
		cout << ans << "\n";
	}
};
int main()	{
	//freopen("A-small-attempt1 (1).in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int test_case;
	cin >> test_case;
	for (int i = 0; i < test_case; i++)	{
		cout << "Case #" << i + 1 << ": ";
		koro ob;
		ob.get_inp();
	}
	return 0;
}