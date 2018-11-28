#include <iostream>

using namespace std;

unsigned long gcd (unsigned long n1, unsigned long n2) {
    return (n2 == 0) ? n1 : gcd (n2, n1 % n2);
}

int main(){
    int T;
    string tmpStr;
    bool flag;
    long long a,b;
    cin >> T;
    
    
    for (int t1 = 1 ; t1 <= T ; t1++){
        cin >> tmpStr;
        flag = true;
        
        a = 0;
        b = 0;
        for (int i = 0 ; i < tmpStr.length(); i++){
            if (tmpStr[i] == '/'){
                flag = false;
                continue;
            }
            if (flag){
                a = a * 10 + (tmpStr[i] - '0');
            }
            else{
                b = b * 10 + (tmpStr[i] - '0');
            }
        }
        
        int g = gcd(a, b);
        if (g != 1){
            a /= g;
            b /= g;
        }
        
        int loop;
        for (loop =  0 ; loop < 62; loop++){
            if ((2 << loop) == b){
                break;
            }
        }
        if (loop != 62){
            int count = 0;
            while (a < b){
                count ++;
                a = a << 1;
            }
            cout << "Case #" << t1 << ": " << count << endl;
        }else{
            cout << "Case #" << t1 << ": impossible" << endl;
        }
        
        //cout << a << " " << b << endl;
        //cout << "CASE " << t1 << ": " << endl;
    }
    
    return 0;
}