#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

int worst, num, M;
vector<string> s;

void calc(vector<int>& serv)
{	
	vector<set<string> > S(M);
	for (int i = 0; i < serv.size(); ++i)
	{
		string& t = s[i];
		for (int j = 1; j <= t.size(); ++j)
			S[serv[i]].insert(t.substr(0, j));
	}
	int res = M;
	for (int i = 0; i < M; ++i)
	{
		if (S[i].size() == 0)
			return;
		res += S[i].size();
	}
//	cerr<<res<<endl;
	if (res > worst)
	{
		worst = res;
		num = 1;
	}
	else if (res == worst)
		++num;
}

void search(int nword, vector<int>& serv)
{
	if (nword == serv.size())
	{
		calc(serv);
		return;
	}
	for (int i = 0; i < M; ++i)
	{
		serv[nword] = i;
		search(nword + 1, serv);
	}
}

pair<int, int> solve()
{
	num = worst = -1;
	vector<int> serv(s.size(), 0);
	search(0, serv);
	return make_pair(worst, num);
}

int main()
{
	int T, N;
	cin>>T;
	vector<pair<int, int>> res(T);
//	#pragma omp parallel for
	for (int i = 0; i < T; ++i)
	{
		cerr<<i<<endl;
		cin>>N>>M;
		s.resize(N);
		for (int j = 0; j < N; ++j)
			cin>>s[j];
		res[i] = solve();
	//	cout<<"Case #"<<(i+1)<<": "<<res.first<<" "<<res.second<<endl;
	}
	for (int i = 0; i < T; ++i)
		cout<<"Case #"<<(i+1)<<": "<<res[i].first<<" "<<res[i].second<<endl;
	return 0;
}

