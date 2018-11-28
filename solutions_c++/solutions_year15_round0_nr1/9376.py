#include <iostream>
#include <string>
using namespace std;

inline int get_int(char c){return (int)(c-'0');}

int main(){
	
	int t, npersona;
	cin>>t;
	for(int i=0; i<t; ++i){
		string shy;
		cin>>npersona;
		cin>>shy;

		int np=0, n=0, entero, difference;
		for(int s=0; s<=npersona; ++s){
			if (np<s){
				difference = s-np;			
				n += difference;
				np +=difference;				
			}
			entero=get_int(shy[s]);
			np+=entero;
		}
		cout<<"Case #"<<i+1<<": "<<n<<endl;
	
	}


}
