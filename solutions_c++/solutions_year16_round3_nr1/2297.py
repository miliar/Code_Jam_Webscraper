#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct predicate
{
    bool operator()(const std::pair<int, int> &left, const std::pair<int, int> &right)
    {
         return left.first < right.first;
    }
};


void SolveCase(vector< pair<int,int> > parties)
{
	sort(parties.rbegin(), parties.rend(), predicate());

	
	vector<string> ans;
	
	while(1)
	{
		if(parties[0].first > parties[1].first + 1) {
			char a = 'A' + parties[0].second;
			string s = "" ;
			s += a;
			
			s += a;
			
			ans.push_back(s);
			
			parties[0].first -= 2;

		}
		else if(parties[0].first == parties[1].first+1)
		{
			
			if(parties[0].first > 2) {
		        char a = 'A' + parties[0].second;
				string s = "" ;
	   			s += a;

				char b = 'A' + parties[1].second;
				s += b;

				ans.push_back(s);

				parties[0].first -= 1;
				parties[1].first -= 1;
			}
			else
			{
				char a = 'A' + parties[0].second;
				string s = "" ;
				s += a;
				
				ans.push_back(s);

				parties[0].first -= 1;
			}

		}
		else {
			if(parties[0].first > 1) {
				char a = 'A' + parties[0].second;
				string s = "" ;
				s += a;

				char b = 'A' + parties[1].second;
				s += b;

				ans.push_back(s);

				parties[0].first -= 1;
				parties[1].first -= 1;
			}
			else
			{
				int num = parties.size();
				if(parties.size()&1) {
					char a = 'A' + parties[num-1].second;
					string s = "" ;
					s += a;
					ans.push_back(s);
					num--;
				}
				
				for(int i = 0; i < num; i+=2) {
					char b = 'A' + parties[i].second;
					string t = "" ;
					t += b;

					char c = 'A' + parties[i+1].second;
					t += c;

					ans.push_back(t);
				}
				
				break;
			}
		}
		
		sort(parties.rbegin(), parties.rend(), predicate());

	}
	
	for ( int i = 0; i < ans.size(); i++) {
		cout << ans[i] << " ";
	}
}

int main() 
{
	FILE *fin = freopen("A.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A.out", "w", stdout);
	
	int testCases;
	cin >> testCases;
	for(int t = 1; t <= testCases; t++)
	{
		int n;
		cin >> n;
		
		vector< pair<int,int> > parties;
		
		int senatorCnt;
		for(int i = 0; i < n; i++) {
  		    cin >> senatorCnt;
			parties.push_back(make_pair(senatorCnt, i));
		}

		cout << "Case #" << t << ": ";
		SolveCase(parties);
		cout << endl;
	}
	
	exit(0);
}
