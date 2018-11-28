#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <string>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define FN "gcj1b_a"

int main()
{
	
	ifstream in(FN ".in");
	ofstream out(FN ".out");

	int t;
	in >> t;
	for(int i = 0; i < t; i++)
	{
		out << "Case #" << (i+1) << ": ";
		 int a,n;
		 in >> a >> n;
		 map<int,int> rest;
		 for(int j = 0; j < n; j++)
		 {
			 int c;
			 in >> c;
			 rest[c]++;
		 }
		 for(auto it = rest.begin(); it != rest.end(); ++it)
		 {
			 if(it->first >= a)
				 break;

			 a += it->first*it->second;
		 }
		 while(!rest.empty() && rest.begin()->first < a)
			 rest.erase(rest.begin());
		 if(a == 1)
		 {
			 out << n << "\n";
			 continue;
		 }
		 if(rest.empty())
		 {
			 out << "0\n";
			 continue;
		 }
		 int remove_ops = 0;
		 int add_ops = 0;
		 for(auto it = rest.begin(); it != rest.end(); ++it)
			 remove_ops += it->second;
		 int best_ops = remove_ops;
		 while(remove_ops) {
			 while(a <= rest.begin()->first)
			 {
				 add_ops++;
				 a += a-1;
			 }
			 while(!rest.empty() && rest.begin()->first < a)
			 {
				a += rest.begin()->first*rest.begin()->second;
				remove_ops -= rest.begin()->second;
				rest.erase(rest.begin());
			 }
			 if(remove_ops+add_ops < best_ops)
				 best_ops = remove_ops+add_ops;
		 }
		 out << best_ops << "\n";
	}

	out.close();
	return 0;
}