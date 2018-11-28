#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <map>
#include <sstream>
using namespace std;

typedef long long LL;
typedef unsigned int UINT32;

vector<string> nums;
vector<string> nums2;

int str2int(const string &s) {
  stringstream ss(s);
  int a;
  ss >> a;
  return a;
}

string int2str(int a) {
  stringstream ss;
  ss << a;
  return ss.str();
}

string pow(string s) {
  string ans(2*s.length()-1, 0);
  int i;
  for (i = 0; i<s.length(); ++i) {
    s[i] -= '0';
  }

  for (i = 0; i<s.length(); ++i) {
    if (s[i] == 0) continue;
    int c = 0;
    for (int j=0; j<s.length(); ++j) {
      int a = s[i]*s[j];
      ans[i+j] += a + c;
      c = ans[i+j]/10;
      ans[i+j]%=10;
    }
  }

  for (i = 0; i<s.length(); ++i) {
    s[i] += '0';
  }
  for (i = 0; i<ans.length(); ++i) {
    ans[i] += '0';
  }

  return ans;
}

bool isp(string &s) {
  for (int i=0, j=s.length()-1; i<j; ++i, --j) {
    if (s[i] != s[j]) return false;
  }
  return true;
}

void gen() {
  nums.push_back("1");
  nums.push_back("2");
  nums.push_back("3");
  nums.push_back("11");
  nums.push_back("22");
  nums2.push_back("1");
  nums2.push_back("4");
  nums2.push_back("9");
  nums2.push_back("121");
  nums2.push_back("484");
  int start = 3;
  for (int i=3; i<=50; ++i) {
    int end = nums.size();
    for (int j=start; j<end; ++j) {
      string s = nums[j];
      int len1 = (s.length()+1)/2;
      if (i&1) {
        for (char ch='0'; ch<='9'; ++ch) {
          string s1 = s.substr(0, len1) + ch;
          s1 += s.substr(len1, s.length() - len1);
          string s2 = pow(s1);
          if (!isp(s2)) break;
          nums.push_back(s1);
          nums2.push_back(s2);
        }
      } else {
        string s1 = s.substr(0, len1) + s[len1-1];
        s1 += s.substr(len1, s.length() - len1);
        string s2 = pow(s1);
        if (isp(s2)) {
          nums.push_back(s1);
          nums2.push_back(s2);
        }
      }
    }
    sort(nums.begin() + end, nums.end());
    sort(nums2.begin() + end, nums2.end());
    start = end;
  }
}

bool isge(string &a, string &b) {
  bool ret = a.length() > b.length() || a.length()==b.length() && a>=b;
  return ret;
}

string calc()
{
  string A, B;
  cin >> A >> B;
  int ans = 0;

  int size = nums2.size();

  for (int i = 0; i < size; ++i) {
    if (isge(nums2[i], A) && isge(B, nums2[i])) {
      ++ans;
    }
  }

  return int2str(ans);
}

bool isp(LL i) {
  stringstream ss;
  ss << i;
  string s = ss.str();
  for (int i = s.length() - 1, j=0; j < i; --i, ++j) {
    if (s[i] != s[j]) return false;
  }
  return true;
}

int main(void)
{
  // cout << "111" << ' ' << pow("111") << endl;
  //return 0;
  gen();
  /*
  for (int i = 0; i < nums.size(); ++i) {
    cout << nums[i] << ' ' << nums2[i] << endl;
  }
  return 0;
  */

  /*
  for (LL i = 1; i <= 1000000000; ++i) {
    if (isp(i) && isp(i*i)) {
      // nums.push_back(i*i);
      cout << i << ' ' << i*i << "LL," << endl;
    }
  }
  return 0;
  */

  // NOTE: if using getline() to read the input, the following two lines should be
  // added to read the line sepeartor in the first line. 
  string line;
  getline(cin, line);
	int N = str2int(line);

	for (int i=1; i<=N; ++i) {
		cout << "Case #" << i << ": " << calc() << endl;
	}

	return 0;
}
