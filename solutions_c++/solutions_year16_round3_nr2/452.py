#include <iostream>
#include <stdio.h>
#include <vector>
#include <memory>
#include <unordered_map>
#include <algorithm>
#include <string>

using namespace std;
using namespace std::string_literals;
namespace std
{
	template<typename C, typename V> auto find(C &Container, const V &Value) { return std::find(begin(Container), end(Container), Value); }
	template<typename C, typename P> auto find_if(C &Container, P Pred) { return std::find_if(begin(Container), end(Container), Pred); }
	template<typename C, typename P> auto find_if_not(C &Container, P Pred) { return std::find_if_not(begin(Container), end(Container), Pred); }
	template<typename C, typename P> auto all_of(C &Container, P Pred) { return std::all_of(begin(Container), end(Container), Pred); }
	template<typename C, typename P> auto any_of(C &Container, P Pred) { return std::any_of(begin(Container), end(Container), Pred); }
	template<typename C, typename P> auto none_of(C &Container, P Pred) { return std::none_of(begin(Container), end(Container), Pred); }
	template<typename C, typename P> auto count_if(const C &Container, P Pred) { return std::count_if(cbegin(Container), cend(Container), Pred); }
	template<typename C, typename V, typename P> auto lower_bound(C &Container, const V &Val, P Pred) { return std::lower_bound(begin(Container), end(Container), Val, Pred); }
	template<typename C, typename P> auto remove_if(C &Container, P Pred) { return std::remove_if(begin(Container), end(Container), Pred); }
	template<typename C, typename P> auto generate(C &Container, P Pred) { return std::generate(begin(Container), end(Container), Pred); }
}

std::vector<char> ones;
std::vector<char> zeroes;

void Solve(int tc)
{
	int64_t b, m;
	cin >> b >> m;
	if(b==2)
	{
		if(m!=1)
		{
			printf("Case #%d: IMPOSSIBLE\n", tc);
			return;
		}
		printf("Case #%d: POSSIBLE\n", tc);
		printf("01\n00\n");
		return;
	}
	if(m>(1i64<<(b-2)))
	{
		printf("Case #%d: IMPOSSIBLE\n", tc);
		return;
	}
	printf("Case #%d: POSSIBLE\n", tc);
	std::string res;
	if(m==(1i64<<(b-2)))
	{
		res="1";
		--m;
	}
	else
	{
		res="0";
	}
	for(auto i=b-3; i>=0; --i)
	{
		if(m&1)
		{
			res="1"s+res;
		}
		else
		{
			res="0"s+res;
		}
		m>>=1i64;
	}
	res="0"s+res;
	printf("%s\n", res.c_str());
	for(int64_t i=1; i<b; ++i)
	{
		printf("%.*s", (int) i+1, zeroes.data());
		if(i!=b-1)
		{
			printf("%.*s", (int) (b-(i+1)), ones.data());
		}
		printf("\n");
	}
}

int main()
{
	zeroes.resize(100, '0');
	ones.resize(100, '1');
	int t;
	cin >> t;
	for(int tc=1; tc<=t; ++tc)
	{
		Solve(tc);
	}
}