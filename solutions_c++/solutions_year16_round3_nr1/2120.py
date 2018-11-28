#include <vector>
#include <set>
#include <utility>
#include<cstdio>
#include <iostream>
using namespace std;

string append_to_ans(string ans, string a) {
	if (ans  == "") {
		return a;
		
	} else {
		return ans + " " + a;
	}
}
void print_set(set <pair <char, int> > S)
{
	for(set < pair <char, int> >::iterator it=S.begin();it!=S.end();++it) {
		printf("%c %d", (*it).first, (*it).second);
	}
	puts("");
	
}
int main()
{
	set < pair <char, int> > S;
	int tc, ti;
	int n;
	scanf("%d",&tc);
	for (ti =1;ti<=tc;++ti) {
		S.clear();
		int i,j;
		string ans = "";
		scanf("%d", &n);
		for (i=0;i<n;++i) {
			scanf("%d", &j);
			S.insert(make_pair('A'+i, j));
		}
		bool two_party = false;
		while(!S.empty()) {
			//print_set(S);
			
			int mx = 0,mxcount=0;
			set< pair <char, int> >::iterator mit;
			pair <char, int> p;
			for (set< pair <char, int> >::iterator it = S.begin();it !=S.end(); ++it) {
				
				p = *it;
				if (p.second ==mx) {
					mxcount++;
				} else if (p.second > mx) {
					mxcount =1;
					mit = it;
					mx=p.second;
				}
			}
			//printf("size %d mxount %d\n", S.size(), mxcount);
			p = *mit;
			if (S.size() == 2 && mxcount ==2) {
				//puts("Two party");
				two_party = true;
				break;
			} else {
				S.erase(mit);
				string temp = ""; temp += p.first;
				ans = append_to_ans(ans, temp);
				if (p.second > 1) {
					S.insert(make_pair(p.first, p.second -1));
				}
			}
			
		}
		if (two_party) {
			int mems=(*S.begin()).second;
			string step = "";
			for (set< pair <char, int> >::iterator it = S.begin();it !=S.end(); ++it) {
				step += (*it).first;
			}
			while(mems--) {
				ans = append_to_ans(ans, step);
			}
		}	
		cout<<"Case #"<<ti<<": "<<ans<<endl;
	}
	return 0;
}