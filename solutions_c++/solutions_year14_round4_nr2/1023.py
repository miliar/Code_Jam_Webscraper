#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <cfloat>
#include <cstring>
#include <ctime>
#include <cassert>

#define REP(k,a) for(int k = 0; k < (a); ++k)
#define FOR(k,a,b) for(int k=(a); k < (b); ++k)
#define FRE(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define SZ(x) ((int)((x).size()))
#define ALL(c) (c).begin(), (c).end()
#define CLR(c) memset((c), 0, sizeof(c))
#define VCLR(v) fill((v).begin(), (v).end(), 0)
#define PB push_back
#define MP make_pair
#define DBG(x) std::cerr << #x" = " << x << std::endl
#define I1 first
#define I2 second

const int INF = 2000000000;

using namespace std;

// typedef vector<int> VI;
typedef deque<int> VI;
typedef vector<vector<int> > VVI;
typedef vector<double> VD;
typedef vector<vector<double> > VVD;
typedef vector<string> VS;
typedef pair<int,int> II;
typedef vector<pair<int,int> > VII;
typedef long long LL;
typedef long double LD;

int bubble_sort(VI& vec)
{
    int cnt = 0;

    int N = SZ(vec);
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < i; ++j)
        {
            if (vec[j] > vec[i])
            {
                swap(vec[i], vec[j]);
                ++cnt;
            }
        }
    }

    return cnt;
}

int bubble_sort_rev(VI& vec)
{
    int cnt = 0;

    int N = SZ(vec);
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < i; ++j)
        {
            if (vec[j] < vec[i])
            {
                swap(vec[i], vec[j]);
                ++cnt;
            }
        }
    }

    return cnt;
}


int merge(VI& vec, int x, int mid, int y)
{
    VI lhs, rhs;
    FOR(i, x, mid+1)
            lhs.PB(vec[i]);
    lhs.PB(INF);

    FOR(i, mid+1, y+1)
            rhs.PB(vec[i]);
    rhs.PB(INF);

    int count = 0;

    int lIdx = 0, rIdx = 0;
    FOR(i, x, y+1)
    {
        if (lhs[lIdx] <= rhs[rIdx])
                vec[i] = lhs[lIdx++];
        else
        {
                count += SZ(lhs) - lIdx - 1;
                vec[i] = rhs[rIdx++];
        }
    }

    return count;
}

int merge_rev(VI& vec, int x, int mid, int y)
{
    VI lhs, rhs;
    FOR(i, x, mid+1)
            lhs.PB(vec[i]);
    lhs.PB(-INF);

    FOR(i, mid+1, y+1)
            rhs.PB(vec[i]);
    rhs.PB(-INF);

    int count = 0;

    int lIdx = 0, rIdx = 0;
    FOR(i, x, y+1)
    {
        if (lhs[lIdx] >= rhs[rIdx])
                vec[i] = lhs[lIdx++];
        else
        {
                count += SZ(lhs) - lIdx - 1;
                vec[i] = rhs[rIdx++];
        }
    }

    return count;
}


int mergeSort(VI& vec, int x, int y)
{
    if (x >= y)
            return 0;

    int mid = (x + y) / 2;
    int count = 0;
    count += mergeSort(vec, x, mid);
    count += mergeSort(vec, mid+1, y);
    count += merge(vec, x, mid, y);
    return count;
}

int mergeSort_rev(VI& vec, int x, int y)
{
    if (x >= y)
            return 0;

    int mid = (x + y) / 2;
    int count = 0;
    count += mergeSort_rev(vec, x, mid);
    count += mergeSort_rev(vec, mid+1, y);
    count += merge_rev(vec, x, mid, y);
    return count;
}

void print(const VI& vec)
{
    for (int i = 0; i < SZ(vec); ++i)
    {
        cout << vec[i] << " ";
    }
}

// map<VI, int> swaps;


int get_swaps(VI vec)
{
    int N = SZ(vec);
    // if (swaps.find(vec) != swaps.end())
    //     return swaps[vec];

    if (N <= 2)
    {
        // swaps[vec] = 0;
        return 0;
    }

    VI first = vec, last = vec;
    int min_idx = 0;
    for (int i = 0; i < N; ++i)
    {
        if (vec[i] < vec[min_idx])
        {
            min_idx = i;
        }
    }

    int num_swaps = min(min_idx, N - 1 - min_idx);
    vec.erase(vec.begin() + min_idx);

    num_swaps += get_swaps(vec);

    // swaps[vec] = num_swaps;

    return num_swaps;
}


int main(int argc, char const *argv[])
{
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t)
    {
        int N;
        cin >> N;
        VI nums(N);
        for (int i = 0; i < N; ++i)
        {
            cin >> nums[i];
        }

        int minSwaps = get_swaps(nums);

        printf("Case #%d: %d\n", t+1, minSwaps);
        // cout << "in:  "; print(nums); cout << endl;
        // cout << "out: "; print(bestup); cout << ","; print(bestdown); cout << endl;
    }

    return 0;
}
