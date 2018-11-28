#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <string>
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
#include <cstring>
#include <fstream>

using namespace std;

int INF = 1E9;


int main() {
	freopen("B-large.in", "r", stdin);
	ofstream fout;
	fout.open("answer.out");

	int T;
	cin>>T;

	for(int Case = 1; Case <= T; Case++){
		fout<<"Case #"<<Case<<": ";
		//fout<<endl;
		string pc;
		cin>>pc;
		int l = pc.length();
		int cnt = 0;
		char ch = 'a';
		for(int i = 0; i < l; i++)
			if(pc[i] != ch){
				cnt++;
				ch = pc[i];
			}
		if(cnt == 1 && ch == '-'){
			fout<<1<<endl;
			continue;
		}
		if(ch == '+') cnt--;
		fout<<cnt<<endl;
		//fout<<endl;
	}
	return 0;
}
