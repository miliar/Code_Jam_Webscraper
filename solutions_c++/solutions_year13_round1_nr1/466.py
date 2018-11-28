#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <cmath>
#include <ctime>
#include <limits>
#include <iterator>
#include <bitset>
#define sz(m)((m).size())
#define all(a)a.begin(),a.end()
#define forn(i,n)for(int i=0,i##e=n;i<i##e;++i)
#define fori(i,m)forn(i,sz(m))
#define each(i,m)for(typeof(m.begin())i=m.begin(),i##e=m.end();i!=i##e;++i)
#define srt(s)sort(all(s))
#define dump(m)copy(all(m),ostream_iterator<typeof(m[0])>(cout,"\n"));cout<<endl
using namespace std;

int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int N;
	fin >> N;
	fout << "[";
	for (int cas = 0; cas < N; ++cas) {
		unsigned long long r, t;
		fin >> r >> t;
		fout << "(" << r << "," << t << ")" << (cas + 1 == N ? "" : ", ");
	}
	fout << "]";
}