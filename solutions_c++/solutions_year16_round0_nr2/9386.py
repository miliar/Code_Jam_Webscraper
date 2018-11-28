#include<iostream>
#include<string>
using namespace std;
bool checkAllUp(string pancake ) {
    for( int i=0;i<pancake.size(); i++) {
        if ( pancake[i] == '-' ) return false;
    }
    return true;
}
bool checkAllDown(string pancake ) {
    for( int i=0;i<pancake.size(); i++) {
        if ( pancake[i] == '+' ) return false;
    }
    return true;
}
int main() {
    int test,i,j,n,flip;
    bool up,down;
    string pancake;
    cin >> test;
    for( i=1; i<=test; i++) {
        cin >> pancake;
        if (checkAllUp(pancake) ) cout << "Case #" << i << ": 0" << endl;
        else if (checkAllDown(pancake) ) cout << "Case #" << i << ": 1" << endl;
        else {
            flip = 0;
            n = pancake.size();
            while ( 1 ) 
            {
                up = down = false;
                if ( checkAllUp(pancake) ) break;
                for( j=0; j<n; j++) 
                {
                    if ( pancake[j] == '+' ) 
                    {
                         pancake[j] = '-';
                         up = true;
                    }
                    else break;
                }
                //cout << " first : " << pancake << endl;
                if ( up ) flip = flip + 1;
                for( j=0; j<n; j++) 
                {
                    if ( pancake[j] == '-' ) 
                    {
                         pancake[j] = '+';
                         down = true;
                    }
                    else break;
                } 
                //cout << " second : " << pancake << endl;
                if ( down ) flip = flip + 1;
            }
            cout << "Case #" << i << ": " << flip << endl;
        }        
    }
    //system("pause");
    return 0;
}
