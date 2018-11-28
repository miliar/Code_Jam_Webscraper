#include <iostream>
#include <stdio.h>

using namespace std;

int l1[4], l2[4], r[4];

void readLineR() {
    int i = 0;
    while(i < 4) {
        cin>>r[i];
        i++;
    }
}
void readLineL1() {
    int i = 0;
    while(i < 4) {
        cin>>l1[i];
        i++;
    }
}
void readLineL2() {
    int i = 0;
    while(i < 4) {
        cin>>l2[i];
        i++;
    }
}

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int N, lr, n = 1;
    cin>>N;
    while(N--) {
        cin>>lr;
        for(int i = lr - 1; i > 0; i--) {
            readLineR();
        }
        readLineL1();
        for(int i = 4 - lr; i > 0; i--) {
            readLineR();
        }
        cin>>lr;
        for(int i = lr - 1; i > 0; i--) {
            readLineR();
        }
        readLineL2();
        for(int i = 4 - lr; i > 0; i--) {
            readLineR();
        }
        int counter = 0, tmp;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                if(l1[i] == l2[j]) {
                    counter++;
                    tmp = l1[i];
                }
            }
        }
        cout<<"Case #"<<n;
        switch(counter) {
            case 0:
                cout<<": Volunteer cheated!"<<endl;
                break;
            case 1:
                cout<<": "<<tmp<<endl;
                break;
            default:
                cout<<": Bad magician!"<<endl;
        }
        n++;
    }
    return 0;
}
