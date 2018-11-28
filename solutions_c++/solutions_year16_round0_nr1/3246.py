#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <climits>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i=0;i<n;i++)
#define INF INT_MAX/3
#define LINF LLONG_MAX/3
#define MP make_pair
#define PB push_back
#define ALL(v) (v).begin(),(v).end()

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

bool used[10];

bool init(){
    for(int i=0;i<10;i++) used[i] = false;
}

bool check(){
    for(int i=0;i<10;i++){
        if(!used[i]) return false;
    }
    return true;
}

void f(int n){
    while(n>0){
        used[n%10] = true;
        n /= 10;
    }
}

void solve(int mondai);

int main(){
    /*          //ここのテストから0以外の数字が入力されていれば必ずINSOMNIAでないことが証明されている
    for(int i=0;i<100;i++){
        init();
        int t = i;
        cout << t << "\t: ";
        int cnt=1;
        while(!check()){
            f(t*cnt);
            cnt++;
            if(cnt==1000){
                cout << "Fail ";
                break;
            }
        }
        cout << t * (cnt-1) << endl;
    }
    */

    /*
     *  1<=T<=200
     *  small : 0<=N<=200
     *  large : 0<=N<=1000000
     */
    int T;
    int mondai=1;
    cin >> T;
    for(int i=0;i<T;i++){
        init();
        solve(mondai);
        mondai++;
    }
}

void solve(int mondai){
    cout << "Case #" << mondai << ": ";
    ll N; cin>>N;
    if(N==0){
        cout << "INSOMNIA" << endl;
        return;
    }

    ll cnt=1;
    while(!check()){
        f(N*cnt);
        cnt++;
        if(cnt==1000){
            cout << "INSOMNIA" << endl;
            return;
        }
    }
    cout << N * (cnt-1L) << endl;
}
