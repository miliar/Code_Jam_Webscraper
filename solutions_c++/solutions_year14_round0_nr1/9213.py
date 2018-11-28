#include<iostream>
#include<set>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	set<int> A[4];
	set<int> B[4];
	int T;
	cin >> T;
	vector<int> ans(8);
	for (int x=1;x<=T;x++)
	{
		int a,b;
		ans.clear();
		cin >> a;
		int q;
		for (int i=0;i<4;i++)
		{
			A[i].clear();
			for (int j=0;j<4;j++)
			{
				cin >> q;
				A[i].insert(q);
			}
		}
		cin >> b;
		for (int i=0;i<4;i++)
		{
			B[i].clear();
			for (int j=0;j<4;j++)
			{
				cin >> q;
				B[i].insert(q);
			}
		}
		cout << "Case #" << x << ": ";
		a--,b--;
		vector<int>::iterator it = set_intersection(A[a].begin(),A[a].end(),B[b].begin(),B[b].end(),ans.begin());
		if (it-ans.begin()==1) 
			cout << ans[0];
		else if (it-ans.begin()>1) 
			cout << "Bad magician!";
		else cout << "Volunteer cheated!";
		cout << endl;
	}
}