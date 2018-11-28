/* BEGIN_OF_SOURCE_CODE */
#include <iostream>
#include <fstream>
#include <sstream>  

#include <cstring> //for memset
#include <cstdio>
#include <cmath>

#include <algorithm>
#include <numeric>
#include <iterator>

#include <vector>
#include <list>
#include <string>

#include <queue>
#include <stack>

#include <utility>
#include <map>
#include <set>
#include <iomanip> //??

#define REP(i,n) for(int i=0;i<(n);++i) 

using namespace std; //change 

int T;
string ss;
int n;
int cnt;


bool is_con(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

bool acc(const string &s) {
    bool flag = false;
    for(int i = 0; !flag && i <= s.size() - n; ++i) {
        bool tflag = true;
        for(int j = 0; j < n; ++j) {
            if(is_con(s[i+j])) {
                tflag = false;
                break;
            }
        }
        flag = tflag;
    }
    return flag;
}

void gao() {
    for(int i = 0; i < ss.size(); ++i) {
        for(int len = n; i + len - 1 < ss.size(); ++len) {
            if(acc(ss.substr(i, len))) cnt++;
        }
    }
    return ;
}


int main(void) {
    cin>>T;
    for(int i = 1; i <= T; ++i) {
        cin>>ss>>n;
        cout<<"Case #"<<i<<": ";
        cnt = 0;
        gao();
        cout<<cnt<<endl;
    }
    return 0;
}
/* @END_OF_SOURCE_CODE */
