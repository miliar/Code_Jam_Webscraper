#include <iostream>
#include <string.h>
#include <cstdlib>
#include <cmath>
#include <math.h>
#include <vector>

using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

#define max(a,b) a<b?b:a

vector<int> plan;

bool makePlan(int parties[26], int n)
{
	
	int remainded = 0;
	int maj = 0;
	for (int i = 0; i < n; i++) {
		remainded += parties[i];
		maj = max(maj, parties[i]);
	}
	
	// End Condition - Successful
	if (remainded == 0)
		return true;

	// End Condition - Unsuccessful
	if (maj > remainded / 2)
		return false;

	for (int i = 0; i < n; i++)
	{
		for (int j = -1; j < i; j++)
		{
			if ((parties[i] <= 0) || (j != -1 && parties[j] <= 0))
				continue;

			if (j == -1) // single choose
			{
				parties[i]--;
				plan.push_back(i);
				plan.push_back(1);
			}
			else
			{
				parties[i]--;
				parties[j]--;
				plan.push_back(i);
				plan.push_back(j);
				plan.push_back(2);
			}

			bool ret = makePlan(parties, n);
			if (ret == true)
				return true;

			plan._Pop_back_n(plan.back() + 1);

			if (j == -1) // single choose
			{
				parties[i]++;
			}
			else
			{
				parties[i]++;
				parties[j]++;
			}
		}
	}
}

int main(int argc, char** argv) {

	int T;
	cin >> T;
	int c = 1;
	while (T--) {

		int parties[26];
		int n;

		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> parties[i];

		
		makePlan(parties, n);

		cout << "Case #" << c++ << ": ";

		vector<int> vplan;
		while (plan.empty() == false) {
			int m = plan.back();
			plan.pop_back();

			int i = plan.back();
			plan.pop_back();
			vplan.push_back(i);

			if (m == 2){
				i = plan.back();
				plan.pop_back();
				vplan.push_back(i);
			}
			vplan.push_back(m);
		}

		while (vplan.empty() == false){
			int m = vplan.back();
			vplan.pop_back();
			char s[3] = { 0 };

			int i = vplan.back();
			vplan.pop_back();
			s[0] = 'A' + i;

			if (m == 2){
				i = vplan.back();
				vplan.pop_back();
				s[1] = 'A' + i;
			}

			cout << s << " ";
		}
		cout << endl;

	}

	return 0;
}
