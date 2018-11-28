#include <iostream>

using namespace std;
int main() {
    int tc, count=1;
    cin>>tc;
    while (tc--) {
        long long n;
        cin>>n;
        cout<<"Case #"<<count++<<": ";
        if (n==0) {
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        int arr[10] = {0};
        int c = 1;
        int a = 0;
        long long ans=-1;
        while (true) {
            long long temp = n*c;
            while (temp>0) {
                long long t = temp%10;
                if (arr[t] == 0){
                    arr[t]++;
                    a++;
                }
                temp/=10;
            }
            if (a == 10) {ans = n*c; break;}
            c++;
            if (c == 1000) {ans = -1; break;}
        }
        if (ans == -1) 
            cout<<"INSOMNIA"<<endl;
        else
            cout<<ans<<endl;
    }
    return 0;
}