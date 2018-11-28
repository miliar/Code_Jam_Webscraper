#include <iostream>
#include <algorithm>
#include <functional>
#include <iterator>
#include <vector>
#include <queue>

bool is_end(const std::vector<unsigned> &v)
{
	auto itr = std::find_if(
		v.begin(), v.end(), 
		std::bind2nd(std::not_equal_to<unsigned>(), 0)
	);
	return itr == v.end();
}

int eat(std::vector<unsigned> &v)
{
	for(unsigned i=0; i<v.size(); ++i)
	{
		v[i] = (v[i] > 0) ? v[i] - 1 : 0;
	}
	return 0;
}

int lift(std::vector<unsigned> &v)
{
	std::sort(v.begin(), v.end(), std::greater<unsigned>());
	unsigned x = v[0] >> 1, y = v[0] - x;
	v[0] = y;
	v.push_back(x);
	return 0;
}

typedef std::pair< unsigned, std::vector<unsigned> > QueueType;
class QueueTypeCompare
{
public:
	bool operator()(const QueueType &a, const QueueType &b) const
	{
		return a.first > b.first;
	}
};

void debug(const std::vector<unsigned> &v)
{
	std::for_each(
		v.begin(), v.end(), 
		[](unsigned x){ std::cout << x << ' '; return x; }
	);
	std::cout << std::endl;
	return;
}

int bfs(const std::vector<unsigned> &v)
{
	std::priority_queue<QueueType, std::vector<QueueType>, QueueTypeCompare> q;
	q.push( QueueType(0, v) );
	
	while(!q.empty())
	{
		QueueType t = q.top(); q.pop();
		
		/*std::cout << t.first << '\t';
		debug(t.second);
		*/
		std::sort(t.second.begin(), t.second.end(), std::greater<unsigned>());
		if(is_end(t.second)) return t.first;
		
		{
			std::vector<unsigned> v1(t.second);
			eat(v1);
			q.push( QueueType(t.first+1, v1) );
		}
		
		{
			unsigned m = (t.second)[0];
			for(unsigned n=1; n<=m>>1; ++n)
			{
				std::vector<unsigned> v2(t.second);
				v2[0] = n;
				v2.push_back(m - n);
				q.push( QueueType(t.first+1, v2) );
			}
		}
	}
	
	return -1;
}

int main()
{
	unsigned T;
	std::cin >> T;
	
	for(unsigned t=0; t<T; ++t)
	{
		unsigned D;
		std::cin >> D;
		
		std::vector<unsigned> P(D);
		for(unsigned d=0; d<D; ++d)
		{
			std::cin >> P[d];
		}
		
		std::cout << "Case #" << (t+1) << ": " << bfs(P) << std::endl;
	}
	
	return 0;
}
