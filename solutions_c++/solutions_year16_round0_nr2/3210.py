#include<bits/stdc++.h>
using namespace std;

int main(){
	freopen ("myfile.txt","w",stdout);
	int t,i,bit,h,hsl,cal,j;
	scanf("%d\n",&t);
	string soal;
	for(i=0;i<t;i++){
		getline(cin,soal);
		soal=soal+"+";
		hsl=0;
		for(j=soal.length()-2;j>=0;j--){
			if(soal[j]!=soal[j+1]){
				hsl++;
			}
		}
		printf("Case #%d: %d\n",i+1,hsl);
	}
	
	
	fclose (stdout);
}
