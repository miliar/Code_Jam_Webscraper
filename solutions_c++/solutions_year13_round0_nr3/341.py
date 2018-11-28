#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <bitset>
#include <numeric>
#include <algorithm>
#include <functional>
using namespace std;

const inline int __GET_INT(){int ret;scanf("%d",&ret);return ret;}
#define INPT_INT __GET_INT()

typedef long long LL;

int len, mid;
string A,B,S;
bool can_be_equal;
int dp[102][55][11][2][2][3];

int updated_sum(int i, int sum, int d)
{
    if( len/2 == i ) return sum + d*d;
    return sum + 2*d*d;
}

int calc(int i, int sum, bool equal, int flag)
{
    if( sum > 9 )
    {
        return 0;
    }
    if( i > mid )
    {
        if( equal && !can_be_equal && !flag ) return 0;
        if( equal && flag == 2 ) return 0;
        return sum > 0;
    }

    int &ret = dp[len][i][sum][equal][can_be_equal][flag];

    if(ret != -1)
    {
        return ret;
    }
    ret = 0;

    if( equal )
    {
        for(int j = S[i];j>='0';--j)if( i || (j-'0') )
        {
            if( j == S[i] )
            {
                if( S[len-i-1] > j ) flag = 1;
                else if( S[len-i-1] < j ) flag = 2;

                ret += calc(i+1,updated_sum(i,sum,j-'0'),true,flag);
            }
            else
            {
                ret += calc(i+1,updated_sum(i,sum,j-'0'),false,flag);
            }
        }
    }
    else
    {
        for(int j = 3;j>=0;--j) ret += calc(i+1,updated_sum(i,sum,j),equal,flag);
    }
    return ret;
}

int call_dp(string A, bool eq)
{
    memset(dp,-1,sizeof(dp));
    S = A;
    len = A.size();
    if( len%2 ) mid = len/2;
    else mid = len/2-1;
    can_be_equal = eq;
    return calc(0,0,true,0);
}

#define DEPTH 10
typedef int bignum_t[1010];
int comp(const bignum_t a, const int c, const int d, const bignum_t b)
{
    int i, t = 0, O = -DEPTH * 2;
    if (b[0] - a[0] < d && c)
        return 1;
    for (i = b[0]; i > d; i--)
    {
        t = t * DEPTH + a[i - d] * c - b[i];

        if (t > 0)
            return 1;
        if (t < O)
            return 0;
    }
    for (i = d; i; i--)
    {
        t = t * DEPTH - b[i];
        if (t > 0)
            return 1;
        if (t < O)
            return 0;
    }
    return t>0;
}
void sub(bignum_t a, const bignum_t b, const int c, const int d)
{
    int i, O = b[0] + d;
    for (i = 1 + d; i <= O; i++)
        if ((a[i] -= b[i - d] * c) < 0)
            a[i + 1] += (a[i] - DEPTH + 1) / DEPTH,a[i] -= (a[i] - DEPTH + 1)
                        / DEPTH * DEPTH;
    for (; a[i] < 0; a[i + 1] += (a[i] - DEPTH + 1) / DEPTH,a[i] -= (a[i] - DEPTH + 1)
            / DEPTH * DEPTH,i++);
    for (; !a[a[0]] && a[0] > 1; a[0]--);
}
void Sqrt(bignum_t b, bignum_t a)
{
    int h, l, m, i;
    memset((void*) b, 0, sizeof(bignum_t));
    for (i = b[0] = (a[0] + 1) >> 1; i; sub(a, b, m, i - 1), b[i] += m, i--)
        for (h = DEPTH - 1, l = 0, b[i] = m = (h + l + 1) >> 1; h > l; b[i] =
                    m = (h + l + 1) >> 1)
            if (comp(b, m, i - 1, a))
                h = m - 1;
            else
                l = m;
    for (; !b[b[0]] && b[0] > 1; b[0]--);
    for (i = 1; i <= b[0]; b[i++] >>= 1);
}

string get_sqrt(string str)
{
    bignum_t a,b;
    a[0]=str.size();
    for(int i=1; i<=a[0]; i++)
        a[i]=str[a[0]-i]-'0';
    Sqrt(b,a);
    string ret = "";
    for(int i=b[0]; i>=1; i--) ret += b[i]+'0';
    return ret;
}

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

int main()
{
    freopen("C-large-2.in","r",stdin);
    freopen("C-large-2.out","w",stdout);

    int T = INPT_INT;

    LL pre[101] = {0};
    string s = "";
    for(int i = 1;i<100;++i)
    {
        s += '9';
        pre[i] = pre[i-1] + call_dp(s,true);
    }

    for(int ca = 1;ca<=T;++ca)
    {
        cin>>A>>B;

        Bigint tmp(A);

        A = get_sqrt(A);
        B = get_sqrt(B);

        Bigint tmp1(A);
        tmp1 = tmp1*tmp1;

        int low, high;

        if( tmp == tmp1 )
        {
            low = call_dp(A,false) + pre[A.size()-1];
        }
        else low = call_dp(A,true) + pre[A.size()-1];

        high = call_dp(B,true) + pre[B.size()-1];

        printf("Case #%d: %d\n",ca,high-low);
    }
    return 0;
}
