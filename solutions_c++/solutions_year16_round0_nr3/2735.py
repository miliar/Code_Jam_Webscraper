#include<iostream>
#include <stdlib.h>
#include<list>
#include<string>
#include<cstring>
#include<sstream>
#include<cctype>
#include<string.h>
#include<algorithm>
#include<cmath>
#include<stack>
#include<fstream>
#include<cstdlib>
#include<vector>
#include<map>
#include<set>
#include<utility>
#include<iomanip>
#include<queue>

using namespace std;

#define INF (1<<29)
#define SET(a) memset(a,-1,sizeof(a))
#define ALL(a) a.begin(),a.end()
#define CLR(a) memset(a,0,sizeof(a))
#define FILL(a,v) memset(a,v,sizeof(a))
#define PB push_back
#define FOR(i,n) for(int i = 0;i<n;i++)
#define PI acos(-1.0)
#define EPS 1e-9
#define MP(a,b) make_pair(a,b)
#define min3(a,b,c) min(a,min(b,c))
#define mai3(a,b,c) mai(a,mai(b,c))
#define READ freopen("input.tit", "r", stdin)
#define WRITE freopen("output.tit", "w", stdout)
#define LL long long
#define Mi 1000000005
#define MX 10000007

#define F first
#define S second
#define pii pair<int,int>
#define p(i) printf("%d",i)
#define inp(i) scanf("%d",&i)
#define inpll(i) scanf("%lld",&i)
#define getci getchar_unlocked
/*inline void inp( int &n )
 {
 n=0;
 int ch=getci();int sign=1;
 while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getci();}
 
 while(  ch >= '0' && ch <= '9' )
 n = (n<<3)+(n<<1) + ch-'0', ch=getci();
 n=n*sign;
 }*/

using namespace std;

bool c[MX];
vector<LL> v;
void seive()
{
    c[0]=1;
    c[1]=1;
    //printf("%lld\n",l);
    for(int i=2;i<MX;i+=2)
    c[i]=1;
    for(int i=3;i<3164;i+=2)
    for(int j=i*i,d=i<<1;j<MX;j+=d)
    c[j]=1;
    v.push_back(2);
    for(int i=3;i<MX;i+=2)
    if(!c[i])
    v.push_back(i);
}

vector<int> getPrimeFactors(int val){
    vector<int> result;
    if(val < 0)
    return result;
    int idx = 0;
    while(val >= 1 && val >= v[idx]){
        if(!c[val]){
            result.PB(val);
            return result;
        }
        if(! (val%v[idx]) ){
            result.PB(v[idx]);
            val /= v[idx];
        }
        else{
            idx++;
        }
    }
    return result;
}

int getFirstDivisor(LL val) {
    for(int i=0; i<v.size(); i++) {
        if(val%v[i] == 0)
            return v[i];
    }
    return 1;
}

LL mulmod(LL a,LL b, LL c)
{
    LL x=0,y=a%c;
    while(b>0)
    {
        if(b%2==1)
        x=(x+y)%c;
        y=(y*2)%c;
        b/=2;
    }
    return x%c;
}
LL modulo(LL a,LL b,LL c)
{
    LL x=1,y=a;
    while(b>0)
    {
        if(b%2==1)
        x=(x*y)%c; //x = mulmod(x,y,c)
        y=(y*y)%c; // y =mulmod(y,y,c);
        b/=2;
    }
    return x%c;
}

//miller algo to find given number is prime or not
bool miller(LL p,int iteration)
{
    if(p<2)
    return false;
    if( p!=2 && p%2==0)
    return false;
    LL s=p-1;
    while(s%2==0)
    s/=2;
    for(int i=0;i<iteration;i++)
    {
        LL a=rand()%(p-1)+1,tmp=s;
        LL mod=modulo(a,tmp,p);
        while( tmp!=p-1 && mod!=1 && mod!=p-1 )
        {
            mod=mulmod(mod,mod,p);
            tmp*=2;
        }
        if(mod!=p-1 && tmp%2==0)
        return false;
    }
    return true;
}

LL getValueInBase(string s, LL base) {
    int len = s.length();
    LL number = 0;
    LL placeValue = 1;
    for (int i=len-1; i>=0; i--) {
        if (s[i]=='1') {
            number += placeValue;
        }
        placeValue *= base;
    }
    return number;
}


string getFirstNLengthNumber(int n) {
    string firstNumber = "1";
    for (int j=1;j<n-1;j++) {
        firstNumber += "0";
    }
    firstNumber += "1";
    return firstNumber;
}

string getLastNLengthNumber(int n) {
    string lastNumber = "1";
    for (int j=1;j<n-1;j++) {
        lastNumber += "1";
    }
    lastNumber += "1";
    return lastNumber;
}

string getNumberInBinaryForm(LL number) {
    string s = "";
    s.insert(0, "");
    while(number !=0) {
        int rem = number%2;
        if(rem==1) {
            s.insert(0, "1");
        }
        else {
            s.insert(0, "0");
        }
        number /= 2;
    }
    return s;
}

bool isNumberPrimeInAnyBase(LL number) {
    string s = getNumberInBinaryForm(number);
    for (int base=2; base<=10; base++) {
        LL n = getValueInBase(s, base);
        if (miller(n, 20)) {
            return true;
        }
    }
    return false;
}

bool printDivisorsOfAllBase(LL  number) {
    string s = getNumberInBinaryForm(number);
    string toPrint = "" + s + " ";
    for (int base=2; base<=10; base++) {
        LL n = getValueInBase(s, base);
        int divisor = getFirstDivisor(n);
        if(divisor == 1) {
            return false;
        }
        toPrint += to_string(divisor);
        toPrint += " ";
//        cout<<"Base : "<<base<<" V : "<<n<<" "<<" divisor : "<<divisors[0]<<endl;
    }
    cout<<toPrint<<endl;
    return true;
}

int main(){
//    cout<<getValueInBase("1000000000010001", 6)<<" isPrime : "<<miller(getValueInBase("101", 2), 3);
    
    int t;
    inp(t);
    seive();
    for(int i=0;i<t;i++){
        cout<<"Case #"<<i+1<<":\n";
        int n, j, numberFound = 0;
        inp(n);
        inp(j);
        string firstNumber = getFirstNLengthNumber(n);
        LL startingNumber = getValueInBase(firstNumber, 2);
        string lastNumber = getLastNLengthNumber(n);
        LL endingingNumber = getValueInBase(lastNumber, 2);

        LL currentNumber = startingNumber;
        while (currentNumber <= endingingNumber && numberFound < j) {
            if(!isNumberPrimeInAnyBase(currentNumber)) {
                if (printDivisorsOfAllBase(currentNumber))
                    numberFound++;
            }
            currentNumber += 2;
        }
        
    }
    return 0;
}