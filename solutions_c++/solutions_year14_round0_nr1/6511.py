#include <iostream>
#include <cstdio>
using namespace std;
int a[16];
int b[16];
int check(int t){
    int flag=-1;
    for(int i=1;i<=16;i++){
        if(a[i]==t&&b[i]==t){
            if(flag==-1)flag=i;
            else return 0;
        }
    }
    return flag;
}
int main(){
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int T,flag;
    cin >> T;
    for(int t=1;t<=T;t++){
        int x;
        cin >> x;
        for(int i=0;i<16;i++){
            int p;
            cin >> p;
            if(x-i/4==1)a[p]=t;
        }
        cin >> x;
        for(int i=0;i<16;i++){
            int p;
            cin >> p;
            if(x-i/4==1)b[p]=t;
        }
        printf("Case #%d: ",t);
        switch(check(t)){
        case 0:
        cout << "Bad magician!\n";
        break;
        case -1:
        cout << "Volunteer cheated!\n";
        break;
        default:
        cout << check(t) << endl;
        }
    }
}
