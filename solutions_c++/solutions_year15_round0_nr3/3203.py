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

const int INFIN = 1000000000;
/*********************************************************************************
WELCOME TO CODING

*********************************************************************************/
/*****************************user defined functions*****************************/


/***********************************main*****************************************/

string mul[4][4] = {{"1", "i", "j", "k"},{"i", "-1", "k", "-j"},{"j", "-k", "-1", "i"},{"k", "j", "-i", "-1"}};

string multiple(string s1, string s2){
    //cout<<s1<<" * "<<s2<<" = ";
    int neg = 0;
    if(s1.size() == 2){
        neg = 1-neg;
        s1 = s1.substr(1,1);
    }
    if(s2.size() == 2){
        neg = 1-neg;
        s2 = s2.substr(1,1);
    }
    int i ,j;
   // cout<<neg<<"=+==+=+++=+=++"<<endl;
    if(s1 == "1") i=0;
    else if(s1=="i") i=1;
    else if(s1=="j") i=2;
    else if(s1=="k") i=3;

    if(s2 == "1") j=0;
    else if(s2=="i") j=1;
    else if(s2=="j") j=2;
    else if(s2=="k") j=3;
   // cout<<"("<<i<<", "<<j<<")";
    string s3 = mul[i][j];
   // cout<<"::::"<<s3<<" ";
    if(s3.size() == 2){
        neg = 1-neg;
        //cout<<neg<<"======================"<<endl;
        s3 = s3.substr(1,1);
    }

    if(neg) {
            //cout<<"-"<<s3<<endl;
            return "-"+s3;
    }
    else {
            //cout<<s3<<endl;
            return s3;
    }
}

int main(int argc, char** argv)
{
   fileIO();
   int allTests;
   cin>>allTests;

   for(int eachTest=1; eachTest<=allTests; eachTest++){
    int l,m;
    string s;
    cin>>l>>m>>s;
    string ans = "NO";
    vector<char> arr(l*m);
    //cout<<endl;
    if(l*m<3){

    } else {
            for(int i=0;i<m;i++){
                for(int j=0;j<l;j++){
                    arr[l*i + j] = s[j];
                    //cout<<arr[l*i + j];
                }
            }
            //cout<<endl;
            int m1=-1,m2=-1;
            if(arr[0]=='i'){
                m1 = 1;
            }
            if(arr[arr.size()-1]=='k'){
                m2 = arr.size()-2;
            }
            //cout<<m1<<" "<<m2<<"++++++++++++++++++++"<<endl;
            if(m1==-1){
                    string is = c2s(arr[0]);
                for(int i=1;i<arr.size();i++){
                    is = multiple(is, c2s(arr[i]));
                    if(is=="i"){
                        m1 = i+1;
                        break;
                    }
                }
            }
            //cout<<m1<<" "<<m2<<"--------------"<<endl;
            if(m2==-1){
                    string is = c2s(arr[arr.size()-1]);
                for(int i=arr.size()-2;i>=0;i--){
                        //cout<<"---------------------"<<i<<"  "<<endl;;
                    is = multiple(c2s(arr[i]),is);
                    if(is=="k"){
                        m2 = i-1;
                        break;
                    }
                }
            }
            //cout<<m1<<" "<<m2;
            if(m1<=arr.size()-2 && m2>=1 && m1<=m2 && m1>0 && m2>0){
                string is = c2s(arr[m1]);
                for(int i=m1+1;i<=m2;i++){
                    is = multiple(is, c2s(arr[i]));
                }
                if(is=="j"){
                    ans = "YES";
                }
            }
    }


    cout<<"Case #"<<eachTest<<": ";
    /**Print ans here**/
    cout<<ans;
    cout<<endl;
   }

   return 0;
}
