#include<iostream>
#include<algorithm>

using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		
		int smax;
		cin>>smax;
		string s;
		cin>>s;
		
		int j=0,count=0,num=0,var;
		while(j <= smax){
			//cout<<(count+s[j]-'0')<<" "<<(j+1)<<endl;
			//break;
			if( (count+s[j]-'0') < (j+1) ){
				//cout<<"j"<<j<<endl;
				var = j+1-(count+s[j]-'0');
				num += var;
				count += var;
			}else{
				count += (s[j]-'0');
			}
			j++;
		}
		cout<<"Case #"<<i<<": "<<num<<endl;
		
	}
	return 0;
}
