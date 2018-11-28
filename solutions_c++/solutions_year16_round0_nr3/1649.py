#include<iostream>
#include<cstring>

using namespace std;

int main(){
	int t,n,j_;
	cin>>t;
	
	while(t--){
		cin>>n>>j_;

		string s="";
		s+='1';
		for(int i=1;i<n-1;i++){
			s+='0';
		}
		s+='1';

		//cout<<s<<endl;
		int net=0,flag=0;
		cout<<"Case #1:"<<endl;
		for(int i=1;i<n-1;i+=2){
			for(int j=i+2;j<n-1;j+=2 ){
				for(int k=2;k<n-1;k+=2){
					for(int l=k+2;l<n-1;l+=2){

						if(net==j_){
							flag=1;
							break;
						}

						s[i]=s[j]=s[k]=s[l]='1';
						cout<<s<<" 3 2 3 2 7 2 3 2 3"<<endl;
						net++;
						s[i]=s[j]=s[k]=s[l]='0';
					}
					if(flag==1){
						break;
					}
				}
				if(flag==1){
					break;
				}
			}
			if(flag==1){
				break;
			}
		}


		//cout<<net<<endl;



	}




	return 0;
}