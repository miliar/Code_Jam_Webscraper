#include<iostream>
#include<set>
#include<queue>
using namespace std;

char rev(char & s1) {
    return (s1 == '+' ? '-' : '+');
}
string convert(string input, int i) {
    string ans = input;
    
    int left = 0;
    int right = i - 1;

    while (left <= right) {
        swap(ans[left], ans[right]);
        ans[left] = rev(ans[left]);
        if (left == right)
            break;
        ans[right]= rev(ans[right]);
        left++;
        right--;
    }
    return ans;
}

int calc2(string begin, int len, bool sign) {
    char x = sign ? '+' : '-';
    char y = sign ? '-' : '+';
    bool first = true;
    
    for (int i = len-1; i >= 0; i--) {
        if (begin[i] == x)
            continue;
        else
            return 1 + calc2(begin, i, !sign);
            
    }
    return 0;
}

int calc(string begin){

    set<string> visited;
    string end="";
    for (int i = 0; i < begin.length(); i++)
        end += '+';
    queue<string> toHandle;
    int round = 0;
    toHandle.push(begin);
    visited.insert(begin);
    while(!toHandle.empty()) {
        int num = toHandle.size();
        for (int t = 0; t < num; t++) {
            string cur = toHandle.front(); toHandle.pop();
            if (cur == end)
                return round;
            else {
                bool first = true;
                for (int i = cur.length()-1; i>= 0; i--) {
                    if (first && cur[i] == '+')
                        continue;
                    else
                        first = false;
                    string strChange = convert(cur, i+1);
                    if (visited.find(strChange) == visited.end()) {
                        visited.insert(strChange);
                        toHandle.push(strChange);
                    }
                }
            }
        }
        round++;
    }
    
    return round;
}
int main() {
    int numCase = 1000000;
    cin >> numCase; 
    for (int i = 0; i < numCase; i++) {
        string val;
        cin >> val;
        cout <<"Case #"<<(i+1)<<": "<<calc2(val, val.length(),true)<<endl;
    }
}
