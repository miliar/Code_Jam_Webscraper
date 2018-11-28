#include <iostream>
#include <algorithm> 
#include <vector>
using namespace std;

int main() {
	// your code goes here
	int _T, idx;
	idx = 0;
	cin >> _T;
	while(idx < _T)
	{
		vector<double> naomi;
		vector<double> ken;
		int num = 0;
		cin >> num;
		for(int i = 0; i < num; i++)
		{
			double tmp;
			cin >> tmp;
			naomi.push_back(tmp);
		}
		for(int i = 0; i < num; i++)
		{
			double tmp;
			cin >> tmp;
			ken.push_back(tmp);
		}
		idx++;
		cout << "Case #" << idx << ": ";
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		int score1, score2;
		score1 = score2 = 0;
		int idxn, idxk;
		idxn = idxk = 0;
		while(idxn < num && idxk < num)
		{
			if(naomi[idxn] < ken[idxk])
			{
				idxn++;
			}else
			{
				score1++;
				idxn++;
				idxk++;
			}
		}
		idxn = idxk = 0;
		while(idxn < num && idxk < num)
		{
			if(naomi[idxn] < ken[idxk])
			{
				idxn++;	idxk++;
				score2++;
			}else
			{
				idxk++;
			}
		}
		score2 = num - score2;
		cout << score1 << " " << score2 << endl;
	}
	return 0;
}