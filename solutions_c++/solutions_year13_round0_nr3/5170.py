#include <fstream>
#include <vector>
#include <iostream>
#include <cmath>

long long int palindromes[40];
using namespace std;
bool palindrom(long long int a){
    long long int num;
    long long int sum=0;
    int rev;
    num=a;
    while(num>0){
        rev=num%10;
        num=(num-rev)/10;
        sum=sum*10+rev;
    }
    if(sum==a) return true;
    else return false;
}

int pal(long long int A,long long int B){
    int count=0;
    for(int i=0;i<40;i++) if(A<= palindromes[i]*palindromes[i] && B>=palindromes[i]*palindromes[i] ) count ++;
    
    return count;
}

int main() {
    ifstream llegeix("C-large-1.in");
    ofstream escriu("sortida.out");
    long double max=1000000000000000;
    int iter=0;
    for(long long int i=1;i<sqrt(max);i++){
        if(palindrom(i)&&palindrom(i*i)){
            palindromes[iter]=i;
            cout << palindromes[iter] << endl;
            iter++;
        }
    }
    
    int T;
    long long int A;
    long long int B;
    llegeix >> T;
    for(int i=0;i<T;i++){
        cout << i << endl;
        llegeix >> A >> B;
        escriu << "Case #" << i+1 <<": " << pal(A,B) << endl;
    }
    
    llegeix.close();
    escriu.close();
}