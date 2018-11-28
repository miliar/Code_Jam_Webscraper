#include <iostream>
#include <cstdio>
using namespace std;
int main(){
	int T;
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("Out.txt","w",stdout);
	cin>>T;
	for(int kasus=0;kasus<T;kasus++){
		int first,second;
		cin>>first;
		int Array1[4][4];
		int Array2[4][4];
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>Array1[i][j];
			}
		}
		cin>>second;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>Array2[i][j];}
		}
		int match=0;
		int Ans;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(Array2[second-1][j]==Array1[first-1][i]){
					match++;
					Ans=Array2[second-1][j];
					break;}
			}
		}
		if (match==1){
			printf("Case #%d: %d\n",kasus+1,Ans);}
		else if (match>1){
			printf("Case #%d: Bad magician!\n",kasus+1);}
		else{
			printf("Case #%d: Volunteer cheated!\n",kasus+1);}
	}
	return 0;}