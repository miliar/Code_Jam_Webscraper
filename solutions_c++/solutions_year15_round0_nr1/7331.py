#include<iostream>

using namespace std;

int main (){
	int n,s,req,standing,sint;
	char si[1002];
	cin>>n;
	for(int i=0; i<n; i++){
		req = 0;
		standing = 0;
		cin>>s>>si;
		for(int j=0;j<=s;j++){
			//cout<<(si[j]-'0')<<" ";
			sint = (si[j] - '0');
			//cout<<"standing "<<j<<" :"<<standing<<endl;
			if(sint > 0){
				
				if(j<=standing){
					standing+=sint;
					
				}
				else{
					req = req + (j-standing);
					standing = j + sint;
					//cout<<"req:"<<req<<endl;
				}
			}
		}
		//cout<<si<<endl;
		cout<<"Case #"<<i+1<<": "<<req<<endl;
	}
return 0;
}
