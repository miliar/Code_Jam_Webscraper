#include <bits/stdc++.h>
#define ll long long
using namespace std;
string s;
int main(){
	int t, i, j, k, it, counter;
	char ch;
	scanf( "%d", &t );
    	for( int tc = 1 ; tc<=t ; ++tc){
                cin >> s;
                int n = s.length();
                counter=0;
                while( true){
                        i = 0;
                        ch = s[0];
                        while(  i<n && s[i] == ch) i++;
                        if( i==n ) break;
                        for( it = 0 ; it<i ; ++it ) s[it] = ch == '+' ? '-' : '+';
                        counter++;
                }
                if( ch == '+' ) printf("Case #%d: %d\n", tc, counter);
                else printf("Case #%d: %d\n", tc, counter+1);
    	}
    	return 0;
}
