#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
void reads (vector<vector<int> > &v)
{
	v.resize(4,vector<int>(4));
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			cin >> v[i][j];
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("outputGoogleJam.txt","w",stdout);
	vector<vector<int> > s1,s2;
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int q1;
		cin >> q1;
		q1--;
		reads (s1);
		int q2;
		cin >> q2;
		q2--;
		reads (s2);
		vector <int> res(4);
		sort(s1[q1].begin(),s1[q1].end());
		sort (s2[q2].begin(),s2[q2].end());
		vector<int>::iterator it;
		it = set_intersection (s1[q1].begin(),s1[q1].end(),s2[q2].begin(),s2[q2].end(),res.begin());
		res.resize(it - res.begin()); 
		printf ("Case #%d: ",i + 1);
		if (res.size() == 1)
			printf ("%d\n",res[0]);
		else if (res.size() > 1)
			printf ("Bad magician!\n");
		else
			printf ("Volunteer cheated!\n");
	}
	return 0;
}