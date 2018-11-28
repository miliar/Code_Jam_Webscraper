#include <bits/stdc++.h>
using namespace std;
#define FL(a) memset(a, 0, sizeof a);
#define pi(a) cout <<  a << endl;
#define si(n) scanf("%d",&n)
#define pis(n) printf("%d ",n);
#define FREP(b) for(int i=0;i<b;i++)
#define REP(a,b,c) for(int a=b;a<c;a++)
typedef pair<int,int> ii;
typedef long long LL;
/*
struct data{
};
bool operator < (const data &a1, const data &a2){
}
*/
vector<double> Na, Ke;
int n;
int w1(){
    int n1 = 0, n2 = 0, N = n;
    int ans = 0;
    while(n1 < n && n2 < N){
        if(Na[n1] > Ke[n2]){
            ans++;
            n2++;
        }
        else{
            N--;
        }
        n1++;
    }
    return ans;
}
int w2(){
    int n1 = 0, n2 = 0;
    int ans = 0;
    while(n1 < n && n2 < n){
        //cout << "Jere " << Na[n1]  << " " << Ke[n2] << endl;
        if(Na[n1] > Ke[n2]){
            ans++;
        }
        else{
            n1++;
        }
        n2++;
    }
    return ans;
}
int main(){
    int tc,t=0;
    cin >> tc;
    while(tc--){
        Na.clear(), Ke.clear();
        double a;
        cin >> n;
        FREP(n){
            cin >> a;
            Na.push_back(a);
        }
        FREP(n){
            cin >> a;
            Ke.push_back(a);
        }
        sort(Na.begin(), Na.end());
        sort(Ke.begin(), Ke.end());
        cout << "Case #" << t+1 << ": " << w1() << " " << w2() << endl;
        t++;
    }
    return 0;
}
