#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <string>
#include <unordered_map>
#include <cmath>

using namespace std;
typedef long long lld;
unordered_map<lld, vector<string>> ans;
unordered_map<string, vector<lld>> proof;

void convert(string& str, lld val) {
    str = "";
    while(val) {
        str = str + ((val % 2) ? "1" : "0");
        val /= 2;
    }
    reverse(str.begin(), str.end());
}

bool judge(const string& str) {
    int len = str.size();
    vector<lld> vec;
    for(lld i = 2; i <= 10; ++ i) {
        lld cnt = 0;
        for(lld j = 0; j < len; ++ j) {
            cnt = cnt * i + (str[j] - '0');
        }
        bool mark = false;
        //cout << cnt << endl;
        for(lld j = 2; j * j <= cnt; ++ j) {
            lld tmp = cnt / j;
            if(j * tmp == cnt) {
                vec.push_back(j);
                mark = true;
                break;
            }
        }
        if(!mark) {
            return false;
        }
    }
    for(lld j = 0; j < vec.size(); ++ j)
        proof[str].push_back(vec[j]);
    return true;
}

int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("C-small-attempt2.in", "r", stdin);
    //freopen("C-out.txt", "w", stdout);
    int tcase, n, num;
    cin >> tcase;
    cin >> n >> num;

    for(int i = n; i <= n; ++ i) {
        lld lf = pow(2, i-1)+1;
        lld rt = pow(2, i-1) - 1 + pow(2, i-1);
        int cnt = 0;
        for(int j = lf; j <= rt; ++ j) {
            if(!(j & 1)) continue;
            string str = "";
            convert(str, j);
            //cout << str << endl;
            if(judge(str)) {
                cnt ++;
                ans[i].push_back(str);
                if(cnt > 500) break;
            }
        }
    }

    printf("Case #1:\n");
    for(int i = 0; i < num; ++ i) {
        cout << ans[n][i];
        for(int j = 0; j <  proof[ans[n][i]].size(); ++ j)
            cout << " " << proof[ans[n][i]][j];
        cout << endl;
    }

    //fclose(stdin);
    //fclose(stdout);
    return 0;
}
