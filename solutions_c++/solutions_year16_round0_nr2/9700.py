#include <bits/stdc++.h>

using namespace std;

char opposite( char c ){
	if( c == '+' )
		return '-';
	else
		return '+';
	return '*';
}
void flip( char* s, int from, int to ){
	char tmp;
	int n = (to+1)/2;
	//cout << "n: " << n << endl;
	for( int i = from, j = to - 1; i < n ; i++, j--){
		if( i != j ){
			tmp = s[i];
			s[i] = opposite( s[j] );
			s[j] = opposite( tmp );
		}else
			s[i] = opposite( s[i] );
		//cout << s << " " << i << endl;
	}
}

void flipPlus( char* sub, bool& done, int size ){
	//cout << "plus" << endl;
	int notPlus = -1;
	
	for( int i = 0; i < size; i++ ){
		if( sub[i] != '+' ){
			notPlus = i;
			break;
		}
	}

	//cout << notPlus << endl;
	if( notPlus == -1 ){
		done = true;
	}else
		flip( sub, 0, notPlus );
	//done = true;
}

void flipMinus( char* sub, bool& done, int size ){
	//cout << "minus" << endl;
	int notMinus = size;
	for( int i = 0; i < size; i++ ){
		if( sub[i] != '-' ){
			notMinus = i;
			break;
		}
	}

	//cout << notMinus << endl;
	/*if( notMinus == -1 ){
		done = true;
	}else
		flip( sub, 0, notMinus );*/
	flip( sub, 0, notMinus );
	//done = true;
}

int main(){
	int T;
	scanf("%d\n", &T);
	for( int t = 0; t < T; t++ ){
		string str;
		cin >> str;
		char* pan = new char [str.size()+1];
		strcpy ( pan, str.c_str() );
		bool done = false;
		
		int times = -1;
		while( !done ){
			if( pan[0] == '+' )
				flipPlus( pan, done, str.size() );
			else
				flipMinus( pan, done, str.size() );
			times++;
		//cout << pan << endl;
		}

		//cout << pan << endl;		
		printf( "Case #%d: %d\n", t+1, times );
	}
}
