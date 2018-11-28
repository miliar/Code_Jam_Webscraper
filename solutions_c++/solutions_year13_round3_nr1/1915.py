#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <utility>
#define abs(x) (((x)>0)?(x):(-x))
#define max(a,b) ((a>b)?(a):(b))
#define min(a,b) ((a<b)?(a):(b))

using namespace std;

string str;
int n;
set < char > vowels;
int pos[1000100];
int len[1000100];

long long solve()
{
    long long res = 0;
    int tot = 1;
    int L = str.size();
    int conse = 0;
    for(int i = 0; i < L; i++){
        bool flag = false;
        conse = 0;
        for(int j = i; j < L; j++){
            if(vowels.find(str[j]) == vowels.end()){
                conse ++;
            }
            else{
                conse = 0;
            }
            if(conse >= n) flag = true;
            if(flag) res ++;
        }
    }
    return res;
}

int main()
{
    //freopen("sample.in", "r", stdin);
    vowels.insert('a');
    vowels.insert('e');
    vowels.insert('i');
    vowels.insert('o');
    vowels.insert('u');
    int T;
    cin >> T;
    for(int Case = 1; Case <= T; Case++){
        cin >> str >> n;
        cout << "Case #" << Case << ": " << solve()<<endl;
    }
    return 0;
}
