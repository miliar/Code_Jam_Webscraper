#include <string>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath> 

using namespace std;

   
int main() {

    //num of test cases
    int test_cnt;
   
    cin >> test_cnt;

    for(int idx = 1; idx <= test_cnt; idx++) {
        int N;
        int fail = 0;
        cin >> N;
        vector<string> string_v;

        for(int i = 0; i < N ; i++){
            string tmp;
            cin >> tmp;
            string_v.push_back(tmp);
        }
    
        string pattern; 
        int pattern_total[101];
        int pattern_cnt[101][101];

        memset(pattern_total,0,101*4);
        memset(pattern_cnt,0,101*101*4);

        char a = string_v[0][0];
        pattern.push_back(a);
       
        // map pattern
        for(int i = 0; i < string_v[0].size(); i++) {
            if(string_v[0][i] != a){
                a = string_v[0][i];
                pattern.push_back(a);
            } 
        }

        for(int i = 0; i < N; i++) {
            char a = string_v[i][0];
            string pattern_tmp;
            pattern_tmp.push_back(a);
            
            int cnt = 0;
            int idx = 0;
            for(int j = 0; j < string_v[i].size(); j++) {
                if(string_v[i][j] != a){
                    pattern_total[idx] += cnt;
                    pattern_cnt[i][idx++] = cnt; 
                    
                    cnt = 1;
                    a = string_v[i][j];
                    pattern_tmp.push_back(a);
                }
                else{
                   cnt++;
                }
            }
            pattern_total[idx] += cnt;
            pattern_cnt[i][idx] = cnt; 

            if (pattern.compare(pattern_tmp) != 0) {
                fail = 1;
                break;
            }
        }
       
        int result = 0;

        if (fail == 1)
            cout << "Case #"<<idx<<": Fegla Won"<<endl; 
        else {
            for(int i = 0 ; i < pattern.size(); i++) {
               // cout << pattern_total[i];
               // cout <<endl;
                pattern_total[i] = (pattern_total[i] + N/2) / N;
            }
            for(int j = 0 ; j < N; j++) {
                for(int i = 0 ; i < pattern.size(); i++) {
                    result += abs(pattern_cnt[j][i]- pattern_total[i]);
                }
            }
             
            cout << "Case #"<<idx<<": "<<result<<endl;   
        }
    }

   return 0;
}
