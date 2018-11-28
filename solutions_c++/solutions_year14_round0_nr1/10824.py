#include<bits/stdc++.h>
using namespace std;

main(){
int p=1;
int tc;cin>>tc;
ofstream myfile;
myfile.open("output.txt");
while(tc--){
	int fa;cin>>fa;
	int asw[4];
	int fp[4][4];
	int sm[4][4];
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			cin>>fp[i][j];
			if(i==fa-1){
				asw[j]=fp[i][j];
			}
		}
	}
	int sa;cin>>sa;
	int coinc=0;
	int answ=-1;
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			cin>>sm[i][j];
			if(i==sa-1){
				for(int k=0;k<4;k++){
					if(asw[k]==sm[i][j]){
						coinc++;
						answ=asw[k];
					}				
				}
			}
		}
	}
	myfile<<"Case #"<<p<<": ";
	if(coinc==1)//printf("Case #%d: %d\n",p,answ);
		myfile<<answ<<endl; 	
	else{
		if(coinc==0) myfile<<"Volunteer cheated!\n";
		else myfile<<"Bad magician!\n";	
		}
	p++;
}

}
