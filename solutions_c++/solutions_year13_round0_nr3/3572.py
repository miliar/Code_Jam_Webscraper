/*#include <iostream>
#include <sstream>
using namespace std;
int main(){
string s;
while ((getline( cin, s ) && !s.empty())){
stringstream ss( s );
}
return 0;
}
*/

#include <iostream>
#include <sstream>
#include <cmath>
using namespace std;
string NumberToString (int Number ){ostringstream ss;ss << Number;return ss.str();}
int ispalindrome(int x){
	string X1,X2;
	X1=NumberToString(x);
	X1 = string ( X1.rbegin(), X1.rend() );		//Reverse string
	X2=NumberToString(x);
	if (X1==X2){return 1;}
	return 0;
}

int issquare(int x){
	int y;
	y=sqrt(x);
	if (y*y==x){if (ispalindrome(y)==1){return 1;}}
	return 0;
}
int main(){
	int T,A,B,C;
	cin>>T;
	int i=0;
	C=0;
	while (i<T){
		cin>>A>>B;
		int j=A;
		while (j<=B){
			if (ispalindrome(j)==1){
				if (issquare(j)==1){
					C++;
				}
			}
			j++;
		}
		cout<<"Case #"<<i+1<<": "<<C<<endl;
		C=0;	
		i++;
	}
	return 0;
}
