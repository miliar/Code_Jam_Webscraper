#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

#define MAX_LENGTH 10000000
int counter =0;
int counter2 = 0;
int number[MAX_LENGTH];
int twod[ MAX_LENGTH][16];

void int_buffer_rec(int n, int length) {
    if(n > 0) {
        number[length-n] = 0;
        int_buffer_rec(n - 1, length);
        number[length-n] = 1;
        int_buffer_rec(n - 1, length);
    }
    else {
        for(int i = 0; i < length; ++i) {
            twod[counter][i] =  number[i];
        }
        counter++;
    }
}


bool checker( int arr[] , long N ){
    if( arr[0] == 1 && arr[N-1] == 1 )
        return true;

    return false;

}

long long int native( int arr[] , int base , long N ){

    long long int fin = 0;
    int counterx = 0;
    for( int i = N-1 ; i > -1 ; i-- ){
        fin += pow( base , counterx )*arr[i];
        //cout << fin << " " ;
        counterx++;
    }

    return fin;
}


long modder( long long int value){
    bool flag = false;
    long long int i;
    long long int x = sqrt( value ) ;
    for ( i = 2 ; i < x+1 ; i++ ){
        if( value%i == 0 ){
            flag = true;
            break;
        }
    }

    if( flag )
        return i;
    return -1;
}

int main(){

    ifstream cin("input3.txt");
    ofstream cout("output3.txt");
    long T , N , J , ans=0 ;

    cin >> T ;
    int_buffer_rec( 16 , 16 );
    for ( int i = 0 ; i < T  ; i++ ){
        cin >> N >> J ;
        cout << "Case #" << i+1 << ": " << endl;
        int arr[N];
        long result[9];
        while( ans != J ){
            // individual array generation
            for( int i = 0 ; i < N ; i++ ){
                arr[i] = twod[counter2][i];
            }
            counter2++;
            // cheaking for array
            if( !checker( arr , N ) ){
                continue;
            }



            long long int fin = 0;
            long number ;
            bool flag = false;
            for ( int f = 2 ; f < 11 ; f++  ){
                // converting binary to native
                fin = native( arr , f , N );


                number = modder( fin );

                if( number == -1 ){
                    flag = false;
                    break;
                }
                // cout << fin << endl;
                result[f-2] = number;
                flag = true;


            }

           // cout << fin << endl;

            if( flag == false )
                continue;

            for( int i = 0 ; i < N ; i++ ){
                cout << arr[i] ;
            }

            cout << " ";
            for ( int i = 0 ; i < 9 ; i++ ){
                cout << result[i] << " " ;
            }
            cout << endl;

            ans++;
        }





    }


}

