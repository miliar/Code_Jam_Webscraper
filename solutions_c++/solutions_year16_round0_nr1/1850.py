#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <unordered_map>
#include <algorithm>
using namespace std;
#define MP(x,y) make_pair(x,y)

bool static comparedesc(const long &stud1, const long &stud2){
    return stud1 > stud2;
}

int main(){
    int t ;
    cin >> t;
    for(int _t=1; _t<=t; _t++){
        short int d;
        map<long long, bool> done;
        vector<bool> seen(10, false);
        int allseen = 0;
        long long num, tempNum, N;
        cin >> N;
        cout << "Case #" << _t << ": ";
        num = 0;
        while(allseen<10){
            tempNum = num + N;
            if(done.count(tempNum) == 1) break;
            num = tempNum;
            done[tempNum] = true;
            while(tempNum){
                d = tempNum%10;
                allseen += !seen[d];
                seen[d] = true;
                tempNum /= 10;
            }
        }
        if(allseen == 10)
            cout << num << endl;
        else
            cout << "INSOMNIA\n";
    }
    return 0;
}