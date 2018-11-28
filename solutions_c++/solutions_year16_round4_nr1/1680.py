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

int n, r, p, s;

void Solve(int tc)
{
	cin >> n >> r >> p >> s;
	switch(n)
	{
	case 1:
		if(r==2||p==2||s==2)
		{
			printf("Case #%d: IMPOSSIBLE\n", tc); 
			return;
		}
		if(p==1&&r==1)
		{
			printf("Case #%d: PR\n", tc);
			return;
		}
		if(p==1&&s==1)
		{
			printf("Case #%d: PS\n", tc);
			return;
		}
		printf("Case #%d: RS\n", tc);
		break;
	case 2:
		if(p==2&&r==1&&s==1)
		{
			printf("Case #%d: PRPS\n", tc);
			return;
		}
		if(p==1&&r==2&&s==1)
		{
			printf("Case #%d: PRRS\n", tc);
			return;
		}
		if(p==1&&r==1&&s==2)
		{
			printf("Case #%d: PSRS\n", tc);
			return;
		}
		printf("Case #%d: IMPOSSIBLE\n", tc);
		return;
	case 3:
		if(p==3&&r==3&&s==2)
		{
			printf("Case #%d: PRPSPRRS\n", tc);
			return;
		}
		if(p==3&&r==2&&s==3)
		{
			printf("Case #%d: PRPSPSRS\n", tc);
			return;
		}
		if(p==2&&r==3&&s==3)
		{
			printf("Case #%d: PRRSPSRS\n", tc);
			return;
		}
		printf("Case #%d: IMPOSSIBLE\n", tc);
		return;
	}
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