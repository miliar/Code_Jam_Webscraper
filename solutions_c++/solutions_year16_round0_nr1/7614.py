#include<iostream>
using namespace std;

int main()
{
    unsigned long long n, i, num;
    int t, j, sum, a[9];
    cin >>t;
    for( j = 1; j <= t; j++ ) {
        cin >>n;
        if( n == 0 )
            cout<<"Case #"<<j<<": INSOMNIA"<<endl;
        else {
            sum = 0;
            for( i = 0; i < 10; i++ )
                a[i] = 0;
            for( i = 1; sum != 10; i++ ) {
                num = n*i;
                while( num != 0) {
                    if( a[num%10] == 0 ) {
                        a[num%10] = 1;
                        sum++;
                    }
                    num = num/10;
                }
            }
            cout<<"Case #"<<j<<": "<<n*(i-1)<<endl;
        }
    }
    return 0;
}



