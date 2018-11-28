#include<iostream>
#include<string>
#include<vector>
#include<utility>
#include<algorithm>
#include<functional>
using namespace std;

int main(){
    int T;
    string S;
    cin >> T;
    for(int t=1; t<=T; ++t){
	cin >> S;
	vector< pair<int, int> > ss;
	for(int i=0; i<S.length(); ++i){
	    ss.push_back(make_pair(S[i], i));
	}
	sort(ss.begin(), ss.end(), greater< pair<int, int> >());
	vector<int> inds;
	inds.push_back(ss[0].second);
	int lastl = ss[0].second;
	for(int i=1; i<S.length(); ++i){
	    if(ss[i].second < lastl){
		inds.push_back(ss[i].second);
		lastl = ss[i].second;
	    }
	}
	string res = "";
	for(int i=0; i<inds.size(); ++i){
	    res += S[inds[i]];
	}
	for(int i=inds.size()-1; i>0; --i){
	    for(int j=inds[i]+1; j<inds[i-1]; ++j){
		res += S[j];
	    }
	}
	for(int j=inds[0]+1; j<S.length(); ++j){
	    res += S[j];
	}
	cout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}
