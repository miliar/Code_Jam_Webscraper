#include <cstdio>
#include <cmath>
#include <string>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <fstream>
#include <set>
#include <map>
#include <unordered_map>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>
#define MAX_NUM 2500

using namespace std;
typedef long long ll;
unordered_map<string, int> dict;
int n;
int word[MAX_NUM];
int nword;

int solve(int cf, vector<int> corr[]){
    fill(word, word+MAX_NUM, 0);
    for(int i = 0; i < n; i++){
        int add = 0;
        if(cf >> i & 1)
            add = 2;
        else
            add = 1;
        for(int j = 0; j < corr[i].size(); j++)
            word[corr[i][j]] |= add;
    }
    int cnt = 0;
    for(int i = 0; i < nword; i++)
        if((word[i] & 3) == 3)
            cnt++;
    return cnt;
}

int main()
{
    freopen("/Users/bochen/Downloads/textfile.in","r", stdin);
    freopen("/Users/bochen/Downloads/textfile.out","w", stdout);

    int t;
    cin >> t;
    for(int cid = 1; cid <= t; cid++){
        cin >> n;
        nword = 0;
        dict.clear();
        vector<int> corr[20];
        string line, word;
        getline(cin, line);
        for(int s = 0; s < n; s++){
            getline(cin, line);
            stringstream ss;
            ss << line;
            while(ss >> word){
                if(dict.count(word) == 0)
                    dict[word] = nword++;
                corr[s].push_back(dict[word]);
            }
        }
        int cf = 1;
        int res = MAX_NUM;
        for(int i = 0; i < (1<<(n-2)); i++)
            res = min(res, solve(i*4+cf, corr));
        printf("Case #%d: %d\n", cid, res);
    }
    return 0;
}
