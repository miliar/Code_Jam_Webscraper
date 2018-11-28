#include<bits/stdc++.h>
using namespace std;

typedef long long lli;

string intToStr(lli num){
    stringstream ss;
    ss<<num;
    return ss.str();
}

lli strToInt(string str){
    stringstream ss;
    ss<<str;
    lli num;
    ss>>num;
    return num;
}


lli translate(string num, lli base){
    reverse(num.begin(),num.end());
    lli pow = 1;
    lli out = 0;
    for(lli i = 0; i<num.size();i++){
        out += pow*((lli)(num[i]=='1'));
        pow *= base;
    }
    return out;
}

bool isPrime(lli num, lli* divisor){
    *divisor = 0;
    if(num <= 1) return false;
    lli a = 2;
    while(a*a<=num){
        if(num%a==0){*divisor = a; return false;}
        a++;
    }

    return true;
}

string intToBinary(lli num, lli len){
    string out = "";
    len--;
    while(len>=0){
        out += '0'+((int)((num&(1<<len)) == (1<<len)));
        len--;
    }

    return out;
}

string multistring(string str, lli n){
    string out = "";
    for(int i=0;i<n;i++){
        out += str;
    }
    return out;
}

string testNum(string numStr){
    bool notPrime = true;
    stringstream ss;
    vector<lli> divisors(9);
    for(lli base = 2; base<=10; base++){
        lli divisor;
        notPrime &= !isPrime(translate(numStr, base), &divisor);
        divisors[base-2] = divisor;
    }
    if(notPrime){
        ss<<numStr;
        for(int i = 0;i<divisors.size(); i++)ss<<" "<<divisors[i];ss<<endl;
    }

    return ss.str();
}


int main(){
    //ifstream in;in.open("B-large.in");
    ofstream out("C-small.out");
    //#define cin in
    #define cout out

    lli T, N,J;
    cin>>T;
    cin>>N>>J;
    string maxNumStr = multistring("1",N);

    cout<<"Case #1:"<<endl;
    lli amount = 0;
    lli num = 0;
    while(amount<J){
        /// Translate num into a jam coin
        string numStr = "1"+intToBinary(num, N-2)+"1";

        /// Check whether the jam coin is prime
        string line = testNum(numStr);
        if(line != ""){
            cout<<line;
            amount++;
        }

        /// Break when all the jam coins were tested
        if(maxNumStr == numStr)break;
        num++;
    }

    return 0;
}
