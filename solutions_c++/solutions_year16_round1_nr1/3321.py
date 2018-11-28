#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <climits>
#define pi acos(-1.0)
#define LL long long

using namespace std;

typedef pair<int, int> ii;

int main()
{
    int N;
    cin >> N;
    for (int n = 1; n <= N; n++) {
        string word;
        cin >> word;
        list<char> res;
        res.push_back(word[0]);
        for (int i = 1; i < word.size(); i++) {
            if (word[i] >= res.front()) {
                res.push_front(word[i]);
            } else {
                res.push_back(word[i]);
            }
        }
        printf("Case #%d: ", n);
        for (auto i = res.begin(); i != res.end(); i++) {
            printf("%c", *i);
        }
        printf("\n");
    }
    return 0;
}
