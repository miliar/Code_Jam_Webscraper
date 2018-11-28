#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

vector<int> edges[1000000];
int s[1000000];
int m[1000000];
int max_salary[1000000];
int min_salary[1000000];

void precompute(int v, int maxi, int mini) {
    maxi = max(maxi, s[v]);
    mini = min(mini, s[v]);

    max_salary[v] = maxi;
    min_salary[v] = mini;

    for (int i = 0; i < edges[v].size(); i++) {
        int w = edges[v][i];
        precompute(w, maxi, mini);
    }
}

int main() {
    int t;
    scanf("%d", &t);

    for (int z = 1; z <= t; z++) {
        int n, d;
        scanf("%d %d", &n, &d);

        for (int i = 0; i < n; i++)
            edges[i].clear();

        int a, c, r;
        scanf("%d %d %d %d", &s[0], &a, &c, &r);
        for (int i = 0; i+1 < n; i++)
            s[i+1] = ((long long)s[i] * a + c) % r;

        scanf("%d %d %d %d", &m[0], &a, &c, &r);
        for (int i = 0; i+1 < n; i++)
            m[i+1] = ((long long)m[i] * a + c) % r;

        for (int i = 1; i < n; i++)
            edges[m[i]%i].push_back(i);
        precompute(0, s[0], s[0]);

        vector<int> max_salaries, min_salaries;
        int bad = 0;
        for (int i = 0; i < n; i++) {
            if (max_salary[i] - min_salary[i] > d) {
                bad++;
                continue;
            }
            max_salaries.push_back(max_salary[i]);
            min_salaries.push_back(min_salary[i]);
        }

        sort(max_salaries.begin(), max_salaries.end());
        sort(min_salaries.begin(), min_salaries.end());

        int ans = 0;
        for (int i = 0; i < n; i++) {
            int low = s[i];
            int upper = s[i] + d;

            int lb = lower_bound(min_salaries.begin(), min_salaries.end(), low) - min_salaries.begin();
            int ub = max_salaries.end() - lower_bound(max_salaries.begin(), max_salaries.end(), upper+1);

            ans = max(ans, n - bad - lb - ub);
        }

        printf("Case #%d: %d\n", z, ans);
    }
}
