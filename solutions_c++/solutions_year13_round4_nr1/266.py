#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <ctime>
#include <queue>
using namespace std;
typedef long long llong;

const llong Mod = 1000002013;
struct Event{
	int time;
	int num;
	int flag;
	
	Event(){};
	Event(int time, int num, int flag):time(time), num(num), flag(flag){}

	bool operator <(const Event &e) const{
		return time != e.time ? time > e.time : flag < e.flag;
	}
};

const int MaxM = 1000;
int enter[MaxM], num[MaxM];
llong cost(int o, int e, int p, int N){
	llong ret = e - o;
	ret = (N + N - ret + 1) * ret / 2;
	return ret % Mod * p % Mod;
}
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int TT;
	scanf("%d", &TT);
	for(int cas = 1;cas <= TT; ++cas){
		int N, M;
		scanf("%d %d", &N, &M);
		
		llong ret = 0;
		priority_queue<Event> events;
		for(int i = 0;i < M; ++i){
			int o, e, p;
			scanf("%d %d %d", &o, &e, &p);
			events.push(Event(o, p, 1));
			events.push(Event(e, p, -1));
			ret = (ret + cost(o, e, p, N)) % Mod;
		}

		int tail = 0;
		while(!events.empty()){
			Event e = events.top();
			events.pop();
			if(e.flag > 0){
				enter[tail] = e.time;
				num[tail] = e.num;
				++tail;
			}
			else{
				int rem = e.num;
				while(rem > 0 && tail > 0){
					int leave = min(num[tail - 1], rem);
					ret = (ret - cost(enter[tail - 1], e.time, leave, N)) % Mod;
					ret = (ret + Mod) % Mod;
					rem -= leave;
					num[tail - 1] -= leave;
					if(num[tail - 1] == 0) -- tail;
				}
			}
		}
		printf("Case #%d: %lld\n", cas, ret);
	}
	return 0;
}
