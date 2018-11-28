
#include <string.h>
#include <unordered_map>
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>
#include <unordered_set>

using namespace std;


vector<string> numbers = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int freq[300];
int total=0;
vector<int> res;
bool form(int num){
    if(num > 9) return false;
    if(total == 0) return true;
    string w = numbers[num];
    bool can = 1;
    for(char c : w){
        freq[c]--;
        total--;
        if(freq[c] < 0) can=0;
    }
    if(can){
        res.push_back(num);
        bool r = form(num);
        if(!r){
            res.pop_back();
            for(char c : w){
                freq[c]++;
                total++;
            }
            return form(num+1);
        }
        return true;
    }
    else{
     for(char c : w){
        freq[c]++;
        total++;
     }
     return form(num+1);
    }
}
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tst;
    cin >> tst;
    for(int tt=1; tt <= tst; tt++){
        memset(freq,0,sizeof(freq));
        total=0;
        res.clear();
        string s;
        cin >> s;
        for(char c : s){
            freq[c]++;
            total++;
        }
        cout << "Case #"<<tt<<": ";
        if(form(0)){
            for(int a : res)
                cout << a;
        }
        else{
            cout << "Impossible";
        }
        cout << endl;
    }
    return 0;
}