#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

typedef unsigned long long ull;


bool comp(const pair<char, int>& firstElem, const pair<char, int>& secondElem) {
	return firstElem.second > secondElem.second;

}

int main()
{
	ofstream output;
	ifstream input;
	input.open("input.txt");
	output.open("output.txt");

	//	FILE * input;
	//	input = fopen("input.txt","r");

	int T;

	//	fread(&n, sizeof(int), 1, input);cout<<n<<endl; char cc=getchar();

	input >> T;// cout<<n<<endl;
	//cin >> T;
	
	int n;

	//string ans;
	int len;
	for (int t = 0; t < T; ++t)
	{
		input >> n ;
		int total = 0;
		vector<pair<char, int>> p(n);
		//pair<char, int>* p = new pair<char, int>[n];
		for (int i = 0; i < n; ++i)
		{
			input >> p[i].second;
			p[i].first = ('A' + i);
			total += p[i].second;
		}

		sort(p.begin(), p.end(), comp);

		output << "Case #" << t + 1 << ": ";


		while (p[1].second * 2 <= (total - 1 ))
		{
			output << p[0].first;
			p[0].second--;
			--total;
			if (p[0].second && p[1].second * 2 <= (total - 1))
			{
				output << p[0].first;
				p[0].second--;
				--total;
			}
			output << " ";
			sort(p.begin(), p.end(), comp);
		}

		while (p[0].second > 0)
		{
			output << p[0].first;
			p[0].second--;
			--total;
			
				output << p[1].first;
				p[1].second--;
				--total;
			
				output << " ";
				sort(p.begin(), p.end(), comp);
		}

		//output << res.first << ' ' << res.second;

		output << endl;

		//cout << ans;
		//delete[] p;
	}
	//	fclose(input);
	input.close();
	output.close();
	//	system("pause");
	return 0;
}
