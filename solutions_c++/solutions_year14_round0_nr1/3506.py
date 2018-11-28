#include<iostream>
#include<cstdio>

using namespace std;

int main() {
    int T,ans,arr[4][4],selectedArray[4],i,j,flag =0,num,k;

    freopen("A-small-attempt0.in", "r", stdin);
    freopen("1.out", "w", stdout);

    cin>>T;
    for(k = 1 ; k <= T ; k++) {
            flag = 0;
        cin>>ans;

        for(i = 0 ; i < 4 ; i++) {
            for(j = 0 ; j < 4 ; j++) {
                cin>>arr[i][j];
            }
        }
        for(j = 0 ; j < 4 ; j++) {
            selectedArray[j] = arr[ans-1][j];
        }

        cin>>ans;

        for(i = 0 ; i < 4 ; i++) {
            for(j = 0 ; j < 4 ; j++) {
                cin>>arr[i][j];
            }
        }

        for(i = 0 ; i < 4 ; i++) {
            for(j = 0 ; j < 4 ; j++) {
               if(selectedArray[i] == arr[ans-1][j]) {
                    flag++; num = selectedArray[i];
               }
            }
        }

        if(flag != 0) {
            if(flag > 1) {
                cout<<"Case #"<<k<<": "<<"Bad magician!\n";
            } else {
                cout<<"Case #"<<k<<": "<<num<<"\n";
            }
        } else {
            cout<<"Case #"<<k<<": "<<"Volunteer cheated!\n";
        }
    }
    return 0;
}
