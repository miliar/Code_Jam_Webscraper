#include<iostream>
#include<vector>

using namespace std;

int main(){

    int T, N ;
    int temp, min_rate;
    int method1, method2, diff,j;
    vector<int> m;

    cin>> T;
    j=0;
    while( T-- ){
        j++;
        method1 =0;
        method2 =0;
        m.clear();
        cin >> N;
        for( int i =0; i < N ; i++ )
        {
            cin >> temp;
            m.push_back( temp );
        }
        min_rate = 0;
        for( int i = 1; i < N ; i++ ){
            diff = m[i-1]-m[i];
            if( m[i-1] > m[i] ) {
                method1+= diff;
            }
            if( diff > min_rate ){
                min_rate = diff;
            }
        }
        for( int i = 1; i < N ; i++ ){
            if( m[ i-1 ] >= min_rate ){
                method2 += min_rate;
            }
            else{
                method2 += m[ i- 1 ];
            }
        }
        cout<<"Case #"<<j<<": "<<method1<<" "<<method2<<endl;
    }
}
