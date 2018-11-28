#include <iostream>
#include <string.h>
using namespace std;
int main(){
	int i,t,n,j,pos,ans;
	char s[105];
	cin>>t;
	j=0;
	while(t--){
		j++;
		cin>>s;
		n=strlen(s);
		pos=0;
		ans=0;
		for(i=0;i<n;){
			if(s[i]==s[pos]){
				i++;
			}
			else{
				ans+=1;
				pos=i;
			}
		}
		if(s[pos]=='-')
			ans+=1;
		cout<<"Case #"<<j<<": "<<ans<<"\n";
	}
	return 0;
}