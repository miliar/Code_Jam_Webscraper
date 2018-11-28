#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


void solve(vector<vector<int> > vals, int i ){
    

}
int main(int argc, char **argv)
{
    int test_cnt = 0;
    scanf("%d", &test_cnt);
    string s;
    getline(cin, s);
    for (int i = 0; i < test_cnt; i++){
        string s;
        getline(cin, s);
        string next;
        if (s.size () != 0){
            char c = s[0];
            next = string(1, c);
            for (int j = 1; j < s.size(); j++){
                if (s[j] >= next[0])
                    next = string(1,s[j]) + next;
                else
                    next = next + string(1,s[j]);
            }
        }
        cout << "Case #"<<i+1<< ": " << next << endl;
    }
    return 0;
}

