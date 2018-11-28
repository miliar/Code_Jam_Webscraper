#include <cstdio>

#include <vector>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        int smax;
        scanf("%d", &smax);
        vector<int> people;
        char c;
        scanf("%c", &c);
        for (int j = 0; j <= smax; j++) {
            scanf("%c", &c);
            people.push_back(c - '0');
        }
        int needed = 0;
        int counter = 0;
        for (int j = 0; j <= smax; j++) {
            if (people[j] > 0 && counter < j) {
                needed += j - counter;
                counter = j;
            }
            counter += people[j];
        }
        printf("Case #%d: %d\n", i, needed);
    }
}