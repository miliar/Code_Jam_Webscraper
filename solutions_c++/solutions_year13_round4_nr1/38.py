#include <cstdio>
#include <queue>
#include <algorithm>
#include <vector>

struct ele_t{

	int type;
	int val, num;

	ele_t(int ntype, int nval, int nnum): type(ntype), val(nval), num(nnum){}

	bool operator < (const ele_t& cmp) const{
		return val == cmp.val? type < cmp.type: val < cmp.val;
	}

};

struct heap_t{

	int val, num;

	heap_t(int nval, int nnum): val(nval), num(nnum){}

	bool operator < (const heap_t& cmp) const{
		return val < cmp.val;
	}

};

int main(){

	int T;
	scanf("%d" ,&T);
	for(int t = 1; t <= T; t++){

		printf("Case #%d: " ,t);

		int n, m;
		__uint128_t cst = 0;
		std::vector<ele_t> vec;
		scanf("%d %d" ,&n ,&m);
		for(int i = 0; i < m; i++){
			int s, e, p;
			scanf("%d %d %d" ,&s ,&e ,&p);
			vec.push_back(ele_t(0, s, p));
			vec.push_back(ele_t(1, e, p));
			__uint128_t _cst = (long long)(n + n - (e - s - 1)) * (e - s) / 2;
			cst += _cst * p;
		}
		std::sort(vec.begin(), vec.end());
		//printf("-- %lld\n" ,cst);

		__uint128_t ans = 0;
		std::priority_queue<heap_t> heap;
		for(int i = 0; i < vec.size(); i++){
			//printf("-- %d %d\n" ,vec[i].type ,vec[i].val);

			if(vec[i].type == 0){
				heap.push(heap_t(vec[i].val, vec[i].num));
				continue;
			}

			int R = vec[i].val;
			while(vec[i].num > 0){

				heap_t now = heap.top(); heap.pop();

				int sub = std::min(now.num, vec[i].num);
				int L = now.val;

				__uint128_t _cst = (long long)(n + n - (R - L - 1)) * (R - L) / 2;
				ans += _cst * sub;

				vec[i].num -= sub;
				if((now.num -= sub) > 0) heap.push(now);

			}

		}

		long long rans = (cst - ans) % 1000002013;
		printf("%lld\n" ,rans);

	}

}

