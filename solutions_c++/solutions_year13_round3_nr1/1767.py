#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
#include<map>
#include<set>
#include<queue>
#include<deque>
#include<utility>
#include<string>
#include<sstream>
#include<cmath>
#include<list>
#include<new>

using namespace std;

#define tr(c, it) \
        for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)

#define all(c) (c).begin(),(c).end()

typedef long long int LLI;

LLI get_count(string s, LLI n, map<char,int>alpha){

	LLI len = s.size();
	vector< pair<LLI, LLI> >cons;
	LLI start = -1, cnt = 0;
	for(LLI i = 0; i < len; i++){

		if(start == -1 && alpha.find(s[i]) == alpha.end()){
			//cout << "start = i " << i << " cnt = " << cnt;
			start = i;
			cnt += 1;
		}

		else if(alpha.find(s[i]) == alpha.end()){
			cnt += 1;
		}

		else if(alpha.find(s[i]) != alpha.end()){
			start = -1;
			cnt = 0;
		}
	
		if(cnt == n){
			//cout << "first = " << start << " second = " << i << endl;
			cons.push_back(make_pair(start, i));
			start += 1;
			cnt -= 1;
		}	
	}		


	LLI ans = 0;
	for(LLI i = 0; i < len; i++){
		for(LLI j = 0; j < len; j++)
		{
			for(LLI k = 0; k < cons.size(); k++){
				if(cons[k].first >= i && cons[k].second <= j){
					ans += 1;
					break;
				}
			}	
		}
	
	}
	return ans;

}

int main()
{	
	int N;
	cin >> N;

	for(int i = 0; i < N; i++){

		string s;
		LLI n;

		map<char,int>alpha;
		alpha['a'] = 1;	
		alpha['e'] = 1;	
		alpha['i'] = 1;	
		alpha['o'] = 1;	
		alpha['u'] = 1;	

		cin >> s >> n;

		LLI ans = get_count(s,n,alpha);
	
		cout << "Case #" << i+1 << ": " << ans << endl;

	}

	return 0;
}
