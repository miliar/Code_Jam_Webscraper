#include<iostream>
#include <cstdio>
using namespace std;
int N;

int main(){
    if (fopen("input.txt", "r")) freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin>>N;
    for (int k =1; k<=N; k++){
        int r1,r2;
        cin>>r1;
        int a[4];
        int x;
        for (int i = 1; i<=4; i++){
            for (int j =0; j<4; j++){
                cin>>x;
                if (i==r1) a[j] = x;
            }
        }
        cin>>r2;
        int cnt = 0;
        int curnum;
        for (int i =1; i<=4; i++){
            for (int j=0; j<4; j++){
                cin>>x;
                if (i==r2){
                    for (int c = 0; c < 4; c++){
                        if (x==a[c]){
                            cnt++;
                            curnum = a[c];
                        }
                    }
                }
            }
        }
        cout<<"CASE #"<<k<<": ";
        if (cnt == 0) cout<< "Volunteer cheated!"<<endl;
        else if (cnt>1) cout<<"Bad magician!"<<endl;
        else cout<<curnum<<endl;
    }
    return 0;
}
