#include <iostream>
#include <math.h>
#include <vector>
using namespace std;
long long int findDivisor(long long int n){
    long long int end = (long long int)sqrt(n);
    for(long long int i=2;i!=end+1;i++){
        if(n%i == 0)
            return i;
    }
    return -1;
}
long long int baseChange(int base,long long int n){
    long long int x = n;
    long long int result = 0;
    long long int multer = 1;
    for(int i=0;x!=0;i++){
        result += x%10*multer;
        multer *= base;
        x /= 10;
    }
    return result;
}
int main(){
    int n;
    cin >> n;
    for(int i=0;i!=n;i++){
        int N,J;
        cin >> N >> J;
        cout << "Case #" << i+1 << ":" << endl;
        long long int x = (long long int)pow(10,N-1)+1;
        for(int j=0;j!=J;j++){
            bool isCoinJam = true;
            vector<long long int> divs;
            for(int base = 2;base!=11;base++){
                long long int y = findDivisor(baseChange(base,x));
                if(y == -1){
                    isCoinJam = false;
                    break;
                }
                divs.push_back(y);
            }
            if (isCoinJam){
                cout << x;
                for(int c=0;c!=9;c++){
                    cout << " " << divs[c];
                }
                cout << endl;
            }
            else{
                j--;
            }
            x = baseChange(2,x) + 2;
            long long int bet = x;
            x = 0;
            long long int multer = 1;
            for(int c=0;bet!=0;c++){
                x += bet%2*multer;
                multer*=10;
                bet /= 2;
            }
        }
    }
    return 0;
}