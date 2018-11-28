#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

int main()
{
	int T = 0;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		double price, rate, rateinc, total, answer;
		answer = 0;
		rate = 2;
		cin >> price;
		cin >> rateinc;
		cin >> total;
		while(true)
		{
			if ((total-price)/rate > total/(rate+rateinc) )
			{
				answer = answer + (price/ rate);
				rate = rate+rateinc;
			}
			else
			{
				answer = answer + (total/rate);
				break;
			}
		}
		cout << "Case #" << i << ": ";
		cout << setprecision(10) << answer << endl;
	}
	return 0;
}