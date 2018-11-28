#include <iostream>
#include <map>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

void getSet(int &ans, vector<vector<int> > &cards)
{
	cin >> ans;
	ans = ans - 1;

	for(int i=0; i<4; i++)
	{
		vector<int> temp_row;

		for(int j=0; j<4; j++)
		{
			int temp;
			cin >> temp;

			temp_row.push_back(temp);
		}

		cards.push_back(temp_row);
	}

}

int main(int argc, char const *argv[])
{
	int T;

	cin >> T;

	for(int i=0; i<T; i++)
	{
		int ans1, ans2;

		vector<vector<int> > cards1, cards2;

		getSet(ans1, cards1);
		getSet(ans2, cards2);


		sort(cards1[ans1].begin(),cards1[ans1].end());
		sort(cards2[ans2].begin(),cards2[ans2].end());

		std::vector<int> overlap(4);
  		std::vector<int>::iterator it;

  		it = set_intersection(cards1[ans1].begin(), cards1[ans1].end(), 
  							  cards2[ans2].begin(), cards2[ans2].end(), 
  							  overlap.begin());
		overlap.resize(it-overlap.begin());


  		cout << "Case #" << (i+1) << ": ";

  		if(overlap.size()==0)
		{
			cout << "Volunteer cheated!" << endl;
		}
		else if(overlap.size()==1)
		{
			cout << overlap[0] << endl;
		}
		else
		{
			cout << "Bad magician!" << endl;
		}
	}

	return 0;
}