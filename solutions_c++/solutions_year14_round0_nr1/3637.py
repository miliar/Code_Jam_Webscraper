#include<iostream>
#include<string>
#include<sstream>
using namespace std;

int main(){
	int cases,crap=1;
	string s="";
	cin>>cases;
	while(cases>0){
		int arr1[4][4],arr2[4][4],a1,a2,match=0;
		bool bad=false;
		cin>>a1;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>arr1[i][j];
			}
		}
		cin>>a2;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>arr2[i][j];
			}
		}
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(arr1[a1-1][i]==arr2[a2-1][j]){
					if(match==0){
						match=arr1[a1-1][i];
					}else{bad=true;break;}
				}
			}
		}
		stringstream ss;
		ss<<"Case #"<<crap<<": ";
		string str=ss.str();
		s=s+str;
		if(bad){
			s=s+"Bad magician!\n";
		}else if(match==0){
			s=s+"Volunteer cheated!\n";
		}else{
			stringstream ss;
			ss << match<<endl;
			string str = ss.str();
			s=s+str;
		}		
		cases--;
		crap++;
	}
	cout<<s;
	return 0;
}
		
