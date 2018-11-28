#include<bits/stdc++.h>
using namespace std;
int arrr[1000005];
#define ll long long int
#define VI vector<int>
#define VLL vector<long long int>
#define PQI priority_queue<int>
#define PQLL priority_queue<long long int>
#define VP vector<pair<int,int> >
#define II pair<int,int> 
#define ll long long int
#define mem(in,rem) memset(in,rem,sizeof(in)) 
#define mp make_pair 
#define sol first
#define Y second
#define pb push_back
#define rep(i,in,b) for(int i=in;i<b;i++)
 
string dp[1005];
long long int inp[3000],n;

typedef pair<int, ll> pl;

string A, B;
int N;

map<pl, int> memo;

#define UR (1<<28)
/*Use like- 
rep(i,0,n - 1)
*/
template<class T> T pwr(T b, T pr){T r=1,sol=b;while(pr){if(pr&1)r*=sol;sol*=sol;pr=(pr>>1);}return r;}

#define sc second

bool flagSET(string s11, int idx){
    while(idx){
        if(s11.back() == '?'){
            idx/=10;
            s11.pop_back();
            continue;
        }

        if(s11.back() == (idx % 10) + '0'){
            idx/=10;
            s11.pop_back();
            continue;
        } else {
            return false;
        }
        
    }
    return true;
}

bool check(int n1, int n2){
    string strA = A;
    string strB = B;
    int sz = N;
    while(sz--){
        int digA = n1 % 10;
        int digB = n2 % 10;

        if(strA.back() != '?'){
            if(strA.back() != digA + '0'){
                return false;
            }
        }

        if(strB.back() != '?'){
            if(strB.back() != digB + '0'){
                return false;
            }
        }

        strA.pop_back();
        strB.pop_back();
        n1/=10;
        n2/=10;
    }
    return true;

}


int main(){
      freopen("Cs.txt", "r", stdin);
    freopen("outputl.txt", "w", stdout);
    int T; 
    cin >> T;

    for(int i=0;i<T;i++){
      
        printf("Case #%d: ",i+1);
        string x[16],y[16];
        int f1[16],f2[16];
        int n; 
        cin >> n;
        map<string,int>map1,N;
        for(int i=0;i<n;i++){
            cin >> x[i] >> y[i];
            map1[x[i]] = 0;
            N[y[i]] = 0;
        }
        int nx = 1;
        for(map<string,int>::iterator it=map1.begin();it!=map1.end();it++){
            it->sc = nx++;
        }
        nx = 1;
        for(map<string,int>::iterator it=N.begin();it!=N.end();it++){
            it->sc = nx++;
        }
        for(int i=0;i<n;i++){
            
            f1[i] = map1[x[i]];
            f2[i] = N[y[i]];
        }
        int ans[(1<<16)+5]={}; fill(ans,ans+(1<<n),-100000);
        ans[0] = 0;
        for(int i=0;i<(1<<n);i++){
            int LBIT=0,RBIT=0;
            for(int j=0;j<n;j++){
                if(((i>>j)&1)){
                    LBIT |= (1<<f1[j]);
                    RBIT |= (1<<f2[j]);
                }
            }
            for(int j=0;j<n;j++){
                if(!((i>>j)&1)){
                    int check = ( (LBIT|(1<<f1[j]))==LBIT && (RBIT|(1<<f2[j]))==RBIT );
                    ans[i+(1<<j)] = max(ans[i+(1<<j)],ans[i]+check);
                }
            }
        }
        
        cout << ans[(1<<n)-1] << endl;
    }
}