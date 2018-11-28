#include <iostream>
using namespace std;

int main(){
	int t;
	cin>>t;

	for(int i=0;i<t;i++){
		bool end=false;
		bool diff=false;
		int times=0;
		int pos;
		string cadena;
		
		cin>>cadena;

		if(cadena.length()==1){
			if(cadena[0]=='-'){
				cout<<"Case #"<<i+1<<": 1"<<endl;
			}
			else{
				cout<<"Case #"<<i+1<<": 0"<<endl;
			}
		}
		else{
			while(!end){
				int j;
				for(j=1;j<(int)cadena.length() && !diff;j++){
					if(cadena[j]!=cadena[0]){
						diff=true;
						pos=j;
					}
				}
				if(diff){
					times++;
					for(int k=0;k<pos;k++){
						cadena[k]=cadena[pos];
					}
					diff=false;
				}
				else if(cadena[0]=='-'){
					times++;
					cout<<"Case #"<<i+1<<": "<<times<<endl;
					end=true;
				}
				else{
					cout<<"Case #"<<i+1<<": "<<times<<endl;
					end=true;
				}
			}
		}
	}
}