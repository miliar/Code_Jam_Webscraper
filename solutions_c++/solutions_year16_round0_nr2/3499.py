#include <iostream>
#include <fstream>
#include <string>
using namespace std;


string calculate( string str ){
    char a = str[0];
    int counter = 1;

    while( str[counter] == a ){
        counter++;
        if( counter == str.size() ){
            return str;
        }
    }

    for( int i = 0 ; i < counter ; i++ ){
        if( str[i] == '-'){
            str[i] = '+';
        }
        else{
            str[i] = '-';
        }
    }

    return str;
}
int main() {
    ifstream cin("input2.txt");
    ofstream cout("output2.txt");

    int T , counter;
    string str;
    cin >> T ;

    for( int k=0 ; k<T ; k++ ){
        cin >> str;
        counter = 0;
        bool flag = false;
        if( str.size() == 1 ){
            if( str[0] == '-')
                cout << "Case #" << k+1 << ": 1" << endl;
            else
                cout <<  "Case #" << k+1 << ": 0" << endl;
            continue;

        }
        for ( int s = 0 ; s < str.size()-1 ; s++ ){
            if( str[s] == str[s+1] ){
                    counter = -1;
                    continue;
                }
                else{
                    counter = 0;
                    break;

                }
        }

        while( !flag ){
           // cout << counter << endl;
            str = calculate( str );
            for ( int i = 0 ; i< str.size()-1 ; i++ ){
                if( str[i] != str[i+1]  ){
                    flag = false;
                    break;
                }
                else if( i ==  str.size() -2 ){
                    flag = true;

                }
            }

            counter++;
        }
       // cout << str << endl;

        if( str[0] == '-' ){
            counter++ ;
        }

        cout << "Case #" << k+1 << ": " << counter << endl;

    }




}
