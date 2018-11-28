#include<bits/stdc++.h>
using namespace std;
int main(){
	
   /*
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
   */
   int n;
   cin>>n;
 
   for ( int i = 0; i < n; i++ ){
		string s;
		cin>>s;
		char c = ' ';
		deque< char > v;
		for ( int j = 0 ; j < (int)s.size();j++ ){
			
			if ( (c == ' ') || ( s[ j ] >= c ) ){
				c = s[ j ];
				v.push_front( c );
			}else{
				v.push_back( s[ j ] );
			}
		}
		printf("Case #%d: ",i+1);
		for ( deque< char >::iterator it = v.begin(); it != v.end(); it++ ){
			cout<<(*it);
		}
		cout<<endl;
		
   }
   

}
