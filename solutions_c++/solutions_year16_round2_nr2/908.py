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
    freopen("Bs.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;

    scanf("%d", &tc);

    for(int tcid = 0; tcid<tc; tcid++){
        cin >> A >> B;
        N = A.size();

        int a = UR;
        int b = UR;
        int score = UR;
        printf("Case #%d: ", tcid+1);
        if(N == 1){
            for(int i = 0; i<=9; i++){
                for(int j = 0; j<=9; j++){
                    if(flagSET(A,i) && flagSET(B, j)){

                        if(!check(i, j)){
                            continue;
                        }

                        int subt = abs(i-j);
                        if(subt < score){
                            score = subt;
                            a = i;
                            b = j;
                        } else if (subt == score){
                            if(i < a){
                                a = i;
                            } else if (i == a){
                                if(j < b){
                                    b = j;
                                }
                            }
                        }
                    }
                }
            }

            printf("%d %d\n",a,b);
        } else if (N == 2){

            for(int i = 0; i<=99; i++){
                for(int j = 0; j<=99; j++){
                    if(flagSET(A,i) && flagSET(B, j)){


                        if(!check(i, j)){
                            continue;
                        }

                        int subt = abs(i-j);
                        if(subt < score){
                            score = subt;
                            a = i;
                            b = j;
                        } else if (subt == score){
                            if(i < a){
                                a = i;
                            } else if (i == a){
                                if(j < b){
                                    b = j;
                                }
                            }
                        }
                    }
                }
            }

            printf("%02d %02d\n",a,b);


        } else if (N == 3){

            for(int i = 0; i<=999; i++){
                for(int j = 0; j<=999; j++){
                    if(flagSET(A,i) && flagSET(B, j)){

                        if(!check(i, j)){
                            continue;
                        }

                        int subt = abs(i-j);
                        if(subt < score){
                            score = subt;
                            a = i;
                            b = j;
                        } else if (subt == score){
                            if(i < a){
                                a = i;
                            } else if (i == a){
                                if(j < b){
                                    b = j;
                                }
                            }
                        }
                    }
                }
            }

            printf("%03d %03d\n",a,b);

        }


    }

    return 0;
}