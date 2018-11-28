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
        printf("Case #%d: ", _t);
        string s;
        cin >> s;
        string anss = "";
        anss += s[0];
        int len = 1;
        for(int i=1; i<s.length(); i++){
            if(s[i] >= anss[0])
                anss = s.substr(i,1) + anss;
            else anss += s[i];
            len++;
        }
        cout << anss << endl;
    }
    return 0;
}