#include <iostream>
#include <algorithm>
#include <vector>
#include <map>


#define NAO 0
#define FOI 1

using namespace std;

struct passou{
	int valor;
	bool foi;
};

passou v[11][11];
int N,M;

int main(){
	int t,caso;
	cin>>t,caso = 1;
	while(t--){
		cout << "Case #" << caso++ << ": ";
		cin>>N>>M;
		for(int i =0 ;i<N;++i){
			for(int j = 0;j<M;++j){
				cin>>v[i][j].valor;
				v[i][j].foi = NAO;
			}
		}

		for(int i =0 ;i<N;++i){
			for(int j = 0;j<M;++j){
				int h = v[i][j].valor;
				bool flag = true,flag2 = true;
				for(int k = j;k>=0 && flag;--k){
					if(v[i][k].valor>h)flag = false;
				}
				for(int k = j;k<M && flag;++k){
					if(v[i][k].valor>h)flag = false;
				}

				for(int k = i;k>=0 && flag2;--k){
					if(v[k][j].valor>h)flag2 = false;
				}
				for(int k = i;k<N && flag2;++k){
					if(v[k][j].valor>h)flag2 = false;
				}
				if(flag || flag2) v[i][j].foi = FOI;
				 else v[i][j].foi = NAO;

			}
		}
		
		bool flag = true;
		for(int i =0 ;i<N && flag;++i){
			for(int j = 0;j<M && flag;++j){
				if(v[i][j].foi == NAO) flag = false;
			}
		}

		if(flag)cout<<"YES"<<endl;
		else cout<<"NO"<<endl;

	}
	return 0;
}