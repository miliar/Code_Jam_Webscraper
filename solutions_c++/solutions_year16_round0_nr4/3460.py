#include <iostream>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

class BigInteger{
private:
    string number;
public:
    BigInteger();//empty constructor
    BigInteger(string s);//string constructor
    BigInteger(int n);//int constructor
    void setNumber(string s);
    const string& getNumber();//retrieves number
    BigInteger operator + (BigInteger b);
    BigInteger operator * (BigInteger b);
private:
    string add(string number1, string number2);
    string multiply(string n1, string n2);
};

BigInteger BIexponencial (BigInteger number, int exp){
    BigInteger aux(1);

    for(int i = 1; i<=exp; i++){
        aux = aux*number;
    }
    return aux;
}

int main(){
    int T;
    int caso =1;
    cin >> T;

    while(T--){
        int k,c,s;
        cin >> k >> c >> s;

        cout << "Case #" << caso++ << ":";
        if (k>s)
            cout << " IMPOSSIBLE\n";
        else{
            //calcula gap
            //int gap = pow(k, (c-1) );
            BigInteger gap(k);
            BigInteger one(1);
            gap = BIexponencial(gap,c-1);

            for(int i =0; i<s; i++){
                //escreve saída através do gap*i + 1
                BigInteger aux(i);
                aux = gap*aux;
                aux = aux + one;
                cout << " " << aux.getNumber();
            }
            cout << "\n";
        }
    }
    return 0;
}

//empty constructor
BigInteger::BigInteger(){
    number = "0";
}
//string constructor
BigInteger::BigInteger(string s){
    setNumber(s);
}

//int constructor
BigInteger::BigInteger(int n){
    stringstream ss;
    string s;
    ss << n;
    ss >> s;

    setNumber(s);
}

//set number
void BigInteger::setNumber(string s){
    number = s;
}

//get number
const string& BigInteger::getNumber(){
    return number;
}

BigInteger BigInteger::operator + (BigInteger b){
    BigInteger addition;

    //add numbers
    addition.setNumber( add(getNumber(), b.getNumber() ));

    return addition;
}

string BigInteger::add(string number1, string number2) {
    string add = (number1.length() > number2.length()) ?  number1 : number2;
    char carry = '0';
    int differenceInLength = abs( (int) (number1.size() - number2.size()) );

    if(number1.size() > number2.size())
        number2.insert(0, differenceInLength, '0'); // put zeros from left

    else// if(number1.size() < number2.size())
        number1.insert(0, differenceInLength, '0');

    for(int i=number1.size()-1; i>=0; --i) {
        add[i] = ((carry-'0')+(number1[i]-'0')+(number2[i]-'0')) + '0';

        if(i != 0) {
            if(add[i] > '9') {
                add[i] -= 10;
                carry = '1';
            } else
                carry = '0';
        }
    }
    if(add[0] > '9') {
        add[0]-= 10;
        add.insert(0,1,'1');
    }
    return add;
}

BigInteger BigInteger::operator * (BigInteger b) {
    BigInteger mul;

    mul.setNumber( multiply(getNumber(), b.getNumber() ) );

    return mul;
}

string BigInteger::multiply(string n1, string n2) {
    if(n1.length() > n2.length())
        n1.swap(n2);

    string res = "0";
    for(int i=n1.length()-1; i>=0; --i) {
        string temp = n2;
        int currentDigit = n1[i]-'0';
        int carry = 0;

        for(int j=temp.length()-1; j>=0; --j) {
            temp[j] = ((temp[j]-'0') * currentDigit) + carry;

            if(temp[j] > 9) {
                carry = (temp[j]/10);
                temp[j] -= (carry*10);
            } else
                carry = 0;

            temp[j] += '0'; // back to string mood
        }

        if(carry > 0)
            temp.insert(0, 1, (carry+'0'));

        temp.append((n1.length()-i-1), '0'); // as like mult by 10, 100, 1000, 10000 and so on

        res = add(res, temp); // O(n)
    }

    while(res[0] == '0' && res.length()!=1) // erase leading zeros
        res.erase(0,1);

    return res;
}

