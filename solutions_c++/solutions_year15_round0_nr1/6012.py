#include <cstring>
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
#include <memory.h>
#include <cassert>
#include <climits>

using namespace std;

#define case "Case #"

int main() 
{
	int t, stand = 0, ma, cno = 1;
	long ans = 0;
	string s;

	cin>>t;
	while(t--) {
		cin >> ma;
		cin>>s;
		stand = 0;
		ans = 0;
		for(int i = 0;i<=ma;i++) {
			if(s[i] != '0' && stand < i) {
				//cout<<"h " << i << "\n";
				ans += (i - stand);
				stand += (i - stand);
				stand += s[i] - '0';
			}
			else {
				//cout<<"h1 " << i << "\n";
				stand += s[i] - '0';
			}
			//cout<<ans<<" "<<stand<<endl;
		}
		cout<<case << cno++<<": "<<ans<<endl;
	}

	return 0;
}