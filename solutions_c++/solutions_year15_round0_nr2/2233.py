#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>

const int MAXN = 1010;

using namespace std;

int N;
int table[MAXN];

int fun1(int pos){
	
	while( (pos > 0) && (table[pos] == 0)  )
		pos--;
	
	return pos;
}


int main() {
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	
	int T; cin>>T;
	
	for(int t=1;t<=T;t++){
		
		for(int i=0;i<=1000;i++)
			table[i] = 0;
		
		cin>>N;
		for(int i=0;i<N;i++){
			int x; cin>>x;
			table[x]++;
		}
		
		int result = 1000;
		for(int i=1;i<=1000;i++){
			int sum = 0;
			for(int j=i+1;j<=1000;j++)
				if( table[j] ){
					int dia = j / i;
					if( (i*dia) != j )
						dia++;
					sum += table[j] * (dia - 1);
				}
			result = min( result, sum + i );
		}
		cout<<"Case #"<<t<<": "<<result<<'\n';
	}
	
	return 0;
}
