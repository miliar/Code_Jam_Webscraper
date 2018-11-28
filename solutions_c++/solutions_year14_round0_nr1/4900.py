#include<iostream>
#include<set>
using namespace std;



void Solve(int t)
{
	int a, b;
	set<int>set1;
	set<int>set2;

	int A[5][5];
	int B[5][5];

	cin >> a;

	for(int i = 1; i<=4; ++i)
		for(int j = 1; j<=4; ++j)
			cin >> A[i][j];

	for(int k = 1; k<=4; ++k)set1.insert(A[a][k]);

	cin >> b;

	for(int i = 1; i<=4; ++i)
		for(int j = 1; j<=4; ++j)
			cin >> B[i][j];

	for(int k = 1; k<=4; ++k)set2.insert(B[b][k]);

	set<int>setans;

	for(set<int>::iterator it = set2.begin(); it != set2.end(); ++it)
	{
		int to = *it;
		if (set1.count(to)) setans.insert(to);
	}
	
	cout << "Case #" << t << ": ";
	if (setans.size() == 1)cout << *setans.begin() << "\n";
	if (setans.size() == 0)cout << "Volunteer cheated!\n";
	if (setans.size() > 1) cout << "Bad magician!\n";

}

int main()
{
	freopen ("input.txt", "r", stdin );
	freopen("output.txt", "w", stdout);

	int T;
	cin>>T;

	for(int i = 1; i <= T; ++i)
	{
		Solve(i);
	}

}


