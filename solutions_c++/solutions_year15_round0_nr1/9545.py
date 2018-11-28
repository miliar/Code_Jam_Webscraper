#include <iostream>
#include <vector>
using namespace std;
int main(){
	int t,c;
	cin>>t;
	c=t;
	while(t--){
		int S,n;
		string s;
		cin>>S>>s;
		n = s.length();
		vector<int> v(n);
		for(int i=0;i<n;i++){
			v[i]=s[i]-'0';
		}
		int addCount =0;
		int tCount=v[0];
		for(int i=1;i<n;i++){
			if( tCount<i && v[i]!=0){
				addCount+=i-tCount;
				tCount=i+v[i];
			}
			else{
				tCount+=v[i];
			}
		}
		cout<<"Case #"<<c-t<<": "<<addCount<<endl;
	}
}