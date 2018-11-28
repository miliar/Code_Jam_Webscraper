#include <iostream>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <iomanip>
#include <sstream>

template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }

using namespace std;
char used[10] = {0};

void fill(long long num)
{
	stringstream ss;
	ss << num;
	string s;
	ss >> s;
	for(int i = 0; i < s.length(); i++)
		used[s[i]-'0'] = 1;
}

int main()
{
  int T;
  long long N;
  cin >> T;
  for(int t = 1; t <= T; t++)
  {
  	cout << "Case #"<<t << ": ";
  	cin >> N;
  	memset(used, 0, sizeof(used));
  	int temp = N;
  	while(true)
  	{
  		int sum = 0;
  		fill(temp);
  		for(int i = 0; i < 10; i++)
  			sum += used[i];
  		if (sum == 10)
  		{
  			cout << temp << endl;
  			break;
  		}
  		temp += N;
  		if (temp == N)
  		{
  			cout << "INSOMNIA\n";
  			break;
  		}
  		

  	}
  }


  return 0;
}