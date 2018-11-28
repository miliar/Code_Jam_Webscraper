#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <fstream>
#include <cstring>

using namespace std;
typedef long long LL;

int main() {
	freopen("revenge_of_the_pancakes.in","r",stdin);
	freopen("revenge_of_the_pancakes.out","w",stdout);
	int tc, nt=1;
	cin>>tc;
	while (tc--) {
		string s;
		cin>>s;
		int ret=0;
		while (true) {
			int i=0;
			while (i<s.size() && s[i]==s[0]) i++;
			if (i==s.size()) break;
			for (int j=0;j<i;j++)
				if (s[j]=='+') s[j]='-';
				else s[j]='+';
			ret++;
		}
		cout<<"Case #"<<nt++<<": "<<ret+(s[0]=='-')<<endl;
	}
}
