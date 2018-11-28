#include <vector>
#include <map>
#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>

using namespace std;

const string path = "/Users/mac/Documents/cpp/Code Jam/";

const string IMPOSSIBLE = "IMPOSSIBLE";
const int N = 101;

int b[N] =   { 0,   2,   4,   5,   6,   7,   8,   9,   1,   3};
char ch[N] = {'Z', 'W', 'U', 'F', 'X', 'S', 'G', 'I', 'N', 'R'};

string nums[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int main() {
    ifstream cin(path + "in");
    ofstream cout(path + "out");
    
    int T;
    cin >> T;
    for (int CT = 1;  CT <= T; CT ++) {
        string s;
        cin >> s;
        
        vector<int> sk(300, 0);
        for (int j = 0; j < s.size(); j ++)
            sk[s[j]] ++;
        
        vector<int> a(10, 0);
        
        for (int i = 0; i < 10; i ++) {
            int d = b[i];
            int ex = ch[i];
            
            a[d] = sk[ex];
            
            string num = nums[d];
            for (int j = 0; j < num.size(); j ++)
                sk[num[j]] -= a[d];
        }
        
        string t;
        for (int i = 0; i < 10; i ++)
            for (int j = 0; j < a[i]; j ++)
                t += char('0' + i);
        
        cout << "Case #" << CT << ": " << t << endl;
    }
    
    
    return 0;
}
