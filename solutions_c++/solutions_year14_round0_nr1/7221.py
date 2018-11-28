#include<iostream>
#include<map>
#include<cmath>
#include<cstring>
using namespace std;



int main(){
	int t,first,second;
	
	cin>>t;
	int cases=0;
	while(t--){ 
	    cases++;
		cin>>first;
		bool temp[17];
		int arr[4][4];
		
		memset(temp,false,sizeof(temp));
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>arr[i][j];
				if(i==first-1){
					temp[arr[i][j]]=true;
					
				}
		    }
		}
		cin>>second;
		int cont=0;
		int ans=0;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>arr[i][j];
				if(i==second-1){
					if(temp[arr[i][j]]){
						cont++;
						ans=arr[i][j];
					}
					
					
				}
			}
		}
		cout << "Case #"<<cases<<": ";
		if(cont==1){
			cout << ans<<endl;
			
		}
		else if(cont>1)
			cout << "Bad magician!"<<endl;
		else
			cout << "Volunteer cheated!"<<endl;
		
	}
	
	
	
	return 0;
	
	
}