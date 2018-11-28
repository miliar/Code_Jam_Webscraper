#include<iostream>

using namespace std;
int main(){
	int t;
	cin>>t;
	for(int i=0; i<t; i++){
		int a=0;
		int tot=0;
		int n;
		cin>>n;
		string ss;
		cin>>ss;
		int S[1001];
		for(int j=0; j<=n; j++){
			S[j]=ss[j]-'0';
		}
		/*0001*/
		/*    */
		for(int j=0; j<=n; j++){
			if( j>tot && S[j]!=0 ){
				a+=(j-tot);
				tot+=a;
			}
			tot+=S[j];
		}
		cout<<"Case #"<<i+1<<": "<<a<<endl;
	}
}
