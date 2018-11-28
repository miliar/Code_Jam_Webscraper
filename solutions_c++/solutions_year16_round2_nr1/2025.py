#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

int main(){
	int hash[27];
	int ans[30];
	int t,i,j,k,len,temp;
	string S;
	cin>>t;
	for(i=1;i<=t;i++){
		cin>>S;
		len = S.length();
		k=0;
			for(j=0;j<=26;j++) ans[j]=hash[j]=0;
		for(j=0;j<len;j++) hash[ S[j]-'A' +1 ]++;
		//zero
		if(hash['Z'-'A'+1]!=0){
			temp = hash[26];
			hash['E'-'A'+1]-=temp; hash['R'-'A'+1]-=temp; hash['O'-'A'+1]-=temp;
			ans[0]=temp;
		}
		//TWO
		if(hash['W'-'A'+1]!=0){
			temp = hash['W'-'A'+1];
			hash['T'-'A'+1]-=temp; hash['O'-'A'+1]-=temp;
			ans[2]=temp;
		}	
		//EIGHT
		if(hash['G'-'A'+1]!=0){
			temp = hash['G'-'A'+1];
			hash['E'-'A'+1]-=temp; hash['I'-'A'+1]-=temp; hash['H'-'A'+1]-=temp; hash['T'-'A'+1]-=temp;
			ans[8]=temp;
		}
		//THREE

		if(hash['H'-'A'+1]!=0){
			temp = hash['H'-'A'+1];
			hash['T'-'A'+1]-=temp; hash['R'-'A'+1]-=temp; hash['E'-'A'+1]-=temp; hash['E'-'A'+1]-=temp;
			ans[3]=temp;
		}

		////FOUR
		if(hash['R'-'A'+1]!=0){
			temp = hash['R'-'A'+1];
			hash['F'-'A'+1]-=temp; hash['O'-'A'+1]-=temp; hash['U'-'A'+1]-=temp;// hash['E'-'A'+1]-=temp;
			ans[4]=temp;
		}		

		//FIVE
		if(hash['F'-'A'+1]!=0){
			temp = hash['F'-'A'+1];
			hash['I'-'A'+1]-=temp; hash['V'-'A'+1]-=temp; hash['E'-'A'+1]-=temp;// hash['E'-'A'+1]-=temp;
			ans[5]=temp;
		}

		//SIX
		if(hash['X'-'A'+1]!=0){
			temp = hash['X'-'A'+1];
			hash['S'-'A'+1]-=temp; hash['I'-'A'+1]-=temp;// hash['E'-'A'+1]-=temp; hash['E'-'A'+1]-=temp;
			ans[6]=temp;
		}	
		//SEVEN
		if(hash['S'-'A'+1]!=0){
			temp = hash['S'-'A'+1];
			hash['E'-'A'+1]-=temp; hash['V'-'A'+1]-=temp; hash['E'-'A'+1]-=temp; hash['N'-'A'+1]-=temp;
			ans[7]=temp;
		}

		//ONE
		if(hash['O'-'A'+1]!=0){
			temp = hash['O'-'A'+1];
			hash['N'-'A'+1]-=temp; hash['E'-'A'+1]-=temp;// hash['E'-'A'+1]-=temp; hash['E'-'A'+1]-=temp;
			ans[1]=temp;
		}

		//NINE
		if(hash['I'-'A'+1]!=0){
			temp = hash['I'-'A'+1];
			hash['N'-'A'+1]-=temp; hash['N'-'A'+1]-=temp; hash['E'-'A'+1]-=temp; //hash['E'-'A'+1]-=temp;
			ans[9]=temp;
		}

		printf("Case #%d: ",i);
		for(j=0;j<=9;j++){
			temp = ans[j];
			while(temp--){
				cout<<j;
			}
		}
		printf("\n");
	}

}