#include <bits/stdc++.h>

using namespace std;

int main(){
	int cases;
	cin>>cases;
	int first[4][4],second[4][4];
	vector <int> m1(4),m2(4);
	for(int i=1; i<=cases; i++){
		bool bandera=false;
		bool bandera2=false;
		int ans1,ans2;
		cin>>ans1;
		for(int k=0; k<4; k++){
			for(int j=0; j<4; j++){
				cin>>first[k][j];
			}
		}
		cin>>ans2;
		for(int k=0; k<4; k++){
			for(int j=0; j<4; j++){
				cin>>second[k][j];
			}
		}
		for(int k=0; k<4; k++){
			m1[k]=first[ans1-1][k];
			m2[k]=second[ans2-1][k];
		}

		for(int k=0; k<4; k++){
			if(m1[k]==m2[k]){
				bandera=true;
			}
			else{
				bandera=false;
				break;
			}
		}

		cout<<"Case #"<<i<<": ";
		if(bandera)cout<<"Bad magician!"<<endl;
		else{
			sort(m1.begin(),m1.end());
			sort(m2.begin(),m2.end());
			vector <int> posibles;
			for(int j=0; j<4; j++){
				if(binary_search(m2.begin(),m2.end(),m1[j])){
					bandera2=true;
					posibles.push_back(m1[j]);
				}
			}
			if(posibles.size() == 1)cout<<posibles[0]<<endl;
			if(posibles.size() > 1)cout<<"Bad magician!"<<endl;
			if(!bandera2 && posibles.size() != 1)cout<<"Volunteer cheated!"<<endl;
		}

	}
	return 0;
}