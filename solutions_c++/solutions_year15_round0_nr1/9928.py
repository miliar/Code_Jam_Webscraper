#include <iostream>
#include <string>

using namespace std;

int main(){
	int test = 0,cont = 0,size = 0,suma = 0;
	cin >> test;
	for(int i=0;i<test;i++){
		string c= "";
		size = cont = 0;
		cin>>size>>c;
		suma = c[0] - '0';
		for(int j=1;j<size+1;j++){
			if (suma < j){
				if (c[j] != '0'){
					int a = j - suma;
					//cout << c[j] << " " << suma << " " << j <<endl;
					suma += a;
					cont += a;	
				}
			}
			suma += c[j] - '0';
		}
		cout << "Case #"<<i+1<<": "<< cont <<endl;
	}
	
	return 0;
}
