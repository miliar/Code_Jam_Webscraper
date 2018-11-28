#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdio>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <ostream>
using namespace std;

bool is_cons(char c){
    return c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u';
}

int main(int argc, char *argv[]){
    cerr << "go!" << endl;
    
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int test_count; cin >> test_count;
    for(int test = 0; test < test_count; ++test){
        string s; cin >> s;
        int len; cin >> len;
        
        int ans = 0;
        for(int st = 0; st < s.size(); ++st){
            for(int l = len; st + l <= s.size(); ++l){
                string curr = s.substr(st, l);
                //cerr << curr << endl;
                int maxrow = 0;
                int cnt = 0;
                for(int i = 0; i < curr.size(); ++i)
                    if(is_cons(curr[i])){
                        ++cnt;
                        if(cnt > maxrow)
                            maxrow = cnt;
                    } else 
                        cnt = 0;
                    if(maxrow >= len){
//                        cerr << curr << " " << maxrow << endl;
                        ++ans;
                    }
            }
        }
        //vector<int> cons_follow(s.size());
        //int cnt = 0;
        //for(int i = s.size() - 1; i >= 0; --i){
        //    if(is_cons(s[i]))
        //        ++cnt;
        //    else
        //        cnt = 0;
        //    cons_follow[i] = cnt;
        //}
        //for(int i = s.size() - 2; i >= 0; --i)
        //    if(cons_follow[i] == 0)
        //        cons_follow[i] = cons_follow[ i + 1 ];
        //
        //for(int i = 0; i < cons_follow.size(); ++i)
        //    cerr << cons_follow[i] << " ";
        //cerr << endl;

        //long long ans = 0;
        //for(int i = 0; i < s.size(); ++i)
        //    if(cons_follow[i] >= len){
        //        long long diff = s.size() - i - len;
        //        ans += diff;
        //        //cerr << diff << " ";
        //    }
        //    //cerr << endl;
        cout << "Case #" << (test + 1) << ": " << ans << endl;
    }
    cerr << "done!" << endl;
    return 0;
}