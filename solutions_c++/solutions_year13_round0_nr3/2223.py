#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
#include <complex>
#include <limits>
#include <list>
#include <stack>
#include <numeric>
#include <queue>
#include <algorithm>
#include <functional>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <map>
#include <list>
#include <math.h>
#include <set>
#include <stdio.h>
#include <ctype.h>
#include <vector>
#include <sstream>

using namespace std;


vector<string> getLineFields(istream& stream) {
    string line;
    getline(stream, line);
    stringstream str;
    str << line;
    vector<string> fields;
    string temp;
    while(str>>temp)
    {
        fields.push_back(temp);
    }
    return fields;
}

bool poly(long a) {
    stringstream strstr;
    strstr << a;
    string s;
    strstr >> s;
    for (int i = 0; i < s.length() / 2; ++i)
        if (s[i] != s[s.length() - i - 1])
            return false;
    return true;
}

vector<long long> numbers;

void init() {
    numbers.push_back(1ll);
    numbers.push_back(4ll);
    numbers.push_back(9ll);
    numbers.push_back(121ll);
    numbers.push_back(484ll);
    numbers.push_back(10201ll);
    numbers.push_back(12321ll);
    numbers.push_back(14641ll);
    numbers.push_back(40804ll);
    numbers.push_back(44944ll);
    numbers.push_back(1002001ll);
    numbers.push_back(1234321ll);
    numbers.push_back(4008004ll);
    numbers.push_back(100020001ll);
    numbers.push_back(102030201ll);
    numbers.push_back(104060401ll);
    numbers.push_back(121242121ll);
    numbers.push_back(123454321ll);
    numbers.push_back(125686521ll);
    numbers.push_back(400080004ll);
    numbers.push_back(404090404ll);
    numbers.push_back(10000200001ll);
    numbers.push_back(10221412201ll);
    numbers.push_back(12102420121ll);
    numbers.push_back(12345654321ll);
    numbers.push_back(40000800004ll);
    numbers.push_back(1000002000001ll);
    numbers.push_back(1002003002001ll);
    numbers.push_back(1004006004001ll);
    numbers.push_back(1020304030201ll);
    numbers.push_back(1022325232201ll);
    numbers.push_back(1024348434201ll);
    numbers.push_back(1210024200121ll);
    numbers.push_back(1212225222121ll);
    numbers.push_back(1214428244121ll);
    numbers.push_back(1232346432321ll);
    numbers.push_back(1234567654321ll);
    numbers.push_back(4000008000004ll);
    numbers.push_back(4004009004004ll);
    numbers.push_back(100000020000001ll);
    numbers.push_back(100220141022001ll);
    numbers.push_back(102012040210201ll);
    numbers.push_back(102234363432201ll);
    numbers.push_back(121000242000121ll);
    numbers.push_back(121242363242121ll);
    numbers.push_back(123212464212321ll);
    numbers.push_back(123456787654321ll);
    numbers.push_back(400000080000004ll);
}

int main() {
    int T;
    cin >> T;
    
    init();
    
    for (int t = 0; t < T; ++t) {
        long a, b;
        cin >> a >> b;
//        int res1 = 0;
//        for (long k = (long)sqrt(a) - 1; k * k <= b; ++k) {
//            if (poly(k) && poly(k*k) && k * k >= a && k * k <= b) {
//                ++res1;
//            }
//        }
        
        int pos1 = (int)(lower_bound(numbers.begin(), numbers.end(), a) - numbers.begin());
        int pos2 = (int)(lower_bound(numbers.begin(), numbers.end(), b) - numbers.begin());
        int res = pos2 - pos1;
        bool isfirst = false, issecond = false;
        if (pos1 < numbers.size() && numbers[pos1] == a) isfirst = true;
        if (pos2 < numbers.size() && numbers[pos2] == b) issecond = true;
        if (issecond) ++res;
        cout << "Case #" << t + 1 << ": " << res << endl;
    }
}
