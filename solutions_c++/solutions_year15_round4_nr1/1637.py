#include <iostream>
#include <iosfwd>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cassert>
#include <cctype>
#include <vector>
#include <bitset>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <deque>
#include <algorithm>
#include <string>
#include <list>
#include <iterator>
#include <sstream>
#include <complex>
#include <fstream>
#include <functional>
#include <numeric>
#include <utility>

using namespace std;
/*****************************************macros************************************/
#define TYPE(m,a) __typeof(a) m = a
#define FOR(i,a,b) for(TYPE(i,(a)); i < (b); ++i)
#define DFOR(i,a,b) for(TYPE(i,(a)); i >= (b); --i)
#define ZFOR(i,N) FOR(i,0,N)
#define DZFOR(i,N) FOR(i,N,0)
#define SORT(x) sort((x).begin() , (x).end())
#define PB(x) push_back((x))
#define FORALL(it,v) for(TYPE(it, (v).begin()); it != (v).end(); ++it)
#define S2C(st, c) for(int i=0;i<st.size();i++) c[i] = st[i];
#define IA2CA(ia, ca, l) for(int i=0;i<l;i++) ca[i] = i2c(ia[i]);
#define CA2IA(ca, ia, l) for(int i=0;i<l;i++) ia[i] = c2i(ca[i]);
#define fout(x) cout<<"Case #"<<i+1<<": "<<x<<endl;
#define cfout(x) {cout<<"Case #"<<i+1<<": "<<x<<endl; continue;}
/****************************************typedefs**********************************/
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<VI> VVI;
typedef vector<VD> VVD;
typedef vector<VS> VVS;
typedef vector<long long> VL;
typedef vector<VL> VLL;
typedef vector<bool> VB;
typedef vector<VB> VBB;
/*****************************************Math************************************/
bool isPrime(int a){ if(a <= 1) return false; if(a == 2) return false;
	if(a%2 == 0) return false; for(int i=3;i<sqrt(a);i+=2) if(a%i == 0) return false; return true; }
int GCD(int a,int b){ if(b==0) return a; return GCD(b,a%b);}
int LCM(int a,int b){return a*b/GCD(a,b);}
int getInt() { int x=0; scanf("%d",&x); return x;}

/*************************************Input Output*******************************/
char getChar(){ char x=' '; scanf("%c",&x); return x;}
string getString(){char c[1024]=""; scanf("%s",c); return c;}
long long getLong(){long long x= 0; scanf("%lld",&x); return x;}
void fileIO(){freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);}
void sfileIO(){freopen("C-small-attempt0.in","r",stdin); freopen("C-small-attempt0.out","w",stdout);}
void lfileIO(){freopen("C-large.in","r",stdin); freopen("C-large.out","w",stdout);}

/********************************char, int, string, array************************/
int c2i(char c){int i=0; i=(int)c; i=i-48; if(i>=0 && i<=9) return i; else return -1;}
char i2c(int i){char c; c=(char)i; c=c+'0'; if(i>=0 && i<=9) return c; else return '0';}

//char* c2i(char c){int i=0; i=(int)c; i=i-48; if(i>=0 && i<=9) return i; else return -1;}

int countchar(string s,char c){int i=0;for(int j=0;j<s.length();j++) if(s[j] == c) i++; return i; }
vector<string> ex2s(string s, char c){vector<string> vs; string tmp=""; for(int i=0;i<s.length();i++){
    if(s[i]==c){vs.PB(tmp); tmp=""; continue;} tmp=tmp+s[i];} if(tmp!="") vs.PB(tmp); return vs;}

string ia2s(int a[],int sz){string c=""; stringstream ss; for(int i=0;i<sz;i++){ss<<a[i];} ss>>c; return c;}
int* s2ia(string s,int ar[50]){ar[0]=0;for(int i=1;i<=s.length();i++){ ar[i]=c2i(s[i-1]); ar[0]++;} return ar;}

string ca2s(char a[],int sz){string c=""; stringstream ss; for(int i=0;i<sz;i++){ss<<a[i];} ss>>c; return c;}
//macro for string to character array
string c2s(char a){string c=" "; c[0]=a; return c;}
/****************************************cases************************************/
char toup(char c){ if(c>='a' && c<='z') return c-' '; return NULL;}
char tolo(char c){ if(c>='A' && c<='Z') return c+' '; return NULL;}
char toswap(char c){ if(c>='A' && c<='Z') return c+' '; else if(c>='a' && c<='z') return c-' '; return NULL;}
#define PRINT2D(array, maxr, maxc) cout<<endl<<#array<<":   "; for(int i=0; i < (maxr); i++) { for(int j=0;j<(maxc);j++) cout<<array[i][j]<<"  "; if(i!=(maxr) - 1)cout<<endl<<#array<<":   ";}

const int INFIN = 1000000000;
/*********************************************************************************
WELCOME TO CODING

*********************************************************************************/
/*****************************user defined functions*****************************/


/***********************************main*****************************************/

int main(int argc, char** argv)
{
   //fileIO();
   int allTests;
   cin>>allTests;


   for(int eachTest=1; eachTest<=allTests; eachTest++){
    /**Logic goes here*/
    int r, c;
    cin>>r>>c;
    char arr[r+1][c+1];
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            cin>>arr[i][j];
        }
    }

    int carr[4][r+1][c+1];
    for(int i=0;i<4;i++){
        for(int j=0;j<r;j++){
            for(int k=0;k<c;k++){
                carr[i][j][k] = 0;
            }
        }
    }
    for(int i=0;i<r;i++){
        carr[0][i][0] = 0;
        carr[1][i][c-1] = 0;
    }
    for(int i=0;i<c;i++){
        carr[2][0][i] = 0;
        carr[3][r-1][i] = 0;
    }
//PRINT2D(arr, r, c);

    for(int i=0;i<r;i++){
        for(int j=1;j<c;j++){
            if(arr[i][j-1]!='.'){
                carr[0][i][j] = 1 + carr[0][i][j-1];
            } else carr[0][i][j] = carr[0][i][j-1];
        }
    }
//PRINT2D(carr[0], r, c);
    for(int i=0;i<r;i++){
        for(int j=c-2;j>=0;j--){
            if(arr[i][j+1]!='.'){
                carr[1][i][j] = 1 + carr[1][i][j+1];
            } else carr[1][i][j] = carr[1][i][j+1];
        }
    }
 //PRINT2D(carr[1], r, c);
    for(int i=0;i<c;i++){
        for(int j=1;j<r;j++){
            if(arr[j-1][i]!='.'){
                carr[2][j][i] = 1 +  carr[2][j-1][i];
            } else carr[2][j][i] = carr[2][j-1][i];
        }
    }
 //PRINT2D(carr[2], r, c);
    for(int i=0;i<c;i++){
        for(int j=r-2;j>=0;j--){
            if(arr[j+1][i]!='.'){
                carr[3][j][i] = 1 +  carr[3][j+1][i];
            } else carr[3][j][i] = carr[3][j+1][i];
        }
    }





    //PRINT2D(carr[3], r, c);
    int change = 0;
    int imposs = 0;
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            char c = arr[i][j];
            if(c!='.'){
                bool flag  = true;
                if(c=='^' && carr[2][i][j]==0){
                    change++;
                    //cout<<i<<"  "<<j;
                    flag = false;
                }
                if(c=='<' && carr[0][i][j]==0){
                    change++;
                     //cout<<i<<"  "<<j;
                    flag = false;
                }
                if(c=='>' && carr[1][i][j]==0){
                    change++;
                     //cout<<i<<"  "<<j;
                    flag = false;
                }
                if(c=='v' && carr[3][i][j]==0){
                    change++;
                     //cout<<i<<"  "<<j;
                    flag = false;
                }

                if(!flag){
                    int sm = 0;
                    for(int k=0;k<4;k++){
                        sm += carr[k][i][j];
                    }
                    if(sm==0){
                        imposs = 1;
                    }
                }
            }
        }
    }
    if(imposs){
        cout<<"Case #"<<eachTest<<": "<<"IMPOSSIBLE";
        /**Print ans here**/
        cout<<endl;
    } else {
        cout<<"Case #"<<eachTest<<": "<<change;
        /**Print ans here**/
        cout<<endl;
    }
   }

   return 0;
}
