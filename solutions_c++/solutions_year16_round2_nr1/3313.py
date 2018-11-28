#include <iostream>
#include <tuple>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>

#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;
typedef vector<vi> vvi;
typedef long long i64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;
typedef pair<i64, i64> pi64;
typedef double ld;


int main() {
    int T;
    cin >> T;
    string number[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
    int numberIndexOrder[] = {0,6,8,7,2,5,4,9,1,3};
    for1(tc, T) {
        cout << "Case #" << tc << ": ";
        string S;
        cin >> S;

        int numberIndex = 0;
        int arr[10];
        fill_n(arr,10,0);
        while(S.length() > 0){ 
        	string num = number[numberIndexOrder[numberIndex]];
        	forn(i,num.length()){
        		int found = S.find(num[i]);
        		if(found == string::npos){
        			if (i != 0)
        				S = S + num.substr(0,i);
		        	numberIndex++;
	        		break;
        		}
        		S.replace(found,1, "");

        		if(i+1 == num.length())
        			arr[numberIndexOrder[numberIndex]]++;
        	}
        }
        forn(i,10){
            forn(j,arr[i]){
                cout << i;
            }
        }
        cout << '\n';
    }
    return 0;
}
