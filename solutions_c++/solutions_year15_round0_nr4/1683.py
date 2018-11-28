#include<vector>
#include<string>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<stack>
#include<set>
#include<map>

using namespace std;

int main()
{
	ifstream in("./input.txt");
	ofstream out("./output.txt");
	cin.rdbuf(in.rdbuf());
	cout.rdbuf(out.rdbuf());
	int N;
	map<int, int> lMap;
	lMap[1] = 1;
	lMap[2] = 1;
	lMap[3] = 2;
	lMap[4] = 3;
	lMap[5] = 3;
	lMap[6] = 4;
	cin >> N;
	for (int t = 1; t <= N; ++t)
	{
		int x,r,c;
		cin>>x>>r>>c;
		if(r > c)
			swap(r,c);
		string res = "RICHARD";
		if(x < 7 && r >=  lMap[x] && ((r*c)%x == 0))
			res = "GABRIEL";
		cout<<"Case #"<<t<<": "<<res<<endl;
	}
}