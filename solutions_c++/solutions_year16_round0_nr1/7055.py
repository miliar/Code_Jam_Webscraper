#include <iostream>
#include <fstream>
using namespace std;
long n, t, seenCount, j = 1;

long seen[10];
void process(int n){
    while(n){
        if(seen[n%10]==0){
            seen[n%10]++;
            seenCount++;
        }
        n=n/10;
    }
}
void resetSeen(){
    for (int i = 0; i < 10; ++i) {
        seen[i] = 0;
    }
    seenCount = 0;
    j = 1;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin>>t;
    int i = 1;
    while(t--){
        cin>>n;

        while(seenCount<10){
            process(j*n);
            j++;
            if(j > 100){
                cout<<"Case #"<<i++<<": "<<"INSOMNIA"<<endl;
                break;
            }
        }
        if(j<=100){
            j--;
            cout<<"Case #"<<i++<<": "<<j*n<<endl;
        }
        resetSeen();
    }
    return 0;
}