#include <cstdio>
#include <algorithm> 
#include <vector>
#include <string>

using namespace std;

string get_string(char top, int levels){
	if(levels==0){
		return string(1,top);
	}
	string s1, s2;
	s1=get_string(top, levels-1);
	if(top=='R'){
		s2=get_string('S', levels-1);
	}
	if(top=='S'){
		s2=get_string('P', levels-1);
	}
	if(top=='P'){
		s2=get_string('R', levels-1);
	}
	if(s1<s2){
		return s1+s2;
	}
	else{
		return s2+s1;
	}
}

int main(){
	int t;
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		int n, r, p, s;
		scanf("%d %d %d %d",&n, &r, &p, &s);
		string rs=get_string('R', n);
		string ps=get_string('P', n);
		string ss=get_string('S', n);
		vector<string> ok;
		vector<string> cand={rs, ps, ss};
		for(auto& ss : cand){
			int cntr=0;
			int cntp=0;
			int cnts=0;
			for(auto c : ss){
				if(c=='R'){ cntr++; }
				if(c=='P'){ cntp++; }
				if(c=='S'){ cnts++; }
			}
			if(cntr!=r){continue;}
			if(cntp!=p){continue;}
			if(cnts!=s){continue;}
			ok.push_back(ss);
		}
		sort(ok.begin(), ok.end());
		printf("Case #%d: ", tc);
		if(ok.size()==0){
			printf("IMPOSSIBLE\n");
		}
		else{
			printf("%s\n", ok[0].c_str());
		}
	}
}
