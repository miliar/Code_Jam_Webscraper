#include<iostream>
#include <fstream>

using namespace std;

int main(){
	ofstream myfile;
  	ifstream input;
  	input.open("file.in");
    myfile.open ("saida.txt");
	int t;
	int ans;
	string nome;
	int smax;
	int standup;
	int aux;
	input>>t;
	for(int k=1; k<=t; k++){
		ans = 0;
		standup=0;
		input>>smax;
		input>>nome;
		for(int i=0; i<nome.size(); i++){
			aux=nome[i]-'0';
			if(aux>0){
				if(standup>=i){
					standup+=aux;
				}else{
					ans+=(i-standup);
					standup+=aux+(i-standup);
				}
			}
		}
		myfile<<"Case #"<<k<<": "<<ans<<endl;
	}
	myfile.close();
	input.close();
	return 0;
	
}
