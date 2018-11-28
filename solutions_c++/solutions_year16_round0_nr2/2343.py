#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main(){
	//ifstream fin ("B-small-attempt0.in");
	//ofstream fout ("B-small-attempt0.out");
	ifstream fin ("B-large.in");
	ofstream fout ("B-large.out");
	int t,i,j,l,ans;
	string s;
	fin>>t;
	for(i=1;i<=t;++i){
		ans=0;
		fin>>s;
		l=s.length();
		if(l>1)
			for(j=1;j<l;++j)
				if(s[j]!=s[j-1])
					++ans;
		if(s[l-1]=='-')
			++ans;
		fout<<"Case #"<<i<<": "<<ans<<"\n";
	}
	return 0;
}
