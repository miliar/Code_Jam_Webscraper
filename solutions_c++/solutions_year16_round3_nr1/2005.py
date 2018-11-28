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

template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }

using namespace std;

int main()
{
  int T,N;
  cin >> T;
  int s[100];
  for(int t = 1; t <= T; t++)
  {
  	cout << "Case #"<<t<<":";
  	cin >> N;
  	memset(s, 0, sizeof(s));
  	int sum = 0;
  	for(int i = 0; i < N; i++)
  	{
  		cin >> s[i];
  		sum += s[i];
  	}
  	vector<int> res;
  	while(sum > 0)
  	{
  		cout <<" ";
  		res.clear();
  		int index = -1;
  		for(int i = 0; i < N; i++)
  		{
  
  			if (s[i] > s[index] || index == -1)
  				index = i;
  		}
  		res.push_back(index);
  		s[index]--;
  		sum--;
  		index = -1;
  		for(int i = 0; i < N; i++)
  		{
  		  	if (s[i] > s[index] || index == -1)
  				index = i;
  		}

  		if (s[index] > 0){
  			s[index]--;
  			res.push_back(index);
  			sum--;
  		}

  		index = -1;
  		for(int i = 0; i < N; i++)
  		{
  		  	if (s[i] > s[index] || index == -1)
  				index = i;
  		}
  		if(s[index]*2 > sum && res.size() == 2)
  		{
  			sum++;
  			s[res[1]]++;
  			res.pop_back();
  		}

  		for(int i = 0; i < res.size(); i++)
  			cout << char(res[i]+'A');


  	}	
  	cout << endl;
  	

  }

  return 0;
}