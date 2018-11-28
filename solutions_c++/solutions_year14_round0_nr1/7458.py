#include <iostream> 
#include <algorithm> 
#include <vector> 
#include <queue>
#include <stack>
#include <string> 
#include <string.h> 
#include <fstream> 
#include <map> 
#include <iomanip> 
#include <cstdio> 
#include <cstdlib>
#include <cmath>
#include <deque>
#include <set>

using namespace std; 

const int MAX = 0x7FFFFFFF; 
const int MIN = 0x80000000; 

int main()
{
	int testcase ,count = 0; 
	freopen("A-small-attempt1.in", "r", stdin);
	ofstream fout("result.txt");
	cin >> testcase ; 
	while(testcase--)
	{
		count++ ; 
		int first, second, t ;
		vector<set<int>> magic1, magic2 ; 
		cin >> first ; 
		for(int i = 0; i < 4; i++)
		{
			set<int> temp ; 
			for(int j = 0; j < 4; j++)
			{
				cin >> t ; 
				temp.insert(t) ; 
			}
			magic1.push_back(temp) ; 
		}
		cin >> second ; 
		for(int i = 0; i < 4; i++)
		{
			set<int> temp ; 
			for(int j = 0; j < 4; j++)
			{
				cin >> t ; 
				temp.insert(t) ;
			}
			magic2.push_back(temp) ; 
		}
		vector<int> s ; 
		s.resize(10) ; 
		vector<int>::iterator it ; 
		it = set_intersection(magic1[first-1].begin(), magic1[first-1].end(), magic2[second-1].begin(), magic2[second-1].end(), s.begin()) ;
		s.resize(it - s.begin()) ; 
		fout << "Case #" << count << ": " ; 
		if(s.size() == 1)
		{
			it = s.begin() ; 
			fout << *it << endl ; 
		}
		else if(s.size() == 0)
			fout << "Volunteer cheated!" << endl ; 
		else
			fout << "Bad magician!" << endl ; 
	}
	fout.close() ; 
	return 0 ;
}