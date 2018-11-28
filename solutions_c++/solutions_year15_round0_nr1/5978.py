#include<iostream>
#include<fstream>
#include<string>
#define re(i,j,k) for(int i=j;i<k;i++)
using namespace std;
int main(){
	ofstream fout("out.txt");
	ifstream fin("A-large.in");
	int t, d, g,a[20000],ans,max,max2,maxi;
	fin >> t;
	int c = 0;
	while (++c!=t+1){
		int n; string s;
		ans = 0;
		fin >> n >> s;
		d = 0;
		re(i, 0, n+1){
			if (i <= d) d += s[i] - '0';
			else if (s[i] - '0') { ans += i - d; d = i + s[i] - '0'; }
		}
		d++;
		fout << "Case #" << c <<": "<<ans<<endl;
	}
}