//Google Code Jam--Standing Ovation
#include<bits/stdc++.h>

using namespace std;


int main(void){
	
	string S;
	int testCases,i,standing=0,extra=0,length,Case=1;
	
	scanf("%d",&testCases);
	
	while(testCases--){
		
		cin>>length>>S;
		
		length++;
		
		standing=0;extra=0;
		for(i=0;i<length;i++){
			
			if(standing>=i) standing+=S[i]-'0';			
			
			else if(S[i]>'0'){
				
				int reqd=i-standing;
				extra+=reqd;
			    
			    standing+=extra+S[i]-'0';
			    
			}
			
		}
		
		printf("Case #%d: %d\n",Case++,extra);
		
	}
	
	return 0;
	
}
