#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <iomanip>
#include <sstream>
#include <cstring>
#include <cmath>

using namespace std;

typedef long long int ll;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;
typedef vector<bool> vb;
typedef vector<ll> vll;


bool isPalindrome(ll n){

    stringstream s;
    s<<n;
    string str;
    s>>str;
    string str_r = str;
    reverse(str_r.begin(),str_r.end());
    return str== str_r;
}

int main()
{
    // Listing all squares numbers less than 10**14 which are palindrome
    // whose root are palindromes too

    vll sq;
    ll n;
    ll lim = 10000000;

    for(n=1;n<=lim;n++){

        if(isPalindrome(n)){
            if(isPalindrome(n*n)){
                sq.push_back(n*n);
            }

        }

    }

//    ofstream out("palsquare");

//    for(int i=0; i< sq.size(); i++){
//        out<<sq[i]<<endl;
//    }

//    out.close();

//    return 0;

    int T;
    cin>>T;

    for(int c=1;c<=T;c++){

        ll A,B;
        cin>>A>>B;
        ll count = 0;

        for(int i=0; i<(int)sq.size();i++){

            if(sq[i]>=A && sq[i]<=B){
                count++;
            }
        }

        cout<<"Case #"<<c<<": "<<count<<endl;
    }



    return 0;
}
