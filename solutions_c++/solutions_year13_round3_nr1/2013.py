#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <cstring>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <fstream>

using namespace std;

int main() {

#ifndef ONLINE_JUDGE
	freopen("A-small-attempt0.in", "rt", stdin);
	  freopen("out.txt", "wt", stdout);
#endif

	int tc = 0, n = 0, count = 0, c = 0;
	string name;
	cin >> tc;
	map<pair<string ,int>, bool> vis;
	char arr[] = { 'a', 'e', 'i', 'o', 'u' };

	for (int i = 1; i <= tc; i++) {

		cin >> name >> n;
		int size = name.size();
		for (int x = 0; x < size; x++) {

			for (int y = 1; y <=  size   ; y++) {

				string tmp = name.substr(x , y );
				if((int)tmp.size() < n)continue;
				for (unsigned int f = 0; f < tmp.size(); f++) {
						if (find(arr , arr + 5 ,tmp[f]) == arr + 5) {
							c++;
						}
						else c = 0;

						if(c == n)break;
				}

				if (c == n && vis.find(make_pair(tmp , x)) == vis.end()) {

					vis[make_pair(tmp , x)] = true;
					count++;
				}
				c = 0;
			}

		}

		cout <<"Case #"<<i << ": "<< count << endl;
		count = 0;
		vis.clear();

	}

	/* if(find(arr , arr + 5 , name[x]) == arr + 5)count++;
	 else count = 0;

	 if(count == n){
	 ret+=1 + ((x + 1) - n) + (size - ((x + 1) ) );
	 count = 0;
	 }*/
	return 0;
}
//By : mohamed waleed
