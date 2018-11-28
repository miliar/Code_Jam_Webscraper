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

std::vector<int> p;

void Solve(int tc)
{
	int n;
	cin >> n;
	p.resize(n);
	int s=0;
	for(auto &pp: p)
	{
		cin >> pp;
		s+=pp;
	}
	printf("Case #%d: ", tc);
	while(s>0)
	{
		auto i=std::max_element(p.begin(), p.end());
		--*i;
		--s;
		if(s==2)
		{
			printf("%c ", 'A'+(int)(i-p.begin()));
			continue;
		}
		auto j=std::max_element(p.begin(), p.end());
		--*j;
		--s;
		printf("%c%c ", 'A'+(int)(i-p.begin()), 'A'+(int)(j-p.begin()));
	}
	printf("\n");
}

int main()
{
	int t;
	cin >> t;
	for(int tc=1; tc<=t; ++tc)
	{
		Solve(tc);
	}
}