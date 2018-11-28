# include <iostream>
# include <cstdio>
using namespace std;
int main(){
	int t;
	cin >> t;
	int j = 1;
	while(j <= t){
	string texto,texto2;
	cin >> texto;
	texto2.clear();

		for(int i = 0; i < texto.length(); i++){
			if(i == 0){
				texto2.insert(texto2.begin(), texto.at(i));
			} else{

			if(texto.at(i) >= texto2.at(0)){
				texto2.insert(texto2.begin(), texto.at(i));
			} else{
				texto2.insert(texto2.end(), texto.at(i));
			}
			}
		}
		cout << "CASE #" << j << ": "<< texto2 << endl;
		j++;
	}
	return 0;
}