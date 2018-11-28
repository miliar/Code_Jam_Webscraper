#include <cstdio>

int solve(const char* people, const int N);

int main() {
    int T;
    scanf("%d", &T);

    for (int i=0; i<T; ++i) {
	int Smax;
	char People[1000+1];
	scanf("%d %s", &Smax, People);
	printf("Case #%d: %d\n", i+1, solve(People, Smax+1));
    }

    return 0;
}

int solve(const char* people, const int N) {
    int upkeep = 0;
    int friends = 0;
    for (int i=0; i<N; ++i) {
	if (i > upkeep) {
	    const int diff = (i - upkeep);
	    friends += diff;
	    upkeep += diff;
	}
	upkeep += (people[i] - '0');
    }
    return friends;
}
