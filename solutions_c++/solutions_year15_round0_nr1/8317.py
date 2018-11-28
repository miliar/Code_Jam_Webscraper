#include<cstring>
#include<cstdio>
#include<iostream>
using namespace std;
int main(){
	int test, t, req, n, sofar, j = 1;

	freopen ("A-small-attempt0.in","r",stdin);
	freopen( "output.txt","w",stdout);
		cin>>test;
	while( j <= test){
		char arr[1010] = "";
		sofar = 0, t = 0, req = 0;
		scanf( "%d", &n);
		scanf( "%s", arr);
		//cout<<arr<<"*";
		for( int i = 0; i <= n && arr[i] != '\0'; i++){
			//cout<<sofar<<" ";
			t = arr[i] - '0';
			if( t == 0)
				continue;
			if( sofar >= i){
				sofar = sofar + t;
				continue;
			}
			req += i - sofar;
			sofar = sofar + i - sofar + t;
			
		}
		printf( "Case #%d: %d\n",j,req);
		j++;
	}
	return 0;
}
		
		
