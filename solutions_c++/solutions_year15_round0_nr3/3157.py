//#define CUTE_PLATFORM
//#define CUTE_MAIN_RUNNER

#ifdef CUTE_PLATFORM
#include "cute_algostudy.h"
#endif

#include <string>
#include <vector>
#include <iostream>

#include <map>
#include <set>
#include <algorithm>

#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#ifdef CUTE_PLATFORM
namespace code_jam_2015_0_c {
#endif

using namespace std;

class Cache {
public:
    pair<bool, char> cache[10000][10000];
};

char mult(char a, char b, bool& pos){
    if(a == '1' && b == '1'){
        return '1';
    }
    if(a == '1' && b == 'i'){
        return 'i';
    }
    if(a == '1' && b == 'j'){
        return 'j';
    }
    if(a == '1' && b == 'k'){
        return 'k';
    }

    if(a == 'i' && b == '1'){
        return 'i';
    }
    if(a == 'i' && b == 'i'){
        pos = !pos;
        return '1';
    }
    if(a == 'i' && b == 'j'){
        return 'k';
    }
    if(a == 'i' && b == 'k'){
        pos = !pos;
        return 'j';
    }

    if(a == 'j' && b == '1'){
        return 'j';
    }
    if(a == 'j' && b == 'i'){
        pos = !pos;
        return 'k';
    }
    if(a == 'j' && b == 'j'){
        pos = !pos;
        return '1';
    }
    if(a == 'j' && b == 'k'){
        return 'i';
    }

    if(a == 'k' && b == '1'){
        return 'k';
    }
    if(a == 'k' && b == 'i'){
        return 'j';
    }
    if(a == 'k' && b == 'j'){
        pos = !pos;
        return 'i';
    }
    if(a == 'k' && b == 'k'){
        pos = !pos;
        return '1';
    }

    return '1';

}

bool mult(vector<char>& target, int start, int end, char wanted, Cache& cache){
    pair<bool, char>& cached = cache.cache[start][end];
    if(cached.second == 'i' || cached.second == 'j' || cached.second == 'k' || cached.second == '1'){
        return (cached.first && cached.second == wanted);
    }

    //cout << "--3" << endl;
    if(start == end){
        cached = pair<bool, char>(true, target[start]);
        //cout << "--4" << ", " << start << target[start] << endl;
        if(wanted == target[start]){
            //cout << "--5" << endl;
            return true;
        }
        return false;
    }

    pair<bool, char>& cached_prev = cache.cache[start][end-1];
    if(cached_prev.second == 'i' || cached_prev.second == 'j' || cached_prev.second == 'k' || cached_prev.second == '1'){
        bool pos = cached_prev.first;
        char ret = mult(cached_prev.second, target[end], pos);
        cached = pair<bool, char>(pos, ret);
        return (ret == wanted && pos);
    }

    bool pos = true;
    char ret = mult(target[start], target[start + 1], pos);
    int nextIdx = start + 2;
    while(nextIdx <= end){
        ret = mult(ret, target[nextIdx], pos);
        nextIdx++;
    }

    cached = pair<bool, char>(pos, ret);
    return (ret == wanted && pos);
}

bool divide(vector<char>& target, int start, int selected, Cache& cache){
    if(selected == 3){
        int lastEnd = target.size() - 1;
        //cout << "--" << start << ", " << lastEnd << endl;
        if(start > lastEnd){
            return false;
        }

        // 종료 조건
        //cout << "--" << start << ", " << lastEnd << endl;
        return mult(target, start, lastEnd, 'k', cache);
    }

    for(int end = start; end < target.size(); ++end){
        char wanted = 'j';
        if(selected == 1){
            wanted = 'i';
        }
        //cout << wanted << ", " << start << ", " << end << endl;
        if(!mult(target, start, end, wanted, cache)){
            continue;
        }

        //cout << "--2" << endl;

        if(divide(target, end + 1, selected + 1, cache)){
            return true;
        }
    }
    return false;
}

string solve(){
    int CHAR_NUM, REPEAT_NUM;
    cin >> CHAR_NUM >> REPEAT_NUM;
    string chars;
    cin >> chars;

    vector<char> sequences;
    for(int i = 0; i < REPEAT_NUM; ++i){
        for(int j = 0; j < chars.size(); ++j){
            sequences.push_back(chars[j]);
        }
    }

    Cache* cache = new Cache;
    bool ret = divide(sequences, 0, 1, *cache);
    delete cache;
    if(ret){
        return "YES";
    }
    return "NO";
}

int main(){
	int T;
	cin >> T;

	for(int testCaseNo = 1; testCaseNo <= T; ++testCaseNo){
	    string ret = solve();
	    cout << "Case #" << testCaseNo << ": " << ret << endl;
	}
	return 0;
}

#ifdef CUTE_PLATFORM
#ifdef CUTE_MAIN_RUNNER
CUTE_MAIN(__FILE__, main);
#endif
}
#endif
