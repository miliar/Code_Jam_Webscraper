#include <iostream>
#include <fstream>

using namespace std;

int arr[10];

bool calculate( int N ){
   while( N ){
        arr[ N%10 ] = 1;
        N = N/10 ;
   }
    bool flag = true;
   for ( int i = 0 ; i < 10 ; i++ ){
        if( arr[i] == 0 ){
            flag = false;
            break;
        }
   }

   return flag;
}

int main(){
    ifstream cin("input1.txt");
    ofstream cout( "output1.txt");

    int T , N , X;

    cin >> T ;

    for( int k = 0 ; k < T ; k++ ){
        for ( int i = 0 ; i < 10 ; i++ ){
                arr[i] = 0;

        }
        cin >> N;
        X = N;
        int counter = 1;
        bool flag = false;
        while( true ){
            if( X == 0 ){
                break;
            }

            X = N*counter;

            flag = calculate( X );
            if( flag == true )
                break;

            counter++;
        }
        if( N*counter== 0 )
            cout << "Case #" << k+1 << ": INSOMNIA"<< endl;
        else
            cout<< "Case #" << k+1 << ": " << N*counter << endl;


    }


}
