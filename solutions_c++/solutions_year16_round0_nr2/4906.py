#include <iostream>
#include <vector>
//#include <algorithm>
//#include <string>
//#include <stack>
//#include <unordered_map>
//#include <limits.h>
//#include <time.h>
//#include <queue>
using namespace std;



int main(){
    int t; cin >> t;
    for(int z = 0; z < t; ++z){
        string str; cin >> str;
        int length = str.length();
        vector<bool> data;
        if(str[0] == '+') data.push_back(1);
        else data.push_back(0);
        int size = 1;
        for(int i = 1; i < str.length(); ++i){
            if(str[i] == '+' && data[size - 1] == 0){
                data.push_back(1);
                ++size;
            }
            else if(str[i] == '-' && data[size - 1] == 1){
                data.push_back(0);
                ++size;
            }
        }
        int i = 0;
        int total = 0;
        //for_each(data.begin(), data.end(), [](const bool & a)->void{ cout << a << ' '; }); cout << endl;
        cout << "Case #" << z + 1 << ": ";
        if(*(data.end() - 1) == 0) cout << data.size() << endl;
        else cout << data.size() - 1 << endl;
    }
}
