#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

#define SIZE 4

int main(int argc, char *argv[])
{
    int T;
    int first[SIZE][SIZE], first_ans;
    int second[SIZE][SIZE], second_ans;
    set<int> s;

    scanf("%d", &T);
    for (int k = 1; k <= T; ++k) {
        scanf("%d", &first_ans);
        --first_ans;
        for (int i = 0; i < SIZE; ++i) {
            for (int j = 0; j < SIZE; ++j) {
                scanf("%d", &first[i][j]);
            }
        }
        scanf("%d", &second_ans);
        --second_ans;
        for (int i = 0; i < SIZE; ++i) {
            for (int j = 0; j < SIZE; ++j) {
                scanf("%d", &second[i][j]);
            }
        }

        for (int i = 0; i < SIZE; ++i) {
            for (int j = 0; j < SIZE; ++j) {
                if (first[first_ans][i] == second[second_ans][j]) s.insert(first[first_ans][i]);
            }
        }

        if (s.size() == 1) printf("Case #%d: %d\n", k, *s.begin());
        else if (s.size() == 0) printf("Case #%d: Volunteer cheated!\n", k);
        else printf("Case #%d: Bad magician!\n", k);

        s.clear();
    }

    return 0;
}
