/*
 * Bidhan Roy
 * University of Dhaka
 */

using namespace std;

#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <ctime>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define rep(i,n) for(__typeof(n) i=0; i<(n); i++)
#define foreach(i,n) for(__typeof((n).begin())i =(n).begin();i!=(n).end();i++)
#define inf (1<<30)
#define eps 1e-9
#define pb push_back
#define ins insert
#define mp make_pair
#define sz(x) ((int)x.size())
#define clr clear()
#define all(x) x.begin(),x.end()
#define xx first
#define yy second
#define sqr(x) ((x)*(x))
#define mem(x,val) memset((x),(val),sizeof(x));
#define read(x) freopen(x,"r",stdin);
#define rite(x) freopen(x,"w",stdout);

template <class T> inline T __in() { T v; cin>>v; return v; }

#define Q __in<int>()
#define QQ __in<i64>()
#define QS __in<st>()

typedef long long i64;
typedef unsigned long long ui64;
typedef string st;
typedef vector<int> vi;
typedef vector<st> vs;
typedef map<int,int> mii;
typedef map<st,int> msi;
typedef map<int,st> mis;
typedef set<int> si;
typedef set<st> ss;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

struct Bigint {

    // representations and structures

    string a; // to store the digits

    int sign; // sign = -1 for negative numbers, sign = 1 otherwise



    // constructors

    Bigint() {} // default constructor

    Bigint( string b ) { (*this) = b; } // constructor for string



    // some helpful methods

    int size() { // returns number of digits

        return a.size();

    }

    Bigint inverseSign() { // changes the sign

        sign *= -1;

        return (*this);

    }

    Bigint normalize( int newSign ) { // removes leading 0, fixes sign

        for( int i = a.size() - 1; i > 0 && a[i] == '0'; i-- )

            a.erase(a.begin() + i);

        sign = ( a.size() == 1 && a[0] == '0' ) ? 1 : newSign;

        return (*this);

    }



    // assignment operator

    void operator = ( string b ) { // assigns a string to Bigint

        a = b[0] == '-' ? b.substr(1) : b;

        reverse( a.begin(), a.end() );

        this->normalize( b[0] == '-' ? -1 : 1 );

    }



    // conditional operators

    bool operator < ( const Bigint &b ) const { // less than operator

        if( sign != b.sign ) return sign < b.sign;

        if( a.size() != b.a.size() )

            return sign == 1 ? a.size() < b.a.size() : a.size() > b.a.size();

        for( int i = a.size() - 1; i >= 0; i-- ) if( a[i] != b.a[i] )

            return sign == 1 ? a[i] < b.a[i] : a[i] > b.a[i];

        return false;

    }

    bool operator == ( const Bigint &b ) const { // operator for equality

        return a == b.a && sign == b.sign;

    }




    // mathematical operators

    Bigint operator + ( Bigint b ) { // addition operator overloading

        if( sign != b.sign ) return (*this) - b.inverseSign();

        Bigint c;

        for(int i = 0, carry = 0; i<a.size() || i<b.size() || carry; i++ ) {

            carry+=(i<a.size() ? a[i]-48 : 0)+(i<b.a.size() ? b.a[i]-48 : 0);

            c.a += (carry % 10 + 48);

            carry /= 10;

        }

        return c.normalize(sign);

    }

    Bigint operator - ( Bigint b ) { // subtraction operator overloading

        if( sign != b.sign ) return (*this) + b.inverseSign();

        int s = sign; sign = b.sign = 1;

        if( (*this) < b ) return ((b - (*this)).inverseSign()).normalize(-s);

        Bigint c;

        for( int i = 0, borrow = 0; i < a.size(); i++ ) {

            borrow = a[i] - borrow - (i < b.size() ? b.a[i] : 48);

            c.a += borrow >= 0 ? borrow + 48 : borrow + 58;

            borrow = borrow >= 0 ? 0 : 1;

        }

        return c.normalize(s);

    }

    Bigint operator * ( Bigint b ) { // multiplication operator overloading

        Bigint c("0");

        for( int i = 0, k = a[i] - 48; i < a.size(); i++, k = a[i] - 48 ) {

            while(k--) c = c + b; // ith digit is k, so, we add k times

            b.a.insert(b.a.begin(), '0'); // multiplied by 10

        }

        return c.normalize(sign * b.sign);

    }

    Bigint operator / ( Bigint b ) { // division operator overloading

        if( b.size() == 1 && b.a[0] == '0' ) b.a[0] /= ( b.a[0] - 48 );

        Bigint c("0"), d;

        for( int j = 0; j < a.size(); j++ ) d.a += "0";

        int dSign = sign * b.sign; b.sign = 1;

        for( int i = a.size() - 1; i >= 0; i-- ) {

            c.a.insert( c.a.begin(), '0');

            c = c + a.substr( i, 1 );

            while( !( c < b ) ) c = c - b, d.a[i]++;

        }

        return d.normalize(dSign);

    }

    Bigint operator % ( Bigint b ) { // modulo operator overloading

        if( b.size() == 1 && b.a[0] == '0' ) b.a[0] /= ( b.a[0] - 48 );

        Bigint c("0");

        b.sign = 1;

        for( int i = a.size() - 1; i >= 0; i-- ) {

            c.a.insert( c.a.begin(), '0');

            c = c + a.substr( i, 1 );

            while( !( c < b ) ) c = c - b;

        }

        return c.normalize(sign);

    }




    // output method

    void print() {

        if( sign == -1 ) putchar('-');

        for( int i = a.size() - 1; i >= 0; i-- ) putchar(a[i]);

    }

};


#define mx 0

char temp[1000000];

Bigint odd(i64 a,i64 b){
    b=a+max(b-1,0LL)*2LL;
    a-=2;
    //cout<<a<<" "<<b<<endl;
    sprintf(temp,"%lld",a);
    Bigint A;
    A=temp;
    Bigint Ans;
    Ans=A;
    //Ans.print(); cout<<endl;
    Bigint ONE;
    ONE="1";
    A=A+ONE;
    Ans=Ans*A;
    //Ans.print(); cout<<endl;
    A=A+ONE;
    Ans=Ans*A;
    //Ans.print(); cout<<endl;
    ONE="6";
    Ans=Ans/ONE;
    //cout<<"--->"<<endl;
    //Ans.print(); cout<<endl;

    sprintf(temp,"%lld",b);
    A=temp;
    Bigint Ans2;
    Ans2=A;
    //cout<<"----"<<endl;
    //Ans2.print(); cout<<endl;
    ONE="1";
    A=A+ONE;
    //cout<<">>>"<<endl;
    //A.print(); cout<<endl;
    Ans2=Ans2*A;
    //Ans2.print(); cout<<endl;
    A=A+ONE;
    Ans2=Ans2*A;
    //Ans2.print(); cout<<endl;
    ONE="6";
    Ans2=Ans2/ONE;
//Ans2.print(); cout<<endl;
    return Ans2-Ans;
}

Bigint All(i64 a,i64 am){
    Bigint ONE,TWO,SIX,Ans,A;
    ONE="1";
    TWO="2";
    sprintf(temp,"%lld",max(a-1,0LL));

    A=temp;
    Ans=A;

    A=A+ONE;
    Ans=Ans*A;

    A=temp;
    A=A*TWO;
    A=A+ONE;

    Ans=Ans*A;

    SIX="6";

    Ans=Ans/SIX;

    Bigint Ans2;
    sprintf(temp,"%lld",(a+am-1));

    A=temp;
    Ans2=A;

    A=A+ONE;
    Ans2=Ans2*A;

    A=temp;
    A=A*TWO;
    A=A+ONE;

    Ans2=Ans2*A;

    //SIX="6";

    Ans2=Ans2/SIX;
    return Ans2-Ans;
}

Bigint calc(i64 r,i64 am){
    Bigint ret;
    ret=All(r,am*2);
    i64 tr=r;
    if(r%2==0) r++;
    Bigint Odd;
    Odd=odd(r,am);
    Bigint Even;
    Even=ret-Odd;
    //cout<<r<<","<<am<<endl;
    //cout<<"all="; ret.print(); cout<<endl;
    //cout<<"Odd="<<endl;
    //Odd.print();
    //cout<<endl;
    //cout<<"Even="<<endl;
    //Even.print();
    //cout<<endl;
    if(tr%2) return Even-Odd;
    return Odd-Even;
}
const long double pi=M_PI;
int main(){
    ios_base::sync_with_stdio(0);
    //All(3,5).print(); cout<<endl;
	read("in.txt");
	rite("out.txt");
	double cl = clock();
    cl = clock() - cl;
    int test=Q,kas=0;
    while(test--){
        i64 r,t;
        cin>>r>>t;
        //cout<<r<<" "<<t<<endl;
        //cout<<"t="<<t<<endl;
        //t=ceil((long double)((long double)(t)/pi));
        sprintf(temp,"%lld",t);
        Bigint T;

        //T.print();
        //cout<<endl;
        //cout<<"--"<<endl;
        T=temp;
        i64 ans=0;
        i64 lo=1, hi=10000000000000000LL;
        while(lo<=hi){
            i64 mid=(lo+hi)/2;
            //cout<<"mid="<<mid<<endl;
            //cout<<"mid="<<mid<<endl;
            Bigint now=calc(r,mid);

            //cout<<lo<<" "<<hi<<" "<<mid<<" = ";
            //cout<<"now="<<endl;
            //now.print(); cout<<endl;
            //T.print(); cout<<endl;
            if(T<now) hi=mid-1;
            else{
                lo=mid+1;
                ans=max(ans,mid);
            }
        }
        cout<<"Case #"<<++kas<<": ";
        cout<<ans<<endl;
    }
	fprintf(stderr, "-------------------------------\nTotal Execution Time = %lf seconds\n\n", cl / CLOCKS_PER_SEC);
	return 0;
}
