#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <math.h>
using namespace std;

typedef vector<size_t> vi;
typedef vector<vi> vvi;
typedef unsigned long long ll;
typedef vector<ll> vll;
typedef pair<size_t,size_t> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef vector<double> vd;
typedef vector<string> vs;

string solve(size_t X, vi &S)
{
	sort(S.begin(), S.end());
	deque<size_t> Q(S.begin(), S.end());
	
	size_t count = 0;
	while(! Q.empty()) {
		size_t large = Q.back();
		Q.pop_back();
		if (! Q.empty()) {
			size_t small = Q.front();
			if (small + large <= X) {
				Q.pop_front();
			}
		}
		count ++;
	}

	char answer[50];
	sprintf(answer, "%u", count);
	return answer;
}

void preprocess(){}

void readinput(size_t &X, vi &S)
{
	size_t N;
	cin>>N>>X;
	S.resize(N);
	for (size_t i = 0; i < N; i ++) {
		cin>>S[i];
	}
}

vs getoutput()
{
	size_t X;
	vi S;
	readinput(X, S);
	string answer = solve(X, S);
	return vs(1, answer);
}

void main()
{
//	freopen("in.txt", "r", stdin); freopen("out.txt", "w", stdout);
//	freopen("test\\A-small-attempt0.in", "r", stdin);freopen("test\\A-small-attempt0.out", "w", stdout);
	freopen("test\\A-large.in", "r", stdin);freopen("test\\A-large.out", "w", stdout);
	size_t testcase;
	cin>>testcase;
	preprocess();
	for(size_t i = 1; i <= testcase; i ++)
	{
		cout<<"Case #"<<i<<": ";
		vs answer = getoutput();
		for(size_t j = 0; j < answer.size(); j ++)
			cout<<answer[j]<<endl;
	}
	fclose(stdin);
	fclose(stdout);
}