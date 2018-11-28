//#pragma comment(linker,"/STACK:200000000")
#pragma warning(disable:4996)
#include <iostream>
#include <sstream>
#include <fstream>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <utility>
#include <algorithm>
#include <numeric>
#include <functional>
//#include <unordered_map>
using namespace std;

int T;
string s;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("Ans.out","w",stdout);
	//ifstream fin("dict.out");
	//ofstream fout("Ans.out");
	//FILE *fin=fopen("table.txt","r");
	//FILE *fout=fopen("Ans.out","w");
	cin>>T;
	for(int cas=1;cas<=T;cas++){
		cin>>s;
		string tmp;
		for(int i=0;i<s.length();i++){
			if(tmp.empty() || s[i]!=tmp.back())
				tmp.push_back(s[i]);
		}
		if(tmp.back()=='+') tmp.pop_back();
		printf("Case #%d: %d\n",cas,tmp.length());
	}

	return 0;
}