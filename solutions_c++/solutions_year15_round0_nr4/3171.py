#include <iostream>
using namespace std;

int main(){
    int t;
    cin >> t;
    for(int i=0;i<t;i++){
        int blocks,x,y,area;
        cin >> blocks >> x >> y;
        area=x*y;
        
        if(area<blocks){
            cout << "Case #" << i+1 << ": RICHARD" << endl;
            continue;
        }

        if(blocks==1){
            cout << "Case #" << i+1 << ": GABRIEL" << endl;
        } else if(blocks==2){
            if(area%2==0){
                cout << "Case #" << i+1 << ": GABRIEL" << endl;
            } else {
                cout << "Case #" << i+1 << ": RICHARD" << endl;
            }
        } else if(blocks==3){
            if(x==1 or y==1){
                cout << "Case #" << i+1 << ": RICHARD" << endl;
                continue;
            }
            if(area%3==0){
                cout << "Case #" << i+1 << ": GABRIEL" << endl;
            } else {
                cout << "Case #" << i+1 << ": RICHARD" << endl;
            }
        } else if(blocks==4){
            if(area==12 or area==16){
                cout << "Case #" << i+1 << ": GABRIEL" << endl;
            } else {
                cout << "Case #" << i+1 << ": RICHARD" << endl;
            }
        }
    }
}
