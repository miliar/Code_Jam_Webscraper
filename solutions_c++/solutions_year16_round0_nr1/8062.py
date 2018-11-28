#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("/home/aman/Downloads/input.in","r",stdin);
    freopen("/home/aman/Downloads/output.txt","w",stdout);
    int t;
    cin >> t;
    for(int test=1;test<=t;test++){
        int N;
        cin >> N;

        if(N==0){
            cout << "Case #" << test << ": INSOMNIA" << endl;
        }
        else {
            set<int>S;
            int i=1;
            while(S.size()!=10){
                long long int temp = i*N;
                while(temp){
                    S.insert(temp%10);
                    temp/=10;
                }
                i+=1;
            }
            cout << "Case #" << test << ": " << (i-1)*N << endl;
        }
    }
    return 0;
}