#include <iostream>

using namespace std;

void one_lott(int no){
	
	 int a,b,k,ans=0;
	cin>>a>>b>>k;
	
	for( int i=a-1;i>=0;i--){
		for( int j=b-1;j>=0;j--){
			 int c=i&j;
			//cout<<i<<" "<<j<<":"<<c<<" "<<k<<" "<<endl;
			if(c<k){ans++;}
		}
	}
	
	cout<<"Case #"<<no+1<<": ";
	cout<<ans;
}

int main(){
	int t=0;

	cin>>t;
	
	for(int i=0;i<t;i++){
		one_lott(i);
		cout<<endl;
	}
	
}