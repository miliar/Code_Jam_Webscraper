#include<bits/stdc++.h>
using namespace std;

int main(){
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++){
        int X,C,R;
        scanf("%d %d %d",&X,&R,&C);
        switch(X){
            case 1:cout << "Case #"<<i<<": "<<"GABRIEL" << endl;
                break;
            case 2: if((R%2==0)||(C%2==0)) cout << "Case #"<<i<<": "<<"GABRIEL" << endl;
                else cout << "Case #"<<i<<": "<<"RICHARD" << endl;
                break;
            case 3: if (((R==3)&&(C==4))||((R==2)&&(C==3))) cout << "Case #"<<i<<": "<<"GABRIEL" << endl;
                else if (((R==4)&&(C==3))||((R==3)&&(C==2))) cout << "Case #"<<i<<": "<<"GABRIEL" << endl;
                else if ((R==3)&&(C==3)) cout << "Case #"<<i<<": "<<"GABRIEL" << endl;
                else cout << "Case #"<<i<<": "<<"RICHARD" << endl;
                break;
            case 4: if (((R==3)&&(C==4))||((R==4)&&(C==3))) cout << "Case #"<<i<<": "<<"GABRIEL" << endl;
                else if ((R==4)&&(C==4)) cout << "Case #"<<i<<": "<<"GABRIEL" << endl;
                else cout << "Case #"<<i<<": "<<"RICHARD" << endl;
                break;
        }
    }
    return 0;
}

