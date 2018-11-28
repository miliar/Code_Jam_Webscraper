#include <iostream>
#include <set>
#include <map>
#include <string>
#include <vector>

using namespace std;

void exec_1(int M, vector<string> &str, map<int, int> &ans)
{
  set<string> t;
  for(int i = 0; i < M; ++i) {
	int sz = (int)str[i].size();
	for(int len = 0; len <= sz; ++len) t.insert( str[i].substr(0, len) );
  }
  ans[ (int)t.size() ]++;
}

void exec_2(int M, vector<string> &str, map<int, int> &ans)
{
  set<string> temp;

  if(0 == M) {
    ans[0] = 1;
    return;
  }

  int sz = (int)str[M-1].size();
  for(int len = 0; len <= sz; ++len) temp.insert( str[M-1].substr(0, len) );

  int upto = (int)(1U << (M-1));

  for(int i = 0; i < upto; ++i) {
    set<string> t[2]  = { temp };
    for(int j = 0, k = 1; j < M - 1; ++j, k *= 2) {
	  const int idx = !!(i & k);
	  int sz = (int)str[j].size();
	  for(int len = 0; len <= sz; ++len) t[idx].insert( str[j].substr(0, len) );
	}
    ans[ (int)t[0].size() + (int)t[1].size()] += 2;
  }
}

void exec_3(int M, vector<string> &str, map<int, int> &ans)
{
  int upto = (int)(1U << M);

  for(int i = 0; i < upto; ++i) {
    vector<string> strs[2];
    for(int j = 0, k = 1; j < M - 1; ++j, k *= 2) {
	  const int idx = !!(i & k);
	  strs[idx].push_back(str[j]);
	}
    map<int, int> anss[2];
	exec_2((int)strs[0].size(), strs[0], anss[0]); 
	exec_1((int)strs[1].size(), strs[1], anss[1]);
	for( map<int, int>::iterator it = anss[0].begin(); it != anss[0].end(); ++it) {
	  for( map<int, int>::iterator jt = anss[1].begin(); jt != anss[1].end(); ++jt) {
        ans[ it->first + jt->first ] += it->second * jt->second;
	  }
	}
  }
}

void exec_4(int M, vector<string> &str, map<int, int> &ans)
{
  set<string> temp;

  int upto = (int)(1U << M);

  for(int i = 0; i < upto; ++i) {
    vector<string> strs[2];
    for(int j = 0, k = 1; j < M - 1; ++j, k *= 2) {
	  const int idx = !!(i & k);
	  strs[idx].push_back(str[j]);
	}
    map<int, int> anss[2];
	exec_2((int)strs[0].size(), strs[0], anss[0]); 
	exec_2((int)strs[1].size(), strs[1], anss[1]);
	for( map<int, int>::iterator it = anss[0].begin(); it != anss[0].end(); ++it) {
	  for( map<int, int>::iterator jt = anss[1].begin(); jt != anss[1].end(); ++jt) {
        ans[ it->first + jt->first ] += it->second * jt->second;
	  }
	}
  }
}




int main()
{
  int T;
  cin >> T;
  for(int case_num = 1; case_num <= T; ++case_num) {
    map<int, int> ans;
    int N, M;
	cin >> M >> N;
	vector<string> str(M);

	for(int i = 0; i < M; ++i) cin >> str[i];

	ans.clear();
	switch(N) {
	case 1: exec_1(M, str, ans); break;
	case 2: exec_2(M, str, ans); break;
	case 3: exec_3(M, str, ans); break;
	case 4: exec_4(M, str, ans); break;
	}

	map<int, int>::reverse_iterator it = ans.rbegin();
	cout << "Case #" << case_num << ": " << it->first << ' ' << it->second << endl;
  }
  return 0;
}

