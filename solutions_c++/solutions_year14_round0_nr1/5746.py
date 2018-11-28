#include <iostream>
using namespace std;

int main(void) {
	int T,t, Arr1[4][4] ,ans1,ans2 ,Arr2[4][4] ,i ,j , ans=0,match=0;
	cin>>T;
	for( t=1 ;t<=T ;t++){
		ans=0;
		match=0;
		cin>>ans1;
		for( i=0;i<4;i++){
			for( j=0;j<4;j++){
				cin>>Arr1[i][j];
			}
		}
		cin>>ans2;
		for( i=0;i<4;i++){
			for( j=0;j<4;j++){
				cin>>Arr2[i][j];
			}
		}
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(Arr1[ans1-1][i]==Arr2[ans2-1][j]){
					match++;
					ans=Arr1[ans1-1][i];
				}
			}
		}
		
		if(match==0){
			cout<<"Case #"<<t<<": Volunteer cheated!\n";
		} else if(match==1){
			cout<<"Case #"<<t<<": "<<ans<<endl;
		} else {
			cout<<"Case #"<<t<<": Bad magician!\n";
		}
		
	}
	return 0;
}
