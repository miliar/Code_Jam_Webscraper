#include <iostream>
#include <cstdio>
#include <string>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;

#define MAX 201
typedef pair<int,int> PII;
typedef long long int64;


/*
 * BigInteger Class, performs basic arithmetic operations of very large integers.
 * Copyright (C) 2011  Mahmoud Mechehoul
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

//#include <iostream>
//#include <algorithm>

//using namespace std;

/* This is a minimized version of the BigInteger class meant to be
 * used for single file development purposes (such as programming contests).
 * For a complete documentation on what every method does please refer to
 * the class header file 'BigInteger.h'.
 */
class BigInteger {
//private:
public:
	string integer;
	BigInteger(unsigned int integer);
	BigInteger(string integer);
	BigInteger();
	void setInteger(unsigned int integer);
	void setInteger(string integer);
	unsigned int getIntValue() const;
	string toString() const;
	BigInteger addInteger(const BigInteger& integer_to_add) const;
	BigInteger addInteger(const string& integer_to_add) const;
	BigInteger subInteger(const BigInteger& integer_to_add) const;
	BigInteger subInteger(const string& integer_to_add) const;
	BigInteger multiplyInteger(const BigInteger& integer_to_multiply) const;
	BigInteger multiplyInteger(const string& integer_to_multiply) const;
	static size_t getTrimIndex(const string& integer);
	bool operator==(const BigInteger& integer) const;
	bool operator<(const BigInteger& integer) const;
	bool operator<=(const BigInteger& integer) const;
	BigInteger operator+(const BigInteger& integer) const;
	BigInteger operator-(const BigInteger& integer) const;
	BigInteger operator*(const BigInteger& integer) const;
	friend ostream& operator<<(ostream& in, BigInteger& integer);
};

//int main() {

	// INSERT YOUR CODE HERE

	/* This is a sample code that demonstrates how to use the
	 * Big Integer arithmetic library.
	 *
	 * BigInteger a("35742549198872617291353508656626642567");
	 * BigInteger b("1298074214633706835075030044377087");
	 *
	 * BigInteger c = a + b;
	 * BigInteger d = a * b;
	 *
	 * cout << a << " + " << b << " = " << c << endl;
	 * cout << a << " * " << b << " = " << d << endl;
	 */

//	return 0;
//}

BigInteger::BigInteger(unsigned int integer) {
	setInteger(integer);
}

BigInteger::BigInteger(string integer) {
	for (int i = 0; i < (int)integer.size() && integer[i] >= '0' && integer[i] <= '9'; i++) {
		this->integer += integer[i];
	}

	if (this->integer.size() == 0) {
		this->integer = "0";
	} else {
		this->integer = integer.substr(getTrimIndex(integer));
	}
}

BigInteger::BigInteger() {
    setInteger(0);
}

void BigInteger::setInteger(unsigned int integer) {
	if (integer == 0) this->integer = "0";

	while (integer) {
		this->integer = (char)((integer % 10) + '0') + this->integer;
		integer /= 10;
	}
}

void BigInteger::setInteger(string integer) {
	this->integer = integer;
}

unsigned int BigInteger::getIntValue() const {
	unsigned int ret = 0;
	unsigned int biggest = 0xFFFFFFFF;
	for (int i = 0; i < (int)integer.size(); i++) {
		int unit = integer[i] - '0';
		if (ret > (biggest - unit) / 10.0) return 0;
		ret = ret * 10 + unit;
	}
	return ret;
}

string BigInteger::toString() const {
	return integer;
}

BigInteger BigInteger::addInteger(const BigInteger& integer_to_add) const {
	int a_n = max((int)(integer_to_add.toString().size() - toString().size()), 0);
	int b_n = max((int)(toString().size() - integer_to_add.toString().size()), 0);
	string a = string(a_n, '0') + toString();
	string b = string(b_n, '0') + integer_to_add.toString();

	reverse(a.begin(), a.end());
	reverse(b.begin(), b.end());

	string result; int carry = 0;

	for (int i = 0; i < (int)a.size(); i++) {
	   int sum = (a[i] - '0') + (b[i] - '0') + carry;
	   result += ((char)(sum % 10 + '0'));
	   carry = sum / 10;
	}

	if (carry != 0) result += ((char)(carry + '0'));

	reverse(result.begin(), result.end());

	return BigInteger(result.substr(getTrimIndex(result)));
}

BigInteger BigInteger::subInteger(const BigInteger& integer_to_add) const {
	int a_n = max((int)(integer_to_add.toString().size() - toString().size()), 0);
	int b_n = max((int)(toString().size() - integer_to_add.toString().size()), 0);
	string a = string(a_n, '0') + toString();
	string b = string(b_n, '0') + integer_to_add.toString();

	reverse(a.begin(), a.end());
	reverse(b.begin(), b.end());

	string result; int carry = 0;

	for (int i = 0; i < (int)a.size(); i++) {
	   int sum = (a[i] - '0') - (b[i] - '0')-carry;
	   carry=0;
       if (sum<0){
           sum+=10;
           carry=1;
       }//  + carry;
	   result += ((char)(sum + '0'));
	   //carry = sum / 10;
	}

	if (carry != 0) result += ((char)(carry + '0'));

	reverse(result.begin(), result.end());

	return BigInteger(result.substr(getTrimIndex(result)));
}

BigInteger BigInteger::addInteger(const string& integer_to_add) const {
	return addInteger(BigInteger(integer_to_add));
}

BigInteger BigInteger::subInteger(const string& integer_to_add) const {
	return subInteger(BigInteger(integer_to_add));
}

BigInteger BigInteger::multiplyInteger(const BigInteger& integer_to_multiply) const {
	string a = integer_to_multiply.toString();
	string b = toString();

	reverse(a.begin(), a.end());
	reverse(b.begin(), b.end());

	BigInteger ret("0");

	for (int i = 0; i < (int)a.size(); i++) {
		int carry = 0; string tmp = string(i, '0');

		for (int j = 0; j < (int)b.size(); j++) {
			int mul = (a[i] - '0') * (b[j] - '0') + carry;
			tmp += ((char)(mul % 10 + '0'));
			carry = mul / 10;
		}

		if (carry != 0) tmp += (carry + '0');

		reverse(tmp.begin(), tmp.end());

		ret = ret.addInteger(tmp.substr(getTrimIndex(tmp)));
	}

	return ret;
}

BigInteger BigInteger::multiplyInteger(const string& integer_to_multiply) const {
	return multiplyInteger(BigInteger(integer_to_multiply));
}

size_t BigInteger::getTrimIndex(const string& integer) {
	size_t index = 0;
	while (integer[index] == '0' && index < integer.size() - 1) index++;
	return index;
}

bool BigInteger::operator==(const BigInteger& integer) const {
	return this->integer == integer.toString();
}

bool BigInteger::operator<(const BigInteger& integer) const {
	string s=this->integer;
    string t=integer.toString();
    //cout<<s<<"<"<<t<<endl;
    if (s.length()<t.length()) return true;
    if (s.length()>t.length()) return false;
    for (int i=0; i<s.length(); i++){
        if (s[i]<t[i]) return true;
        if (s[i]>t[i]) return false;
    }
    return false;
}

bool BigInteger::operator<=(const BigInteger& integer) const {
	return (*this < integer) || (*this == integer) ;
}


BigInteger BigInteger::operator+(const BigInteger& integer) const {
	return addInteger(integer);
}

BigInteger BigInteger::operator-(const BigInteger& integer) const {
	return subInteger(integer);
}

BigInteger BigInteger::operator*(const BigInteger& integer) const {
	return multiplyInteger(integer);
}

ostream& operator<<(ostream& in, BigInteger& integer) {
	in << integer.toString();

	return in;
}

//------- solution code

char s[MAX];
int palin(BigInteger x){
    //sprintf(s,"%lld",x);
    string ss=x.toString();
    //cout<<ss<<"]"<<endl;
    int i=0,j=ss.length()-1;//strlen(s)-1;
    while(i<j && ss[i]==ss[j]){ i++; j--; }
    if (i<j) return 0;
    return 1;
}

BigInteger memo[101][10];
int flag[101][10];


BigInteger cc2(int budget, int len, BigInteger &x, int shift, BigInteger y){
    if ((x.integer.length()==2*len-1&&x<y*y)||budget<0) return BigInteger(0);
    if (2*shift>=len){
        //cout<<x<<">"<<y<<"^2="<<(y*y).toString()<<endl;
        return BigInteger(1);
    }
    if ((x.integer.length()>2*len-1)){
        if (flag[len-2*shift][budget])
            return memo[len-2*shift][budget];
    }
    BigInteger c(0);
    c=c+cc2(budget-0,len,x,shift+1,y);
    y.integer[shift]=y.integer[len-1-shift]='1';
    c=c+cc2(budget-(1+(shift<(len-1-shift)))*1*1,len,x,shift+1,y);
    y.integer[shift]=y.integer[len-1-shift]='2';
    c=c+cc2(budget-(1+(shift<(len-1-shift)))*2*2,len,x,shift+1,y);
    if ((x.integer.length()>2*len-1)){
        memo[len-2*shift][budget]=c;
        flag[len-2*shift][budget]=1;
    }
    return c;
}

BigInteger cc(int budget, int len, BigInteger &x){
    BigInteger c(0);
    if (len==1)
        c=c+min((int)sqrt((int)x.getIntValue()),3)+1;
    else{
        c=c+cc(budget,len-1,x);
        c=c+cc2(budget-2,len,x,1,BigInteger(string("1")+string(len-2,'0')+"1"));
        c=c+cc2(budget-8,len,x,1,BigInteger(string("2")+string(len-2,'0')+"2"));
    }
    return c;
}

int main(){
    int64 t,u,n,m,i,j,a,b,c;
    cin>>t;
    string sa,sb;
    for (i=0; i<101; i++) for (j=0; j<=9; j++) flag[i][j]=0; 
    for (u=0; u<t; u++){
        cout<<"Case #"<<(u+1)<<": ";
        cin>>sa>>sb;
        BigInteger aa(sa),bb(sb); //if (bb<aa) swap(aa,bb);
        /*c=0;
        for (BigInteger ii(1); (ii*ii)<=bb; ii=ii+1){
            if (palin(ii) && palin(ii*ii) && aa<=ii*ii && ii*ii<=bb){
                //cout<<c<<" : "<<ii<<" "<<(ii*ii).toString()<<endl;
                c++;
            }
        }
        cout<<c<<endl;
        */
        aa=aa-1;
        cout<<(cc(9,(1+bb.toString().length())/2,bb)-cc(9,(1+aa.toString().length())/2,aa)).toString()<<endl;
    }
    return 0;
}
