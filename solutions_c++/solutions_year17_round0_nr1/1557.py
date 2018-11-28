#include<iostream>
#include<cstdint>
#include<string>
#define MAX 1005

using namespace std;
typedef int64_t var;
bool p[MAX];
var t, n, s, count;

int main(){
    cin >> t;
    for(var i = 0; i < t; ++i){
        string line;
        cin >> line;
        n = line.length();
        for(var j = 0; j < n; ++j){
            p[j]=(line[j]=='+');
        }
        cin >> s;
        count = 0;
        for(var j = 0; j < n-s+1; ++j){
            if(!p[j]){
                for(var k = j; k < j+s; ++k){
                    p[k]=!p[k];
                }
                ++count;
            }
        }
        bool possible = true;
        for(var j = n-s; j < n; ++j){
            if(!p[j]){
                cout << "Case #" << (i+1) << ": IMPOSSIBLE" << endl;
                possible = false;
                break;
            }
        }
        if(possible){
            cout << "Case #" << (i+1) << ": " << count << endl;
        }
    }
    return 0;
}
