#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <stdlib.h>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <numeric>
#include <utility>
#include <deque>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <queue>
#include <limits>
#include <fstream>
#include <list>
#include <sstream>
#include <iostream>
#include <iomanip>
//#include <time.h>
using namespace std;
#define MAX 1005
#define pii pair<long long , long long>
#define mp make_pair

int main() {
    int t;
    scanf("%d", &t) ;
    string s;
    for( int q = 1 ; q <= t && cin>>s  ; ++q ){
        string ini = "";
        ini += s[0];
        for( int i = 1 ; i < s.length() ; ++i ){
            if( s[i] >= ini[0] ){
                string aux = "";
                aux += s[i];
                //cout<<aux<<endl;
                ini = aux + ini;
                //cout<<ini<<endl;
            }else
                ini += s[i];
        }

        printf("Case #%d: ", q  );
        cout<<ini<<endl;
    }
    return 0 ;
}
