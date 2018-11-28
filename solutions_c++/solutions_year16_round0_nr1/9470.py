#include <iostream>
#include <algorithm>
#include <sstream>

using namespace std;

bool check[10];

string int2str(int v) {
  stringstream ss;
  ss << v;
  return ss.str();
}

long long int solve(int n)
{
  int count = 0;
  int tmp, tmp2;
  string s;
  fill(check, check+10, false);

  if(n == 0) {
    return -1;
  }

  for(int i = 1; ; i+=1){
    tmp = i * n;
    s = int2str(tmp);
    
    for(int j = 0; j < s.size(); j += 1) {
      tmp2 = (int)(s[j] - '0');
      if(!check[tmp2]) {
	check[tmp2] = true;
	count += 1;

	if(count == 10) {
	  return tmp;
	}
      }
    }
  }
  
  return -1;
}

int main()
{
  int tc;
  cin >> tc;

  int n;
  long long int result;
  for(int i = 1; i <= tc; i += 1) {
    cin >> n;
    result = solve(n);
    if(result == -1) {
      cout << "Case #" << i << ": INSOMNIA" << endl;
    } else {
      cout << "Case #" << i << ": " << result << endl;
    }
  }

  return 0;
}
