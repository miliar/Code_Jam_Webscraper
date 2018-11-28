#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
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
#include <iostream>
#include <string.h>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
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
#include <iostream>
#include <string.h>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int main(){
    ifstream in("/Users/tech8/Desktop/Ainput.txt");
    ofstream out("/Users/tech8/Desktop/Aoutput.txt");

    long long testcase;
    in >> testcase;
    long long maxn = 1000000;
    for(int s = 0; s < testcase; s++)
    {
        int n;
        in >> n;
        long long val = (2*n - 1)*n;
        vector<int> a(val);
        vector<int> check(maxn, 0);
        for(int i = 0; i < val; i++){
            in >> a[i];
            check[a[i]]++;
        }
        vector<int> output;
        for(int i = 0; i < maxn; i++){ ///overkill
            if(check[i]%2 == 1){
                output.push_back(i);
            }
        }
        sort(output.begin(), output.end());
        out << "Case #" << s + 1 << ": ";
        for(int i = 0; i < output.size(); i++){
            out << output[i] << " ";
        }
        out << endl;
    }
}