#include <iostream>
using namespace std;

int m1[4][4];
int m2[4][4];

void magic(int numc, int a, int b){
	int cont = 0, ind;
	for(int i = 0 ; i < 4; i++){
		for(int j = 0 ; j < 4; j++){
			if(m1[a][i] == m2[b][j]){
				cont++;
				ind = m1[a][i];
			}
		}
	}
	cout<<"Case #"<<numc<<": ";
	if(cont==0)
		cout<<"Volunteer cheated!";
	else if(cont==1)
		cout<<ind;
	else
		cout<<"Bad magician!";
	cout<<endl;
}

int main(int argc, char *argv[]) {
	int n,a,b;
	cin>>n;
	for(int case_num = 1; case_num <= n; case_num++){
		cin>>a;
		for(int i = 0; i < 4; i++){	
			for(int j = 0; j < 4; j++){	
				cin>>m1[i][j];
			}
		}
		cin>>b;
		for(int i = 0; i < 4; i++){	
			for(int j = 0; j < 4; j++){	
				cin>>m2[i][j];
			}
		}
		magic(case_num,a-1,b-1);
	}
	return 0;
}

