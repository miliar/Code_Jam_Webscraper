#include <iostream>
#include <vector>
using namespace std;

int main(){
	vector<int> posibles;
	int final;
	int casos;
	int temp;
	int respuesta1;
	int respuesta2;
	cin>>casos;
	bool bandera=false;
	bool bandera2=false;
	for(int i=0;i<casos;i++){
		cin>>respuesta1;
		for(int j=0;j<4;j++){
			if(j!=respuesta1-1){
				for(int k=0;k<4;k++)cin>>temp;
			}
			else{
				for(int k=0;k<4;k++){
					cin>>temp;
					posibles.push_back(temp);
				}
			}
		}
		cin>>respuesta2;
		for(int j=0;j<4;j++){
			if(j!=respuesta2-1){
				for(int k=0;k<4;k++)cin>>temp;
			}
			else{
				for(int k=0;k<4;k++){
					cin>>temp;
					if(posibles[0]==temp||posibles[1]==temp||posibles[2]==temp||posibles[3]==temp){
						if(bandera==true)bandera2=true;
						else {
							bandera=true;
							final=temp;
						}
					}
				}
			}
		}
		cout<<"Case #"<<i+1<<": ";
		if(bandera==true && bandera2==false)cout<<final;
		else if(bandera==true && bandera2==true)cout<<"Bad magician!";
		else if(bandera==false)cout<<"Volunteer cheated!";
		if(i<casos-1)cout<<endl;
		bandera=false;
		bandera2=false;
		posibles.clear();

	}


	return 0;
}