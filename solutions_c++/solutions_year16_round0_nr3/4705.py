#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

int getNumCases(){
    int a;
    cin >> a;
    return a;
}

long long getTrivialDivisor(long long n){
    if(n <= 3)
        return true;
    long long sq_n = sqrt(n);
    //cout << "Square Root " << sq_n << endl;
    for(long long i=2; i<=sq_n ; ++i){
        //cout << "N:" << n << " i:" << i << " Modulus:" << n%i << endl;
        if(n%i == 0){
            return i;
        }
    }
    return -1;
}

string generateJamCoines(int & cv, int length){
    string binary = bitset<32>(cv).to_string();
    string s = "1" + binary.substr(binary.length()-length+2) + "1";
    cv++;
    return s;
}

long long convertToInt(string s, int base){
    long long result = 0;
    for(int i=s.length()-1; i>=0; --i){
        char c = s.at(i);
        if(c == '1'){
            result+=pow(base, s.length()-1 - i);
        }
    }
    return result;
}

bool isValidJamCoin(string s){
    vector<long long> tds;
    for(int i=2;i<=10;++i){
        long long intRep = convertToInt(s, i);
        //cout << s << " Base " << i << " is "<< intRep << endl;
        long long td = getTrivialDivisor(intRep);
        if(td==-1){
            return false;
        }
        tds.push_back(td);
    }
    cout << s;
    for(int i=0; i<tds.size(); ++i){
        cout << " " << tds.at(i);
    }
    cout << endl;
    return true;
}

void generateValidJamCoines(int n, int j){
    int cv = 0;
    int coinCount = 0;
    while(coinCount < j){
        string coin = generateJamCoines(cv, n);
        if(isValidJamCoin(coin))
            ++coinCount;
    }
}

void enumerateCases(vector<pair<int, int> > v){
    for(unsigned long i=0; i<v.size(); ++i){
        pair<int,int> p = v.at(i);
        cout << "Case #" << i+1 << ":" << endl;
        generateValidJamCoines(p.first, p.second);
    }
}

vector<pair <int,int> > generateInputVector(){
    int numCases = getNumCases();
    vector<pair<int,int>> v;
    for(int i=0; i<numCases; ++i){
        int n,j;
        cin >> n;
        cin >> j;
        v.push_back(make_pair(n,j));
    }
    return v;
}

void stdinPancakes(){
    enumerateCases(generateInputVector());
}

int main() {
    //stdinPancakes();
    enumerateCases(vector<pair<int,int> >{make_pair(16,50)});
    return 0;
}