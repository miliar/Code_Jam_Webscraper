//*********************SHOPON(CODEHEAD)- UNIVERSITY OF ASIA PACIFIC *************************//
//******************************************************************************************//
//************************************Header Files*****************************************//
#include<bits/stdc++.h>

using namespace std;
//****************************************************************************************//
//************************************Macros*********************************************//
#define MAX 100000
#define pii pair< int, int >
#define FOR(i,A,B) for(int i = (A); i < (B); ++i)
#define sqr(num) ((num)*(num))
#define PI 3.1415926535897
#define pitr (2*acos(0))
#define lp 20071027
#define input() freopen("C:\\Users\\Bad-''CODEHEAD''-Ass\\Desktop\\input.txt","r",stdin);
#define output() freopen("C:\\Users\\Bad-''CODEHEAD''-Ass\\Desktop\\output.txt","w",stdout);
//#define input() freopen("/home/codehead/Desktop/input.txt","r",stdin);
//#define output() freopen("/home/codehead/Desktop/output.txt","w",stdout)
#define pf printf
#define REP(n) for(int i=0;i<n;i++)
#define VREP(i,n) for(int (i)=0;i<n;i++)
#define pb push_back
#define sc1(t) scanf("%d",&t)
#define sc2(a,b) scanf("%d%d",&a,&b)
#define sc3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define sc164(t) scanf("%lld",&t)
#define sc264(a,b) scanf("%lld%lld",&a,&b)
#define sc364(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define scstr(l) scanf("%[^\n]",l)
#define make(a,d) memset(a,d,sizeof(a))
#define lld long long int
#define print(x) printf("%d\n",x)
#define print64(x) printf("%lld\n",x)
#define printcase(x,n) printf("Case %d: %d\n",x,n)
#define printyn(x,s) printf("Case %d: %s\n",x,s)
#define debug(a, i) printf(#a "[%d] = %d\n", i, a[i]);
#define _i int
#define what_is(x) cerr << #x << " is " << x << endl;
#define MOD 1000000007
const lld INF = 0x7fffffff;

//*************************************************************************************************//
char __INPUT[25];
inline int _I() { scanf("%s",__INPUT); return atoi(__INPUT); }
inline long long int _LLD(){scanf("%s",__INPUT); return atoll(__INPUT);}
//************************************************************************************************//
//****************************************Templates**********************************************//
template<class T> inline bool isPrimeNumber(T n)
{if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}
template<class T>T gcd(T a,T b){return b == 0 ? a : gcd(b, a % b);}
template<typename T>T lcm(T a, T b) {return a / gcd(a,b) * b;}

template<class T>T power(T n,T p){if(p==0)return 1;T x=mpower(n,p/2);x=(x*x);if(p&1)x=(x*n);return x;} ///n to the power p
template <typename T>string NumberToString ( T Number ) {ostringstream ss;ss << Number;return ss.str(); }
_i stringtonumber(string S){
    _i N=1,X=S.size(),L=1;
    N=S[0]-48;
    while(L!=X){
        N=N*10;
        N=N+(S[L]-48);
        L++;
    }
    return N;
}

//*************************************************************************************************//
//************************************Bit Works***************************************************//
int Set(int N,int pos){return N=N | (1<<pos);}
int reset(int N,int pos){return N= N & ~(1<<pos);}
bool check(int N,int pos){return (bool)(N & (1<<pos));}
//************************************************************************************************//
//*************************************CharCheck*************************************************//
bool isUpperCase(char c){return c>='A' && c<='Z';}
bool isLowerCase(char c){return c>='a' && c<='z';}
bool isLetter(char c){return c>='A' && c<='Z' || c>='a' && c<='z';}
bool isDigit(char c){return c>='0' && c<='9';}

//************************************************************************************************//
//*************************************MOD WORKS*************************************************//
template <class T> inline T bigmod(T p,T e,T M){
    lld ret = 1;
    for(; e > 0; e >>= 1){
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    } return (T)ret;
}

template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}
//*************************************************************************************************//
//**************************************TypeDefs**************************************************//
typedef vector<int> _VINT;
typedef vector<lld> _VLLD;
typedef pair<int,int> _PAIR;
typedef vector<pair<int,int> > vpintint;
typedef vector<pair<string,int> > vpstringint;
typedef map<string,int> stringintmap;
typedef map<string,int> intstringmap;
typedef map<int,int> intintmap;
//*********************************************************************************************//
//***********************************CASE_INPUT***********************************************//
_i cases,cas=0;
void CAS()
{
    cases=_I();
}
#define CASE() CAS();while(cases--)
//************************************Neccessary Codes*****************************************//
//********************************************************************************************//
/*
    bool PRIME[10000009];
    void primecheck()
    {
        long long i,j,sq=sqrt(10000000);
        for(i=4;i<=10000000;i=i+2)
            PRIME[i]=1;
        for(i=3;i<=sq;i=i+2)
        {
            if(PRIME[i]==0)
            {
                for(j=i*i;j<=10000000;j=j+2*i)
                    PRIME[j]=1;
            }
        }
    }

    bool _SEARCH(int low,int high,int value)
    {
        while(low<=high)
        {
            int mid=(low+high)/2;
            if(a[mid]==value) return 1;
            else if(a[mid]<value)
                low=mid+1;
            else
                high=mid-1;
        }
        return 0;
    }

*/
void faltucode(){

}
//***************************************************************************************//
//***********************************Work Starts From Here******************************//
 /*
    _i cases,cas=0;
    sc1(cases);
    while(cases--)
    {

    }
*/

string S;
bool ONE(){

    bool A1=true,A2=true,A3=true;
    REP(S.size()){
        if(S[i]=='O'&& A1) { S[i]='-'; A1=false; }
        if(S[i]=='N'&& A2) { S[i]='-'; A2=false;}
        if(S[i]=='E'&& A3) { S[i]='-'; A3=false;}
    }
    if(A1 && A2 && A3) return true;
    return false;
}
bool TWO(){
    bool A1=true,A2=true,A3=true;
    REP(S.size()){
        if(S[i]=='T'&& A1) { S[i]='-'; A1=false; }
        if(S[i]=='O'&& A2) { S[i]='-'; A2=false;}
        if(S[i]=='W'&& A3) { S[i]='-'; A3=false;}
    }
    if(A1 && A2 && A3) return true;
    return false;
}
bool THREE(){
    bool A1=true,A2=true,A3=true,A4=true,A5=true;
    REP(S.size()){
        if(S[i]=='T'&& A1) { S[i]='-'; A1=false; }
        if(S[i]=='H'&& A2) { S[i]='-'; A2=false;}
        if(S[i]=='R'&& A3) { S[i]='-'; A3=false;}
        if(S[i]=='E'&& A4) { S[i]='-'; A4=false;}
        if(S[i]=='E'&& A5) { S[i]='-'; A5=false;}


    }
    if(A1 && A2 && A3 && A4 && A5) return true;
    return false;
}

bool FOUR(){
    bool A1=true,A2=true,A3=true,A4=true,A5=true;
    REP(S.size()){
        if(S[i]=='F'&& A1) { S[i]='-'; A1=false; }
        if(S[i]=='O'&& A2) { S[i]='-'; A2=false;}
        if(S[i]=='U'&& A3) { S[i]='-'; A3=false;}
        if(S[i]=='R'&& A4) { S[i]='-'; A4=false;}
        //if(S[i]=='E'&& A1) { S[i]='-'; A1=false; }


    }
    if(A1 && A2 && A3 && A4) return true;
    return false;
}

bool FIVE(){
    bool A1=true,A2=true,A3=true,A4=true,A5=true;
    REP(S.size()){
        if(S[i]=='F'&& A1) { S[i]='-'; A1=false; }
        if(S[i]=='I'&& A2) { S[i]='-'; A2=false;}
        if(S[i]=='V'&& A3) { S[i]='-'; A3=false;}
        if(S[i]=='E'&& A4) { S[i]='-'; A4=false;}
        //if(S[i]=='E'&& A1) { S[i]='-'; A1=false; }


    }
    if(A1 && A2 && A3 && A4) return true;
    return false;
}

bool SIX(){
    bool A1=true,A2=true,A3=true,A4=true,A5=true;
    REP(S.size()){
        if(S[i]=='S'&& A1) { S[i]='-'; A1=false; }
        if(S[i]=='I'&& A2) { S[i]='-'; A2=false;}
        if(S[i]=='X'&& A3) { S[i]='-'; A3=false;}
        //if(S[i]=='E'&& A1) { S[i]='-'; A1=false; }
        //if(S[i]=='E'&& A1) { S[i]='-'; A1=false; }


    }
    if(A1 && A2 && A3) return true;
    return false;
}

bool SEVEN(){
    bool A1=true,A2=true,A3=true,A4=true,A5=true;
    REP(S.size()){
        if(S[i]=='S'&& A1) { S[i]='-'; A1=false;}
        if(S[i]=='E'&& A2) { S[i]='-'; A2=false;}
        if(S[i]=='V'&& A3) { S[i]='-'; A3=false;}
        if(S[i]=='E'&& A4) { S[i]='-'; A4=false;}
        if(S[i]=='N'&& A5) { S[i]='-'; A5=false;}


    }
    if(A1 && A2 && A3 && A4 && A5) return true;
    return false;
}

bool EIGHT(){
    bool A1=true,A2=true,A3=true,A4=true,A5=true;
    REP(S.size()){
        if(S[i]=='E'&& A1) { S[i]='-'; A1=false; }
        if(S[i]=='I'&& A2) { S[i]='-'; A2=false;}
        if(S[i]=='G'&& A3) { S[i]='-'; A3=false;}
        if(S[i]=='H'&& A4) { S[i]='-'; A4=false;}
        if(S[i]=='T'&& A5) { S[i]='-'; A5=false;}


    }
    if(A1 && A2 && A3 && A4 && A5) return true;
    return false;
}

bool NINE(){
    bool A1=true,A2=true,A3=true,A4=true,A5=true;
    REP(S.size()){
        if(S[i]=='N'&& A1) { S[i]='-'; A1=false; }
        if(S[i]=='I'&& A2) { S[i]='-'; A2=false;}
        if(S[i]=='N'&& A3) { S[i]='-'; A3=false;}
        if(S[i]=='E'&& A4) { S[i]='-'; A4=false;}
       // if(S[i]=='T'&& A1) { S[i]='-'; A1=false; }


    }
    if(A1 && A2 && A3 && A4) return true;
    return false;
}

bool ZERO(){
    bool A1=true,A2=true,A3=true,A4=true,A5=true;
    REP(S.size()){
        if(S[i]=='Z'&& A1) { S[i]='-'; A1=false; }
        if(S[i]=='E'&& A2) { S[i]='-'; A2=false;}
        if(S[i]=='R'&& A3) { S[i]='-'; A3=false;}
        if(S[i]=='O' && A4) { S[i]='-'; A4=false;}
       // if(S[i]=='T'&& A1) { S[i]='-'; A1=false; }


    }
    if(A1 && A2 && A3 && A4) return true;
    return false;
}
void letsGo()
{
    input();
    output();
    CASE(){
        cin>>S;
        _i A[10];
        make(A,0);
        _i NN=0;
        REP(S.size()){
            if(S[i]=='Z'){
                A[0]++;
            }
            else if(S[i]=='X'){
                A[6]++;
            }
            else if(S[i]=='W'){
                A[2]++;
            }
            else if(S[i]=='G'){
                A[8]++;
            }
            else if(S[i]=='U'){
                A[4]++;
            }
        }

        if(A[0]){
            REP(A[0]){
                bool Ans=ZERO();
            }
        }
        if(A[2]){
            REP(A[2]){
                bool Ans=TWO();
            }
        }
        if(A[3]){
             REP(A[3]){
                bool Ans=THREE();
            }
        }
        if(A[4]){
             REP(A[4]){
                bool Ans=FOUR();
            }
        }

        if(A[6]){
             REP(A[6]){
                bool Ans=SIX();
            }
        }

        if(A[8]){
             REP(A[8]){
                bool Ans=EIGHT();
            }
        }


        for(int i=0;i<S.size();i++){
             if(S[i]=='R'){
                A[3]++;
            }
        }


        for(int i=0;i<S.size();i++){
            if(S[i]=='O'){
                A[1]++;
            }
            if(S[i]=='S'){
                A[7]++;
            }

        }
        if(A[3]){

            REP(A[3]){
                bool ans=THREE();
            }
        }
        if(A[1]){
            REP(A[1]){
                bool Ans=ONE();
            }
        }
        if(A[7]){
            REP(A[7]){
                bool Ans=SEVEN();
            }
        }
        //cout<<S<<endl;
        for(int i=0;i<S.size();i++){
            if(S[i]=='F'){
                A[5]++;
            }
            if(S[i]=='N'){
                A[9]++;
            }
        }
        if(A[5]){
            REP(A[5]){
                bool ans=FIVE();
            }
        }

        if(A[9]){
            A[9]/=2;
            for(int i=1;i<=A[9];i++){
                bool ans=NINE();
            }
        }
        pf("Case #%d: ",++cas);
        for(int i=0;i<10;i++){
            for(int j=1;j<=A[i];j++){
                if(i==0) pf("0");
                if(i==1) pf("1");
                if(i==2) pf("2");
                if(i==3) pf("3");
                if(i==4) pf("4");
                if(i==5) pf("5");
                if(i==6) pf("6");
                if(i==7) pf("7");
                if(i==8) pf("8");
                if(i==9) pf("9");

            }
        }
        pf("\n");

    }
}

int main(){
   // while(1){
    letsGo();
   // faltucode();
   // }
    return 0;

}
