#include <iostream>
#include <vector>
#include <utility>
#include <sstream>
using namespace std;

int main(){
    int t; cin>>t;
    for(int tt=0;tt<t;tt++){
        unsigned long long n;
        cin>>n;
        int s[10]={0};
        int sum=0;

        if(n==0){
            cout << "Case #" << tt+1 << ": " << "INSOMNIA" << endl;
            continue;
        }

        for(int i=1;sum<10;i++){
            stringstream ss; ss<<(i*n);
            string ns = ss.str();

//            cout << "n is " << n << endl;
 //           cout << "ns is " << ns << endl;

            for(int j=0;j<ns.size();j++){
                if(s[(int)(ns[j]-'0')]==0){
                    s[(int)(ns[j]-'0')]=1;
                    sum++;
                }
            }

            if(sum==10){
                cout << "Case #" << tt+1 << ": " << i*n << endl;
            }
        }
    }
}
