#include <bits/stdc++.h>

#define mt make_tuple
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<string> vs;

void flip(vi &v, int i, int k){
    for(int j = i ; j < i+k ; j++){
        v[j] = 1-v[j];
    }
}

void test(){
    string s;
    cin >> s;
    vi v(s.length(),0);
    for(int i = 0 ; i < s.length() ; i++)
        v[i] = (s[i] == '+' ? 1 : 0);
    int k;
    cin >> k;
    int flips = 0;
    for(int i = 0 ; i < v.size()-k+1 ; i++){
        if(v[i] == 0){
            flip(v,i,k);
            flips++;
        }
    }
    for( int i : v){
        if(i == 0){
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    }
    cout << flips << endl;
        
}

int main(){
    int t;
    cin >> t;
    for( int i = 1;i<= t;i++){
        cout << "Case #" << i << ": ";
        test();
    }
	return 0;
}
