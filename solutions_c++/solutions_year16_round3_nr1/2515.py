#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <utility>
#include <cassert>
using namespace std;

int N;
struct senator{
    char name;
    int value;
};

bool cmp(senator &s1, senator &s2){
    return s1.value < s2.value;
}
senator s_array[26];

vector<string> res;

void solve(int t){
    res.clear();
    cin >> N;
    for(int i = 0; i < N; ++i){
        s_array[i].name = 'A' + i;
        cin >> s_array[i].value;
    }
    sort(s_array, s_array + N, cmp);
    while(N){
        //cout << "N: " << N << endl;
        assert(N >= 2);
        if(N == 2){
            assert(s_array[0].value == s_array[1].value);
            for(int i = 0; i < s_array[0].value; ++i){
                string cur;
                cur += s_array[0].name;
                cur += s_array[1].name;
                res.push_back(cur);
                //cout << cur << endl;
            }
            s_array[0].value = s_array[1].value = 0;
            N -= 2;
        }else{
            int end = N - 1;
            int end2 = N - 2;
            int end3 = N - 3;
            int loop = s_array[end2].value - s_array[end3].value + 1;
            if(N == 3 && s_array[end2].value == s_array[end].value && s_array[end2].value == 1){

                string cur;
                cur += s_array[end].name;
                //cout << cur << endl;
                res.push_back(cur);
                N -= 1;
            }else{
                while(s_array[end2].value > 0 && s_array[end2].value + 1 > s_array[end3].value){
                    if(N == 3 && s_array[end2].value == s_array[end].value && s_array[end2].value == 1){

                        string cur;
                        cur += s_array[end].name;
                        //cout << cur << endl;
                        res.push_back(cur);
                        N -= 1;
                        break;
                    }
                    string cur;
                    cur += s_array[end].name;
                    cur += s_array[end2].name;
                    res.push_back(cur);
                    //cout << cur << endl;
                    s_array[end2].value -= 1;
                    s_array[end].value -= 1;
                }
                if(s_array[end2].value == 0)
                {
                    s_array[end2] = s_array[end];
                    N -= 1;
                }
                if(s_array[N-1].value == 0){
                    N -= 1;
                }
                for(int i = 1; i <= 2 && end3 + i < N; ++i){
                    int ind = end3 + i;
                    int j;
                    for(j = ind - 1; j >= 0 && s_array[ind].value < s_array[j].value; j--);
                    senator save = s_array[ind];
                    for(int k = ind - 1; k > j && k >= 0; k--)
                        s_array[k+1] = s_array[k];
                    s_array[j+1] = save;
                }
    
            }
        }
    }

    cout << "Case #" << t << ": ";
    for(int i = 0; i < res.size(); ++i)
        cout << res[i] << " ";
    cout << endl;
    return;
}

using namespace std;
int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;++t){
        solve(t);
    }

    return 0;
}
