#include<bits/stdc++.h>
using namespace std ;

int main(){
    ios::sync_with_stdio(false);
    int t,q ;
    cin >>t ;
    for(q=1;q<=t;q++){
    int x,r,c,i,j,k,ans ;

    cin >> x >> r >> c ;
    if(x==1){cout << "Case #" << q << ": " << "GABRIEL" <<endl   ;}
    else if(x==2){
       if(r==1&&c==1 || r==1 && c==3 || r==3 && c==1 || r==3&&c==3){        cout << "Case #" << q << ": " << "RICHARD" <<endl   ;}
       else{cout << "Case #" << q << ": " << "GABRIEL" <<endl   ; }

    }
    else if(x==3){
        if(r==2 && c==3 || r==3 && c==2 || r==3 && c==4 || r==4 && c==3 || r==3 && c==3 ){cout << "Case #" << q << ": " << "GABRIEL" <<endl   ;}
        else{  cout << "Case #" << q << ": " << "RICHARD" <<endl   ; }
    }
    else if(x==4){

        if(r==3&&c==4 || r==4 && c==3 || r==4 && c==4){cout << "Case #" << q << ": " << "GABRIEL" <<endl   ;}
        else{cout << "Case #" << q << ": " << "RICHARD" <<endl   ;}
    }
    }
}
