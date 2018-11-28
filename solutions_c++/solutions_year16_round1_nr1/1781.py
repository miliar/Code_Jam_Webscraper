#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <vector>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <climits>
#include <cstdio>
#include <set>
#include <unordered_map>
#include <iomanip>
using namespace std;
#define db(a) (cout << (#a) << " = " << (a) << endl)
typedef long long ll;

string foo(string in)
{
	if(in.size() <= 1) return in;
	char maxc = 0;
	size_t maxi = 0;
	for(size_t i=0;i<in.size();i++)
	{
		if(maxc <= in[i])
		{
			maxc = in[i];
			maxi = i;
		}		
	}
//db(in);db(maxc);db(maxi);	
	string out = in[maxi] + foo(in.substr(0, maxi)) + in.substr(maxi+1);
	return out;
}

int main()
{
  ios_base::sync_with_stdio(false);
	int N;
	cin>>N;
	for(int n=0;n<N;n++)
	{
		string in;
		cin>>in;
		cout << "Case #" << n+1 << ": " << foo(in) << "\n";
	}
  return 0;
}
