#include <iostream>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>

using namespace std;
int result[1000000+10];
int main() {
//cout<<"here"<<endl;
    freopen("A-large.in", "r", stdin);
    freopen("A-large-output.txt", "w", stdout);
    for(int i = 1; i <= 1000000; i++) {
            bool a[10];
            for(int i = 0; i < 10; i++) {
                a[i] = 0;
            }
        int counter = 0;
        for(int j = i; 1; j+=i) {
            int k = j;
            while(k > 0) {
                int d = k % 10;
                if(a[d] == 0) counter++;
                a[d] = 1;
                k = k / 10;
            }
            if(counter==10) {
                    result[i] = j;
                break;
            }
        }
    }

    int T;
    cin>>T;
    for(int tc = 1; tc <= T; tc++) {
        cout<<"Case #"<<tc<<": " ;
        int n;
        cin>>n;
        if(n==0) {
            cout<<"INSOMNIA"<<endl;
        }else {
            cout<<result[n]<<endl;
        }
    }

    return 0;
}
