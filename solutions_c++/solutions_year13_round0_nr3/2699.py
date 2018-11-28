
#include <vector>
#include <list>
#include <tr1/unordered_map>
#include <tr1/unordered_set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <assert.h>

using namespace std;

struct Node {
    
};

int main() {
    int T;
    cin >> T;
    for (int index = 1; index <= T; ++index) {
        int A, B;
        cin >> A >> B;
        int n2[] = {1, 4, 9, 121, 484};
        int count[] = {0, 1, 2, 3, 4, 5};
        int i = 0;
        while (n2[i] < A && i < 5) {
            ++i;
        }
        int j = 0;
        while (n2[j] <= B && j < 5) {
            ++j;
        }
        cout<<"Case #"<<index<<": "<<count[j] - count[i]<<endl;
    }
    return 0;
}