#include <iostream>
#include <bits/stdc++.h>
using namespace std;
// @author mohammed Abd El-Sattar Ahmed 
// FCI-Cu 2015 
int main() {
	
	int testCases,num,totalNumberOfFriends,diff,totalNumOfAudience;
	cin>>testCases;
	string line;
	
	for(int i= 0; i<testCases; i ++){
		cin>>num>>line;
		totalNumberOfFriends=totalNumOfAudience=0;
		for(int q=0 ;q<=num ; q++){
		
		//	cout<<q<<" "<<totalNumOfAudience<<" "<<totalNumberOfFriends<<endl;
			diff =(q-totalNumOfAudience);
			if(q==0 && line[q]=='0' && num>0 ){
				totalNumberOfFriends++;
				totalNumOfAudience++;
			}
				
			if(diff>0 ){
				totalNumberOfFriends+=diff;
				totalNumOfAudience+=diff;
			}
			if(line[q]!='0')
				totalNumOfAudience+=line[q]-48;
		}
		cout<<"Case #"<<(i+1)<<": "<<totalNumberOfFriends<<endl;
	}
		
	
	return 0;
}
