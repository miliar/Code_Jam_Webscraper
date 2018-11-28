#include <iostream>
#include <fstream>

using namespace std;


int a[17];

int main(){
	int t , test = 1, first, sec, tmp;
	ofstream out;
	ifstream in;
	out.open("out.in");
	in.open("A-small-attempt0.in");
	in>>t;
	while ( test <= t){
		for ( int i = 0; i < 17 ; i++)
			a[i] = 0;
		in>>first;
		for ( int i = 0 ; i < 4; i++)
			for ( int j = 0 ; j < 4 ; j++){
				in>>tmp;
				if ( i == first-1)
					a[tmp]++;
			}
		in>>sec;
		for ( int i = 0 ; i < 4 ; i++)
			for ( int j = 0 ; j < 4 ; j++){
				in>>tmp;
				if ( i == sec-1)
					a[tmp]++;
			}
		int cnt = 0;
		int idx = -1;
		for ( int i = 0 ; i < 17;i++ )
			if ( a[i] == 2){
				cnt++;
				idx = i;
			}
		if ( cnt == 0 )
			out<<"Case #"<<test<<": Volunteer cheated!"<<endl;
		else if ( cnt == 1)
			out<<"Case #"<<test<<": "<<idx<<endl;
		else
			out<<"Case #"<<test<<": Bad magician!"<<endl;
		test++;
	}
	out.close();
	in.close();
	return 0;
}