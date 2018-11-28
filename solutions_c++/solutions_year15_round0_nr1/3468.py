#include<iostream>
#include<string>
using namespace std;
string s;
int main(){
	int nn,n,now,cnt,r=1,i;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>nn;
	while(nn--){
		cin>>n>>s;
		for(i=cnt=now=0;i<=n;i++){
			if(now>=i)
				now+=s[i]-'0';
			else{
				cnt++;
				now=now+s[i]-'0'+1;
			}
		}
		cout<<"Case #"<<r<<": "<<cnt<<endl;
		r++;
	}
	return 0;
}