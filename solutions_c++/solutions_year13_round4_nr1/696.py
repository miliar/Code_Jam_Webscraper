#include <iostream>
#include <algorithm>
#include <vector>
#include <tuple>
#include <stack>
#include <cassert>

typedef uint64_t Z;

const Z modu = 1000002013;

Z N;
Z cost(Z len) {
	return len * N - len * (len - 1) / 2;
}

struct Event {
	Z pos;
	enum { in, out } dir;
	Z p;
	bool operator<(const Event& other) const {
		if(pos == other.pos) {
			return dir < other.dir;
		} else {
			return pos < other.pos;
		}
	}
};

int main() {
	Z T;
	std::cin >> T;
	for(Z t = 0; t < T; ++t) {
		Z M;
		std::cin >> N >> M;
		
		Z legit_cost = 0;
		std::vector<Event> events;
		for(Z i = 0; i < M; ++i) {
			Z o, e, p;
			std::cin >> o >> e >> p;
			events.push_back(Event{o, Event::in, p});
			events.push_back(Event{e, Event::out, p});
			legit_cost += ((cost(e - o) % modu) * p) % modu;
			legit_cost %= modu;
		}
		std::sort(events.begin(), events.end());
		
		Z cheat_cost = 0;
		std::stack<std::pair<Z, Z>> cards;
		for(const Event& e : events) {
			if(e.dir == Event::in) {
				cards.push(std::make_pair(e.pos, e.p));
			} else {
				Z p = e.p;
				while(p != 0) {
					Z take = 0;
					Z from = cards.top().first;
					if(cards.top().second > p) {
						cards.top().second -= p;
						take = p;
					} else {
						take = cards.top().second;
						cards.pop();
					}
					p -= take;
					cheat_cost += ((cost(e.pos - from) % modu) * take) % modu;
					cheat_cost %= modu;
				}
			}
		}
		assert(cards.empty());
		std::cout << "Case #" << (t + 1) << ": " << (modu + legit_cost - cheat_cost) % modu << "\n";
	}
	
	return 0;
}
