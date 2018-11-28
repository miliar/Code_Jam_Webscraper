#include <cstdio>
#include <vector>
#include <queue>
#include <bitset>
#include <cinttypes>
#include <cstring>

using namespace std;

typedef unsigned int uint;

const uint PANCSTACK_MEM_HEIGHT = 32;
typedef bitset<PANCSTACK_MEM_HEIGHT> pancstack_t;
uint PANCSTACK_HEIGHT;

// template<typename Value>
// class pancstack_t_vector : public vector<Value> {
//   public:
// 	Value operator[](pancstack_t _n) { return vector<Value>::operator[](_n.to_ulong()); }
// };

uint fast_pow(uint n, uint ppow) {
    uint result = 1;
    while(ppow > 0) {
        if(ppow % 2 == 1) result = result*n;
        n = n*n;
        ppow /= 2;
    }
    return result;
}

vector<uint> dist;

char to_plus(bool arg) { return arg ? '+' : '-'; }

pancstack_t string2pancstack(const char *pancstack_str) {
	pancstack_t pancstack = 0;
	for(uint pos = 0; pos < PANCSTACK_HEIGHT; pos++)
		pancstack[pos] = pancstack_str[pos] == '+';
	return pancstack;
}

void pancstack2string(const pancstack_t pancstack, char *output) {
	for(uint pos = 0; pos < PANCSTACK_HEIGHT; pos++)
		output[pos] = pancstack[pos] ? '+' : '-';
	output[PANCSTACK_HEIGHT] = '\0';
}

pancstack_t flip_pancstack_part(pancstack_t pancstack, uint level) {
	if(level == 0) {
		// printf("no need to flip!\n");
		return pancstack;
	}
	if(level == 1) {
		// printf("level is 1 - changing %u from %c ", 0, to_plus(pancstack[0]));
		pancstack[0] = !pancstack[0];
		// printf("to %c\n", to_plus(pancstack[0]));
		return pancstack;
	}

	for(uint pos = 0; pos < level/2; pos++) {
		if(pancstack[pos] == pancstack[level-pos-1]) {
			// printf("swapping (%u, %c) with (%u, %c) -> ", pos, to_plus(pancstack[pos]), level-pos-1, to_plus(pancstack[level-pos-1]) );
			pancstack[pos] = pancstack[level-pos-1] = !pancstack[pos];
			// printf("(%u, %c); (%u, %c)\n", pos, to_plus(pancstack[pos]), level-pos-1, to_plus(pancstack[level-pos-1]));
		} else {

		}
	}
	if(level % 2 != 0) {
		// printf("level is odd - changing %u from %c ", level/2, to_plus(pancstack[level/2]));
		pancstack[level/2] = !pancstack[level/2];
		// printf("to %c\n", to_plus(pancstack[level/2]));
	}

	return pancstack;
}

struct PancstackQueueEntry {
	pancstack_t pancstack;
	uint my_dist;
	PancstackQueueEntry() { }
	PancstackQueueEntry(pancstack_t pancstack_, uint dist_) : pancstack(pancstack_), my_dist(dist_) { }
};

bool operator<(const PancstackQueueEntry &a, const PancstackQueueEntry &b) {
	return a.my_dist < b.my_dist;
}

uint find_fastest_transformation(pancstack_t start, pancstack_t end) {

	if(start == end) return dist[end.to_ulong()] = 0;

	priority_queue<PancstackQueueEntry> Q;

	dist[start.to_ulong()] = 0;
	Q.push(PancstackQueueEntry(start, dist[start.to_ulong()]));

	while(!Q.empty()) {

		pancstack_t pcstck = Q.top().pancstack;
		uint my_dist = Q.top().my_dist;
		Q.pop();

		char printt[32];
		pancstack2string(pcstck, printt);
		// printf("Queue(%u): %s\n", my_dist, printt);

		for(uint level = 1; level <= PANCSTACK_HEIGHT; level++) {
			pancstack_t next = flip_pancstack_part(pcstck, level);
			if(next != pcstck && my_dist + 1 < dist[next.to_ulong()]) {
				dist[next.to_ulong()] = my_dist + 1;
				if(next == end) break;
				pancstack2string(next, printt);
				// printf("\tAdding %s\n", printt);
				Q.push(PancstackQueueEntry(next, dist[next.to_ulong()]));
			}
		}

	}

	// puts("bye there");

	return dist[end.to_ulong()];
}

void flip_test(pancstack_t pcstck) {

	char buffer[101];
	pancstack2string(pcstck, buffer);
	printf("Oryginal  pancstack: %s\n", buffer);

	for(uint level = 0; level <= PANCSTACK_HEIGHT; level++) {
		pancstack_t next = flip_pancstack_part(pcstck, level);
		pancstack2string(next, buffer);
		printf("Level: %u, pancstack: %s\n", level, buffer);
	}
}

void test_suite() {

	printf("\n\nTEST NO. 1\n");
	PANCSTACK_HEIGHT = 2;
	flip_test(string2pancstack("-+"));

	printf("\n\nTEST NO. 2\n");
	PANCSTACK_HEIGHT = 4;
	flip_test(string2pancstack("--+-"));

	// printf("\n\nTEST NO. 3\n");
	// PANCSTACK_HEIGHT = 2;
	// char test3_buffer[101];
	// pancstack_t test3_pcstck = string2pancstack("-+");
	// pancstack2string(test3_pcstck, test3_buffer);
	// printf("%s (/\\)-> ", test3_buffer);
	// pancstack_t test3_pcstck_flip = flip_pancstack_part(test3_pcstck, 2);
	// pancstack2string(test3_pcstck_flip, test3_buffer);
	// printf("%s | %s\n", test3_buffer, test3_pcstck == test3_pcstck_flip ? "NONO!": "YES.");



	printf("\n\n");
}

void solve(uint case_num) {

	char pancakes_str[101];

	scanf("%s", pancakes_str);
	PANCSTACK_HEIGHT = strlen(pancakes_str);

	if(PANCSTACK_HEIGHT > 32) {
		printf("Case #%u: 42\n", case_num);
		return;
	}

	dist.clear();
	dist.resize(fast_pow(2, PANCSTACK_HEIGHT), 2147483642);

	pancstack_t pancstack = string2pancstack(pancakes_str);
	
	uint result = find_fastest_transformation(pancstack, pancstack_t( ( 1 << (PANCSTACK_HEIGHT) ) - 1) );

	printf("Case #%u: %u\n", case_num, result);

}

int main() {

	// test_suite();
	// return 0;

	uint t;
	scanf("%u", &t);
	for(uint i = 1; i <= t; i++) solve(i);

	return 0;
}