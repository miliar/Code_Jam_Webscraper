#include <iostream>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <complex>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <cfloat>
#include <ctime>

using namespace std;

typedef pair<int,int> point;

typedef signed char int8_t;
typedef unsigned char uint8_t;
typedef signed short int16_t;
typedef unsigned short uint16_t;
typedef signed int int32_t;
typedef unsigned int uint32_t;

int T;
int N;

string minimize(const string &str) {
    string ret;
    string::const_iterator it = str.begin();
    char current = *it;
    ret.push_back(current);
    while((++it) != str.end()) {
        if(*it != current) {
            current = *it;
            ret.push_back(current);
        }
    }
    return ret;
}

std::vector<int> string2count(const string &str) {
    std::vector<int> ret;
    
    char current = '+';
    for(string::const_iterator it = str.begin(); it != str.end(); ++it) {
        if(current != *it) {
            ret.push_back(1);
            current = *it;
        } else {
            ret.back()++;
        }
    }
    return ret;
}

int get_cost(const vector<int> &l, const vector<int> &r) {
    
    int ret = 0;
    for(int i = 0; i < l.size(); ++i) {
        ret += max(l[i], r[i]) - min(l[i], r[i]);
    }
    return ret;
}

int solv(vector<string> &strings) {
    
    string mini = minimize(strings[0]);
    for(int i = 1; i < strings.size(); ++i) {
        if(mini != minimize(strings[i])) {
            return INT_MAX;
        }
    }
    
    vector<vector<int> > counts;
    for(int i = 0; i < strings.size(); ++i) {
        counts.push_back(string2count(strings[i]));
    }
    
    vector<int> min_count(mini.length(), INT_MAX);
    for(int i = 0; i < counts.size(); ++i) {
        for(int j = 0; j < mini.length(); ++j) {
            min_count[j] = min(min_count[j], counts[i][j]);
        }
    }
    
    int cost = 0;
    for(int i = 0; i < strings.size(); ++i) {
        cost += get_cost(min_count, counts[i]);
    }
    
    for(int i = 0; i < strings.size(); ++i) {
        int tmp_cost = 0;
        for(int j = 0; j < strings.size(); ++j) {
            if(i == j) {
                continue;
            }
            tmp_cost += get_cost(counts[i], counts[j]);
        }
        cost = min(cost, tmp_cost);
    }
    
    
    return cost;
}

int main()
{
    cin >> T;
    for(int i = 0; i < T; ++i) {
        cin >> N;
        string tmp;
        vector<string> strings;
        for(int j = 0; j < N; ++j) {
            cin >> tmp;
            strings.push_back(tmp);
        }
        
        int ret = solv(strings);
        if(ret != INT_MAX) {
            printf("Case #%d: %d\n", i+1, ret);
        } else {
            printf("Case #%d: Fegla Won\n", i+1);
        }
    }
}

