#include <iomanip>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <queue>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>

#define foreach(i,v) for(typeof((v).end())i=(v).begin();i!=(v).end();++i)

typedef std::vector< std::string > VS;
typedef std::vector<int> VI;
typedef long long ll;

using namespace std;

struct Asteroid {
    int x, y, z;
    int vx, vy, vz;
};

static
int sdist[1000][1000];

static
int dist[1000];

static
bool done[1000];

static
int sqr(int x)
{
    return x*x;
}

static
int sqdist(const Asteroid& a, const Asteroid& b)
{
    return sqr(a.x - b.x) + sqr(a.y - b.y) + sqr(a.z - b.z);
}

double solve(vector<Asteroid>& a, int S)
{
    int N = a.size();
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            sdist[i][j] = sqdist(a[i], a[j]);
    priority_queue<pair<int, int>> q;
    for (int i = 0; i < N; i++)
        dist[i] = 1 << 30;

    memset(done, 0, sizeof(done));
    q.push(make_pair(0, 1));

    while (!q.empty()) {
        pair<int, int> p = q.top();
        q.pop();
        if (done[p.second])
            continue;
        done[p.second] = true;
        if (p.second == 0)
            break;
        for (int i = 0; i < N; i++) {
            int newd = max(-p.first, sdist[p.second][i]);
            if (newd < dist[i]) {
                dist[i] = newd;
                q.push(make_pair(-newd, i));
            }
        }
    }

    return sqrt(dist[0]);
}

int main(int argc, const char* argv[]) {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, S;
        cin >> N >> S;
        vector<Asteroid> a(N);
        for (int i = 0; i < N; i++) {
            cin >> a[i].x >> a[i].y >> a[i].z >> a[i].vx >> a[i].vy >> a[i].vz;
        }
        printf("Case #%d: %.9f\n", t, solve(a, S));
    }
    return 0;
}
