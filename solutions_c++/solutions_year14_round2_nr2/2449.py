#include <iostream>
#include <string>

using namespace std;

struct Case{
	int a, b, k;
	Case(){
		cin >> a >> b >> k;
	}
	
	string result(){
		int amount = 0;
		for( int i=0; i<a; i++ )
			for( int j=0; j<b; j++ )
				if( (i & j) < k )
					amount++;
		return to_string( amount );
	}
};

int main( int, char** ){
	int amount = 0;
	cin >> amount;
	for( int i=1; i<=amount; i++ )
		cout << "Case #" << i << ": " << Case().result() << endl;
	
	return 0;
}
