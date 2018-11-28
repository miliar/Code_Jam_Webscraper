#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
//#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <iterator>
using namespace std;

ifstream cin("/Users/Nagi2/Downloads/GCJ2016/A-large.in");
ofstream cout("/Users/Nagi2/Downloads/mnbvcxzAxx.txt");

string f(char p, int n){
    if(n==1){
        if(p=='R') return string ("PS");
        if(p=='S') return string ("PR");
        if(p=='P') return string ("RS");
        
    }
    else{
        string s1,s2;
        if(p=='R'){
            s1 = f('S',n-1);
            s2 = f('R',n-1);
            string s3 = s1+s2;
            string s4 = s2+s1;
            return min(s3,s4);
        }
        if(p=='S'){
            s1 = f('S',n-1);
            s2 = f('P',n-1);
            string s3 = s1+s2;
            string s4 = s2+s1;
            return min(s3,s4);
        }
        if(p=='P'){
            s1 = f('R',n-1);
            s2 = f('P',n-1);
            string s3 = s1+s2;
            string s4 = s2+s1;
            return min(s3,s4);
        }
    }
    return string("");
}


int main(int argc, const char * argv[]) {
    int T;
    cin >> T;
    int ans = 0;
    for(int t =0;t<T;t++){
        int N, R, P,S;
        cin >> N;
        cin >> R >> P >> S; //Must check if order correct
        string s1 = f('S',N);
        string s2 = f('R',N);
        string s3 = f('P',N);
        string s1p = s1;
        string s2p = s2;
        string s3p = s3;
        sort(s1p.begin(),s1p.end());
        sort(s2p.begin(),s2p.end());
        sort(s3p.begin(),s3p.end());
        string s4;
        for(int i=0;i<R;i++){
            s4+='R';
        }
        for(int i=0;i<P;i++){
            s4+='P';
        }
        for(int i=0;i<S;i++){
            s4+='S';
        }
        sort(s4.begin(),s4.end());
        if(s4 == s1p){
            cout << "Case #" << t+1 <<": " << s1 << endl;
        }
        else if(s4 == s2p){
            cout << "Case #" << t+1 <<": " << s2 << endl;
        }
        else if(s4 == s3p){
            cout << "Case #" << t+1 <<": " << s3 << endl;
        }
        else{
            cout << "Case #" << t+1 << ": IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
