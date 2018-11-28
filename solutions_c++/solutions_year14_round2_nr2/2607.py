#include<iostream>
#include<fstream>
using namespace std;

#define tin fin
#define tout fout




int main(){

	int testC,caseN=1,ans,a,b,k,number;
	
	ifstream fin ("bin.in");
	ofstream fout ("bout.txt");
	
	tin>>testC;
	
	
	while(testC--){
		ans=0;
		tin>>a>>b>>k;
		
		//choose biggest
		for(int i=0;i<a;i++){
			for(int j=0;j<b;j++){
				number=i&j;
				if(number<k && number>=0){
					ans++;
					//cout<<i<<","<<j<<endl;
				}
			}
		}
	
	
		tout<<"Case #"<<caseN++<<": "<<ans<<endl; 
	}




	return 0;
}
