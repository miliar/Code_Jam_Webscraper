#include <iostream>
using namespace std;


int main()
{
    int i,j,x,r,c,tm;
    int T,k=0,flg;
    string TS[1001];

    cout << "Input\n";
    cin >> T;

    while(T) {
        flg=0;
        cin >> x; //omni
        cin >> r; //row
        cin >> c; //col
        tm=r*c;
        if(x==1) {
            TS[k]="GABRIEL";
        }else if(x==2 && ((r*c)%2)==0){
            TS[k]="GABRIEL";
        }else if(x == 3 && ((r*c)>=(x*2))  && ((r*c)%3==0) ){
            TS[k]="GABRIEL";

        }else if(x >= 4  &&  ( ((r >= x) && (c>=(3))) || ((c >= x) && (r>=(3))) ) && x<=6  && ((r*c)%x==0)   ){
            TS[k]="GABRIEL";

        }else
            TS[k]="RICHARD";



        /*else if( tm%3==0 && (r==2 || c==2) && (x==3 || x==2) && tm==3){
                TS[k]="GABRIEL";
        }else if( tm%x==0 && (r==x || c==x) && tm!=x ) {
                TS[k]="GABRIEL";
/*        }else if( tm%2==1 && x==1) {
                TS[k]="GABRIEL";
        } else {
                TS[k]="RICHARD";
        }*/
        k++;
        T--;
    }

    cout << "\nOutput\n";
    for(i=0;i<k;i++) {
            cout << "Case #" << (i+1) <<": " << TS[i] << endl;
    }

    return 0;
}
