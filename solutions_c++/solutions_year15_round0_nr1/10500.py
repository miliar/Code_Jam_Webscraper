#include<iostream>
#include<cstdio>

using namespace std;

int main() {
    int t, smax;
    string s;
    scanf("%d", &t);
    int j = 1;
    while( t-- ){
        scanf("%d", &smax);
        cin>>s;
        int sum = 0, a = 0;
        for( int i = 0; i<=smax; i++ ){
            int c = int( s[i] ) - '0';
            if( sum < i && c > 0 ){
                a += ( i - sum );
                sum += a;
            }
            sum += c;
        }
        printf("Case #%d: %d\n", j,a);
        j++;
    }
    return 0;
}
