#include<iostream>
using namespace std;

int main() {
    int T, row1, row2;
    int arr1[4], arr2[4];
    int tmp;
    cin>>T;
    
    for (int num = 1; num <= T; ++ num) {
        cin>>row1;
        for(int i = 0; i < 4; ++ i) {
            if (i == row1 - 1) {
                for (int j = 0; j < 4; ++ j) {
                    cin>>arr1[j];
                }
            }
            else {
                for (int j = 0; j < 4; ++ j) {
                    cin>>tmp;
                }
            }
        }
        
        cin>>row2;
        for(int i = 0; i < 4; ++ i) {
            if (i == row2 - 1) {
                for (int j = 0; j < 4; ++ j) {
                    cin>>arr2[j];
                }
            }
            else {
                for (int j = 0; j < 4; ++ j) {
                    cin>>tmp;
                }
            }
        }
        
        int count = 0;
        for (int i = 0; i < 4; ++ i) {
            for (int j = 0; j < 4; ++ j) {
                if (arr1[i] == arr2[j]) {
                    ++ count;
                    tmp = arr1[i];
                }
            }
        }
        
        cout<<"Case #"<<num<<": ";
        if (1 == count) {
            cout<<tmp<<endl;
        }
        else if (1 < count) {
            cout<<"Bad magician!"<<endl;
        }
        else {
            cout<<"Volunteer cheated!"<<endl;
        }
    }
}