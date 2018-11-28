#include<iostream>
using namespace std;
bool allNumberFound(long long int visited[] ) {
    for( long long int i=0;i<10; i++) {
        if ( visited[i] == 0 ) return false;
    }
    return true;
}
int main() {
    long long int test,n,m,i,j,rem,answer;
    long long int visited[10]={0};
    cin >> test;
    for( i=1; i<=test; i++) {
        cin >> n;
        if ( n == 0 ) cout << "Case #" << i << ": INSOMNIA" << endl;
        else {
            for( j = 1; j<=1000; j++) {
                answer = m = n*j;
                while (m) {
                    rem = m%10;
                    visited[rem]=1;
                    m = m/10;
                }
                if ( allNumberFound(visited) ) break;
            }
            cout << "Case #" << i << ": " << answer << endl;
            for( long long int i=0;i<10; i++) {
                visited[i] = 0;
            }
        }        
    }
    return 0;
}
