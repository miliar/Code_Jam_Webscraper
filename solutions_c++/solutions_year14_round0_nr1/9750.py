#include<iostream>
#include<vector>
#include<map>
#define MAX 4
using namespace std;
int T, f, s, aux;
int main(){
	cin>>T;
	for(int i = 1; i <= T; i++){
	
		map<int, int> M;
		
		cin>>f;
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				cin>>aux;
				if(j == f - 1) M[aux]++;
			}
		}
		
		vector<int> V;
		
		cin>>s;
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				cin>>aux;
				if(j == s - 1){
					if(M[aux] > 0){
						V.push_back(aux);
						M[aux]--;
					}
				}
			}
		}
		
		if(V.size() == 0) cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		else{
			if(V.size() == 1) cout<<"Case #"<<i<<": "<<V[0]<<endl;
			else cout<<"Case #"<<i<<": Bad magician!"<<endl;
		}
	}
	return  0;
}