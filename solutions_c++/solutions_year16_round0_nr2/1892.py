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

int makeAllPos(int ind, string &ins, bool make_pos){
    if(ind<0) return 0;
    if(make_pos){
        if ( ins[ind] == '-'){
            return 1 + makeAllPos(ind-1, ins, false);
        }else{
            return makeAllPos(ind-1, ins, true);
        }
    }else{
        if ( ins[ind] == '-'){
            return makeAllPos(ind-1, ins, false);
        }else{
            return 1 + makeAllPos(ind-1, ins, true);
        }
    }
}

int main(){
    int t ;
    cin >> t;
    for(int _t=1; _t<=t; _t++){
        cout << "Case #" << _t << ": ";
        string ins;
        cin >> ins;
        cout << makeAllPos((int)ins.length()-1, ins, true) << endl;
    }
    return 0;
}