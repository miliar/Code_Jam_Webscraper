#include<vector>
#include<string>
#include<fstream>
#include<iostream>
#include<stack>
using namespace std;

int main()
{
	// ifstream in("./input.txt");
	// ofstream out("./output.txt");
	// cin.rdbuf(in.rdbuf());
	// cout.rdbuf(out.rdbuf());
	int N;
	cin >> N;
	for (int t = 1; t <= N; ++t)
	{
		
		int s;
		cin>>s;
		vector<int> shy;
		shy.resize(s+1);
		string inp;
		cin>>inp;
		for(int i=0;i<=s;++i)
			shy[i] = inp[i]-'0';
		int res = 0;
		long long sum = 0;
		for(int i=0;i<=s; ++i)
		{
			if(sum < i)
			{
				res += (i-sum);
				sum = i;
			}
			
			sum += shy[i];
		}
		cout<<"Case #"<<t<<": "<<res<<endl;

	}
}