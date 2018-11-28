#include <iostream>
#include <cstdio>
using namespace std;
int A[4][4][2];
int main(){
	int casos; cin>>casos;
	int a1,a2;
	for(int caso=1;caso<=casos;caso++){
		cin>>a1;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>A[i][j][0];
			}
		}
		cin>>a2;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>A[i][j][1];
			}
		}
		
		a1--; a2--;
		int ans;
		int cont=0;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(A[a1][i][0]==A[a2][j][1]){
					ans=A[a1][i][0];
					cont++;
				}
			}
		}
		printf("Case #%d: ",caso);
		if(cont==0){
			cout<<"Volunteer cheated!"<<endl;
		}else{
			if(cont==1){
				cout<<ans<<endl;			
			}else{
				cout<<"Bad magician!"<<endl;		
			}
		}
	}
return 0;}
