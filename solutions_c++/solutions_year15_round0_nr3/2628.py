#include <iostream>
#include <string>
#include <utility>
using namespace std;

void solve(int testcase);

int main() {
    int N;
    cin >> N;
    for(int i=0; i<N; ++i)
        solve(i+1);
}

class Longstring {
    string L;
    unsigned X;
    unsigned len; // length of part
public:
    Longstring(string L, unsigned X) 
      : L(L),X(X),len(L.length())
    {}
    char operator[](size_t n) {
        //unsigned max = len*X;
        return L[n%len];
    }

    size_t length() {
        return len*X;
    }
};

pair<char,bool> reduce(char a, char b) {
    if(a == '1') {
        return make_pair(b,false);
    } else if(a == 'i') {
        if(b == 'i') return make_pair('1',true);
        if(b == 'j') return make_pair('k',false);
        if(b == 'k') return make_pair('j',true);
    } else if(a == 'j') {
        if(b == 'i') return make_pair('k',true);
        if(b == 'j') return make_pair('1',true);
        if(b == 'k') return make_pair('i',false);
    } else if(a == 'k') {
        if(b == 'i') return make_pair('j',false);
        if(b == 'j') return make_pair('i',true);
        if(b == 'k') return make_pair('1',true);
    }
}

unsigned reduceTo(Longstring &in,char dest, unsigned minpos, unsigned start) {
    bool flag = false;
    char reduced = in[start];
    if(reduced == dest && minpos<=start)
        return start+1;
    for(int i = start+1; i<in.length(); ++i){
        pair<char,bool> res = reduce(reduced,in[i]);
        reduced = res.first;
        flag ^= res.second;
        if(!flag && reduced==dest && i>=minpos)
            return i+1;
    }
    return in.length()+1;
}

void solve(int testcase) {
    unsigned inputlength;
    unsigned repeats;
    string inputpart;
    cin >> inputlength;
    cin >> repeats;
    cin >> inputpart;
    Longstring input(inputpart,repeats);
        
    unsigned ipos=0;
    unsigned jpos=0;
    unsigned kpos=0;
    bool done = false;

    while(ipos <= input.length() && !done) {
        ipos = reduceTo(input,'i',ipos,0);
        while(jpos <= input.length()) {
            jpos = reduceTo(input,'j',jpos,ipos);
            kpos = reduceTo(input,'k',input.length()-1,jpos);
            if(ipos < input.length() && jpos < input.length() && kpos == input.length()){
                done = true;
                break;
            }
        }
    }
    if(ipos < input.length() && jpos < input.length() && kpos == input.length()){
        cout << "Case #" << testcase << ": YES" << endl;
    } else {
        cout << "Case #" << testcase << ": NO" << endl;
    }
}
