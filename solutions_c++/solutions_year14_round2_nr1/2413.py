#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
using namespace std;

int main(){
	ofstream ofs("output.txt"); ifstream ifs("A-small-attempt1.in");
	int T ; ifs >> T ;
	for(int i=1;i<=T;++i){
		int N ; ifs >> N ;
		string str[100]; for(int j=0;j<N;++j) ifs >> str[j];
		pair<char, int> p[2][100];
		int ite[2]={0};
		for(int k=0;k<2;++k){
			for(int l=0;l<str[k].size();++l){
				int r=l;
				while(r+1<str[k].size() && str[k][l]==str[k][r+1]) ++r;
				p[k][ite[k]++]=pair<char, int>(str[k][l],r-l+1);
				l=r;
			}
		}
		int cnt=0; bool failed=false;
		if(ite[0]!=ite[1]) failed=true;
		else {
			for(int j=0;j<ite[0];++j){
				if(p[0][j].first!=p[1][j].first) { failed=true; break;}
				else cnt+=abs(p[0][j].second-p[1][j].second);
			}
		}
		ofs << "Case #" << i << ": " ;
		if(failed) ofs << "Fegla Won\n" ;
		else ofs << cnt << '\n' ;
	}
}