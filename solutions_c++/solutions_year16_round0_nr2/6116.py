#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <stack>
#include <queue>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;

int main(){
	int T; cin>>T;
	for(int t=0;t<T;t++){
		string s; cin>>s;
		int flips = 0;
		for(int i=1;i<s.size();i++) if (s[i]!=s[i-1]) flips++;
		if (s.back()=='-') flips++;
		printf("Case #%d: %d\n",t+1, flips);
	}
}