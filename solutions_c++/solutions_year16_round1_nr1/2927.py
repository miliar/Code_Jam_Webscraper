#include <bits/stdc++.h>
 
#define LLI long long int
#define LD long double
#define PB push_back
#define MP make_pair
#define FORi(i, a, b) for(int i = a; i < b ; ++i)
#define FORd(i, a, b) for(int i = a; i > b ; --i)
 
using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");
	 
const LLI mod = 1e16;

int main(){
	int t;
	string s;
	deque<char> d;
	fin >> t;
	FORi(i,0,t){
		fin >> s;
		fout << "Case #" << i+1 << ": ";
		d.PB(s[0]);
		FORi(i,1,s.size()){
			if (d[0]>s[i])
				d.PB(s[i]);
			else
				d.push_front(s[i]);
		}
		FORi(i,0,d.size())
			fout << d[i];
		d.clear();
		fout << endl;
	}
	fin.close();
	fout.close();
}
