#include <bits/stdc++.h>
#define MAXN 20

using namespace std;

bool numbers[MAXN];

pair<int, int> getAnswer() {
    int t = 0, l = -1;

    for(int i = 1; i <= 16; ++i)
        if(numbers[i]) {
            ++t;
            l = i;
        }

    return make_pair(t, l);
}

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
     freopen("A-small-attempt0.out", "w", stdout);

   // ios_base::sync_with_stdio(0);
   // cin.tie(0);

    int t;
    cin >> t;

    for(int t1 = 1; t1 <= t; ++t1){
        printf("Case #%d: ", t1);
        fill(numbers, numbers + MAXN, true);
        for(int k = 0; k < 2; ++k) {
            int r;
            cin >> r;

            for(int i = 1; i <= 4; ++i)
                for(int j = 0; j < 4; ++j) {
                    int c;
                    cin >> c;

                    if(i != r)
                        numbers[c] = false;
                }
        }

        pair<int, int> answer = getAnswer();

        if(answer.first == 0)
            printf("Volunteer cheated!\n");
        else if(answer.first > 1)
            printf("Bad magician!\n");
        else
            printf("%d\n", answer.second);


    }

}
