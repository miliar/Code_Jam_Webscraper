#include <queue>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <fstream>
#include <cstring>
#include <string>
#include <climits>
#include <random>
using namespace std;

//macros
typedef long long ll;
typedef complex<double> point;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector< vector<int> > vvi;




#define FOR(k,a,b) for(int k=(a); k<=(b); ++k)
#define REP(k,a) for(int k=0; k<(a);++k)
#define SZ(a) int((a).size())
#define ALL(c) (c).begin(),(c).end()
#define PB push_back
#define MP make_pair
#define INF 999999999
#define INFLONG 1000000000000000000
#define MOD 1000000007
#define MAX 100
#define ITERS 100
#define MAXM 200000
#define MAXN 100000
#define _gcd __gcd
#define eps 1e-9
#define pi 3.1415926535897932384626
bool good(string str){
    REP(i,str.length()){
        if(str[i]=='-') return false;
    }
    return true;
}
char inv(char ch){
    if(ch=='-') return '+';
    else return '-';
}
string tran(string str){
    string res = "";
    for(int i = str.length()-1; i >=0; i--){
        res += inv(str[i]);
    }
    return res;
}
int greed(string str){
    int cnt = 0;
    string currstr = str;
    bool found1=false;
    bool found2=false;
    for(int it = 1; it <= 10; it++){
        if(good(currstr)){
            found1=true;
            break;
        }
        int ind = -1;
        for(int p = currstr.length()-1; p >=0; p--){
            if(currstr[p]=='-'){
                ind = p;
                break;
            }
        }
        cnt++;
        string newstr = tran(currstr.substr(0,ind+1)) + currstr.substr(ind+1,currstr.length()-ind-1);
        currstr = newstr;
    }
    int cnt2 = 0;
    currstr = str;
    for(int it = 1; it<=10; it++){
        if(good(currstr)){
            found2=true;
            break;
        }
        int ind = -1;
        for(int p=0; p < currstr.length(); p++){
            if(currstr[p]=='-'){
                ind = p;
                break;
            }
        }
        cnt2++;
        string newstr = tran(currstr.substr(0,ind+1)) + currstr.substr(ind+1,currstr.length()-ind-1);
        currstr = newstr;
    }
    if(!found1 && !found2) return -1;
    else if(!found2) return cnt;
    else if(!found1) return cnt2;
    else return min(cnt,cnt2);
}
int brute(string str){
    queue<string> q;
    q.push(str);
    map<string,bool> seen;
    int currdep = 0;

    while(!q.empty()){
        int sz = SZ(q);
        for(int it=0; it < sz; it++){
            string top = q.front();
            q.pop();
            if(seen[top]) continue;
            if(good(top)){
                return currdep;
            }
            seen[top] = true;
            for(int endind = 0; endind < top.length(); endind++){
                string res = tran(top.substr(0,endind+1)) + top.substr(endind+1,str.length()-endind-1);
                q.push(res);
            }
        }
        currdep++;
    }
    return -1;
}
int main()
{
    ifstream fin("input.dat");
    ofstream fout("output.dat");
    int t;
    fin >> t;
    for(int test = 1; test <=t; test++){
        string str;
        fin >> str;
        int val2 = brute(str);


        fout << "Case #" << test<<": " << val2 << endl;

    }
    fout.close();
}
