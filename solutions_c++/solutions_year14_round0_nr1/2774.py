#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int cnt;
    cin>>cnt;
    for(int t=1; t<=cnt; ++t) {
        int row1, row2;
        int d;
        cin>>row1;
        vector<int> vect1(17, 0);
        for(int r=1; r<=16; ++r) {
            cin >> d;
            if(r>(row1-1)*4 && r<=row1*4) {
                vect1[d] = 1;
            }
        }
        cin>>row2;
        vector<int> vect2(17, 0);
        for(int r=1; r<= 16; ++r) {
            cin >> d;
            if(r>(row2-1)*4 && r<=row2*4) {
                vect2[d] = 1;
            }
        }
        int res = -1;
        bool badMagician = false;
        for(int i=1; i<17; ++i) {
            if(vect1[i]==1 && vect2[i]==1) {
                if(res==-1) {
                    res = i;
                } else {
                    badMagician = true;
                }
            }
        }
        if(res == -1) {
            cout<<"Case #"<<t<<": Volunteer cheated!"<<endl;
        } else if(badMagician) {
            cout<<"Case #"<<t<<": Bad magician!"<<endl;
        } else {
            cout<<"Case #"<<t<<": "<<res<<endl;
        }
    }
    return 0;
}
