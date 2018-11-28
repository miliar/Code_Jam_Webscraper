#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string>
#include <assert.h>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
const double pi=acos(-1.0);
const double eps=1e-11;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define LENGTH(A) ((int)A.length())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)

void print_vector(vector<string> &v){
    for(int i = 0; i < v.size(); i++)
         cout<<v[i]<<" ";
}

void reverse_para(string a){
    vector<string> n;
    string d = "";
    for(int i = 0; i < a.length(); i++){
        if(a[i] != ' ')
            d += a[i];
        if(a[i] == ' ' || (i == a.length()-1)){
            n.push_back(d);
            d = "";
        }
    }
    reverse(n.rbegin(), n.rend());
    print_vector(n);
}

string toString(int a){
    stringstream ss;
    ss<<a;
    string b = ss.str();
    return b;
}

int main()
{
    FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("sheep-small.out", "w", stdout);
    int t = 0;
    cin>>t;
    while(t--){
        int n = 0, d = 0;
        static int j = 1;
        string b = "";
        cin>>n;
        if(n == 0){
            cout<<"Case #"<<j<<": INSOMNIA"<<"\n";
            j++;
        }

        vector<int> v = {0,1,2,3,4,5,6,7,8,9};

        for(int i = 1; i < 1000000; i++){
            d = i*n;
            string b = toString(d);
             for(int i = 0; i < b.length(); i++){
                int k = b[i]-48;
                v.erase(remove(v.begin(), v.end(), k), v.end());
                k = 0;
             }
             b = "";
             if(v.empty()){
                cout<<"Case #"<<j<<": "<<d<<"\n";
                j++;
                break;
             }
             else{
                continue;
             }
        }

    }





	return 0;
}

