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
	freopen("A-large.in", "r", stdin);
	ofstream fout;
	fout.open("answer.out");

	int T;
	cin>>T;

	for(int Case = 1; Case <= T; Case++){
		fout<<"Case #"<<Case<<": ";
		//fout<<endl;
		int N;
		cin>>N;
		if(N == 0){
			fout<<"INSOMNIA"<<endl;
			continue;
		}
		set <long long> dig;
		long long n = 0;
		while(dig.size() != 10){
			n += N;
			long long t = n;
			while(t > 0){
				dig.insert(t % 10);
				t /= 10;
			}
		}
		
		fout<<n<<endl;
		//fout<<endl;
	}
	return 0;
}
