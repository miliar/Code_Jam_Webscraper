// ConsoleApplication1.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"
#include<iostream>
#include<cstdio>
#include<fstream>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
#include<sstream>
#include<string>
#include<iterator>
#include<functional>
#include<time.h>
#include<iomanip>
#include<queue>
#include<utility>
#include<array>

#include <limits>
using namespace std;
typedef long long int ll;
typedef long double ld;
#define INF 100000000000000000LL

ll diff(ll a, ll b)
{
	return a > b ? a - b : b - a;
}
/*
#define COMB_NUM 3001L
ld comb[COMB_NUM][COMB_NUM];
//need init_comb();
void init_comb()
{
	comb[0][0] = 1;
	ll i, j;
	for (i = 1; i < COMB_NUM; i++)
	{
		comb[i][0] = comb[i][i] = 1;
		for (j = 1; j < i; j++)
			comb[i][j] = comb[i - 1][j] + comb[i - 1][j - 1];
	}
}
*/

#define print(a)      for(int i=0;i<a.size();i++) cout<<a[i]<<" "; cout<<endl;
#define print2n(a,n)      for(int i=0;i<=n;i++) cout<<a[i]<<" "; cout<<endl;

void llFromString(const string &s, ll &a, ll &b)
{
	string replacedString = s;
	replace_if(replacedString.begin(),
		replacedString.end(),
		bind2nd(equal_to<char>(), '.'),
		' ');

	istringstream buffer(replacedString);
	buffer >> a;
	if (buffer.good())
	{
		buffer >> b;
	}
	else
	{
		b = 0;
	}
}


template<class T>
vector<T> split(const std::string &s) {

	string replacedString = s;
	replace_if(replacedString.begin(),
		replacedString.end(),
		bind2nd(equal_to<char>(), '.'),
		' ');

	vector<T> ret;
	istringstream buffer(replacedString);
	copy(istream_iterator<T>(buffer),
		istream_iterator<T>(), back_inserter(ret));
	return ret;
}// vector<ll> k = split<ll>(s);

ll N, J;
vector<ll> ps, ms;
ll p[3], m[3];
string t, ans;
vector<string> anss;


void run(ll n, ll i, ll j) {
	if (j == n) {
		ans = t;
		for (int I = 0; I < n; I++) {
			ans[ps[p[I]]] = '1';
			ans[ms[m[I]]] = '1';
		}
		anss.push_back(ans);
			
		if (anss.size() >= J) return;
	}
	else if (i != n) {
		ll start = 0;
		if (i != 0) start = p[i - 1]+1;
		for (int I = start; I < ps.size(); ++I) {
			p[i] = I;
			run(n, i + 1, j);
			if (anss.size() >= J) return;
		}
	}
	else {
		ll start = 0;
		if (j != 0) start = m[j - 1] + 1;
		for (int I = start; I < ms.size(); ++I) {
			m[j] = I;
			run(n, i, j+1);
			if (anss.size() >= J) return;
		}
	}
}

int main()
{
	fstream in, out;
	in.open("test.in.txt", ios::in);
	out.open("test.out.txt", ios::out);
	istream& input = in;
	ostream& output = out;
	//in.open("A-small-attempt0.in",ios::in); out.open("A-small-0.out",ios::out);
	//  in.open("A-large.in",ios::in); out.open("A-large-0.out",ios::out);


	ll case_id, total_case;

	input >> total_case;
	ll I, H, K, ans;

	for (case_id = 1; case_id <= total_case; case_id++)
	{
		input >> N >> J;
		t = "1";
		for (I = 1; I < N-1; I++) t = t + "0";
		t = t + "1";
		for (I = 0; 2 * I + 2  < N; I++) {
			ms.push_back(2 * I + 1);
			ps.push_back(2 * I + 2);
		}
		//output << fixed;
		//output.precision(10);
		output << "Case #" << case_id << ": ";
		output << endl;
		//output << ans;
		run(1, 0, 0);
		run(2, 0, 0);
		for (I = 0; I < J; I++) {
			output << anss[I];
			for (H = 3; H <= 11; H++) output << " " << H;
			output << endl;
		}
	}
	return EXIT_SUCCESS;
}











