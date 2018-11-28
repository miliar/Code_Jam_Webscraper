#include <stdio.h>
#include <map>
#include <string>
#include <cctype>
#include <algorithm>
#include <vector>
#include <string.h>
using std::map;
using std::string;
using std::vector;

vector<string> p;
map<string,int> mymap;
vector<int> set[20];

bool ori[2][200 * 1000];
bool tst[2][200 * 1000];

void parser(char* s){
	p.clear();
	while( 1 ){
		string tmp;
		while( isalpha(*s) ){
			tmp += *s;	
			++s;
		}
		p.push_back(tmp);
		if( *s ) ++s;
		else break;
	}
}

char buf[1000000];

int mcnt;

int find(string &s){
	map<string,int>::iterator it = mymap.find(s);
	if( it == mymap.end() ){
		//printf("%s = %d\n", s.c_str(), mcnt);
		return mymap[s] = mcnt++;
	}
	else
		return it->second;
}

int main(){
	int T;
	gets(buf);
	sscanf( buf, "%d", &T);
	for(int t=1;t<=T;++t){
		mymap.clear();
		for(int i=0;i<20;++i)
			set[i].clear();
		mcnt = 0;
		memset(ori,0,sizeof(ori));
		int n;
		gets(buf);
		sscanf( buf, "%d", &n);
		gets(buf);
		parser(buf);
		for(int i=0;i<p.size();++i)
			ori[0][find(p[i])] = 1;
		gets(buf);
		parser(buf);
		for(int i=0;i<p.size();++i)
			ori[1][find(p[i])] = 1;
		
		printf("Case #%d: ", t);
		
		if( n == 2 ){
			int ans = 0;
			for(int i=0;i<mcnt;++i)
				if( ori[0][i] && ori[1][i] )
					++ans;
			printf("%d\n", ans);
		} else {
			for(int i=0;i<n-2;++i){
				gets(buf);
				parser(buf);
				for(int j=0;j<p.size();++j)
					set[i].push_back(find(p[j]));
			}
			int ans = 2147483647;
			for(int i=0;i<1<<(n-2);++i){
				int cnt = 0;
				memset(tst[0], 0, sizeof(bool)*mcnt);
				memset(tst[1], 0, sizeof(bool)*mcnt);
				for(int j=0;j<n-2;++j)
					for(int k=0;k<set[j].size();++k)
						tst[ ((1<<j)&i) ? 0 : 1 ][set[j][k]] = 1;
				for(int j=0;j<mcnt;++j)
					if( (ori[0][j]||tst[0][j]) && (ori[1][j]||tst[1][j]) )
						//printf("%d added\n", j),
						++cnt;
				//printf("i = %d, cnt = %d\n", i, cnt);
				if( cnt < ans ) ans = cnt;
			}
			printf("%d\n", ans);
		}
	}
	return 0;	
}
