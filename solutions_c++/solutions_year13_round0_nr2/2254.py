#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>	//vector
#include <deque>	//deque
#include <list>	//list
#include <map>	//map,multimap
#include <set>	//set,multiset
#include <stack>	//stack
#include <queue>	//queue,priority_queue
#include <iterator>	//iterator,reverse_iterator,iterator_traits,insert_itreator,back_insert_iterator,front_insert_iterator
		//istream_iterator,ostream_iterator,istreambuf_iterator,ostreambuf_iterator
		//advance(),distance(),back_inserter(),front_inserter(),inserter()
#include <algorithm>	//<algorithm>
#include <numeric>	//accumulate,adjacent_difference,inner_product,partial_sum
#include <functional>	//plus,minus,multiplies,divides,modulus,negate
		//equal_to,not_equal_to,greater,greater_equal,less,less_equal
		//logical_and,logical_or,logical_not
		//bind_1st,bind_2nd,not1,not2
		//ptr_fun,mem_fun,mem_fun1,mem_fun_ref,mem_fun1_ref
#include <utility>	//pair,make_pair()
#include <memory>	//auto_ptr

using namespace std;

const int N=100+5;
const int M=100;
const string sza[2]={"YES","NO"};

multimap< int, pair<int,int> > a;
typedef multimap<int, pair<int, int> >::iterator mmapit;
int x[N][N];

int main()
{
	int tt,T;
	scanf("%d",&T);
	for(tt=1;tt<=T;tt++)
	{
		int i,j,k;
		int n,m;
		scanf("%d%d",&n,&m);
		a.clear();
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				scanf("%d",&x[i][j]);
				a.insert(make_pair(x[i][j],make_pair(i,j)));
			}
		}
		int uln[N]={0},ucl[N]={0};
		for(k=1;k<M;k++)
		{
			pair<mmapit,mmapit> itp;
			mmapit it;
			itp=a.equal_range(k);
			for(it=itp.first;it!=itp.second;++it)
			{
				ucl[(*it).second.second]++;
				uln[(*it).second.first]++;
			}
			for(it=itp.first;it!=itp.second;++it)
			{
				if(ucl[(*it).second.second]<n && uln[(*it).second.first]<m)
					break;
			}
			if(it!=itp.second)
				break;
		}
	
		printf("Case #%d: %s\n",tt,sza[k!=M].c_str());
	}
	return 0;
}
