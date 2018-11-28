#include <iostream>
#include <cmath>
#include <vector>
using namespace std;


vector<int> palindromy;


long long bla(double x){
	if (modf(x,0)>=.5)
		return x>=0?ceil(x):floor(x);
	else
		return x<0?ceil(x):floor(x);
}

bool ispal(long long a){
    long long input = a;
    long long rev =0;
    long long dig =0;
    while(a > 0){
        dig = a % 10;
        rev = rev * 10 + dig;
        a = a/10;
    }
    return (input == rev ? true : false);
}

void znajdzpal(){
    double akt;
    long long zaokr;
    for(long long i = 1; i <= 1000; ++i){
        akt = sqrt(i);
        zaokr = static_cast<int>(akt);
        if(zaokr - akt == 0){
            if(ispal(zaokr) && ispal(i)){
                palindromy.push_back(i);
            }
        }
    }
}

void alg(){
    long long min, max;
    long long licznik = 0;
    cin >> min >> max;
    long long i = 0;
    while(palindromy[i] < min)
        i++;
    licznik = 0;
    while(palindromy[i] != palindromy.back() && palindromy[i] <= max){
        licznik ++;
        i++;
    }
    if(palindromy[i] <= max){
        licznik++;
    }
    cout << licznik << endl;
}


int main() {
    znajdzpal();
    int t;
    cin >> t;
    for (int case_no = 1; case_no <= t; ++case_no) {
        cout << "Case #" << case_no << ": ";
        alg();
    }
    cin.get();
    cin.get();
}
