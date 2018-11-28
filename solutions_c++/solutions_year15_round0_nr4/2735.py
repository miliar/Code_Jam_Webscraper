#include<iostream>

using namespace std;

int main(){
    int T;
    int X,R,C;

    int i=1;
    cin >> T;
    while( i <= T ){
        cin>> X >> R >> C;
        if( X >= 7){
            cout << "Case #"<< i <<": RICHARD"<<endl;
        }
        else if( X > R*C ){
            cout << "Case #"<< i <<": RICHARD"<<endl;
        }
        else if( X == R*C ){
            if( X == 1 || X == 2 ){
                cout << "Case #"<< i <<": GABRIEL"<<endl;
            }
            else{
                cout << "Case #"<< i <<": RICHARD"<<endl;
            }
        }
        else if( X < R*C && X > (R*C)/2){
            cout << "Case #"<< i <<": RICHARD"<<endl;
        }
        else if( X == (R*C)/2 ){
            switch(X)
            {
                case 1:;
                case 2:
                       cout << "Case #"<< i <<": GABRIEL"<<endl;
                       break;
                case 3:
                       if( (R >= 2 && C % 3 == 0) || (C >= 2 && R % 3 == 0) ){
                           cout << "Case #"<< i <<": GABRIEL"<<endl;
                       }
                       else{
                           cout << "Case #"<< i <<": RICHARD"<<endl;
                       }
                       break;
                case 4:
                       if( (R >= 3 && C % 4 == 0) || (C >= 3 && R % 4 == 0) ){
                           cout << "Case #"<< i <<": GABRIEL"<<endl;
                       }
                       else{
                           cout << "Case #"<< i <<": RICHARD"<<endl;
                       }
                       break;
                case 5:
                       if( (R >= 4 && C % 5 == 0) || (C >= 4 && R % 5 == 0) ){
                           cout << "Case #"<< i <<": GABRIEL"<<endl;
                       }
                       else{
                           cout << "Case #"<< i <<": RICHARD"<<endl;
                       }
                       break;
                case 6:
                       if( (R >= 5 && C % 6 == 0) || (C >= 5 && R % 6 == 0) ){
                           cout << "Case #"<< i <<": GABRIEL"<<endl;
                       }
                       else{
                           cout << "Case #"<< i <<": RICHARD"<<endl;
                       }
                       break;
            }
        }
        else if( X < (R*C)/2 ){
            if( R*C % X == 0 ){
                switch(X)
                {
                    case 1:;
                    case 2:
                           cout << "Case #"<< i <<": GABRIEL"<<endl;
                           break;
                    case 3:
                           if( (R >= 2 && C % 3 == 0) || (C >= 2 && R % 3 == 0) ){
                               cout << "Case #"<< i <<": GABRIEL"<<endl;
                           }
                           else{
                               cout << "Case #"<< i <<": RICHARD"<<endl;
                           }
                           break;
                    case 4:
                           if( (R >= 3 && C % 4 == 0) || (C >= 3 && R % 4 == 0) ){
                               cout << "Case #"<< i <<": GABRIEL"<<endl;
                           }
                           else{
                               cout << "Case #"<< i <<": RICHARD"<<endl;
                           }
                           break;
                    case 5:
                           if( (R >= 4 && C % 5 == 0) || (C >= 4 && R % 5 == 0) ){
                               cout << "Case #"<< i <<": GABRIEL"<<endl;
                           }
                           else{
                               cout << "Case #"<< i <<": RICHARD"<<endl;
                           }
                           break;
                    case 6:
                           if( (R >= 5 && C % 6 == 0) || (C >= 5 && R % 6 == 0) ){
                               cout << "Case #"<< i <<": GABRIEL"<<endl;
                           }
                           else{
                               cout << "Case #"<< i <<": RICHARD"<<endl;
                           }
                           break;
                }
            }
            else{
                cout << "Case #"<< i <<": RICHARD"<<endl;
            }
        }
        i++;
    }
}

