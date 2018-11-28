#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;
#define FORI for(lli i=0;i<str.length();i++)
#define FORI1 for(lli i=1;i<n;i++)


int main(){
	freopen("input_file_name.in","r",stdin);
	freopen("output_file_name.out","w",stdout);
lli t,f=1;
	cin>>t;
	while(f<=t){
		lli a,count=0,audhave=0,friendreq=0;
		string str;
		cin>>a;
		cin>>str;
 
		FORI{
 
			if (audhave<i && str[i]!='0'){
				friendreq+=i-audhave;
				audhave+=friendreq;
			}
				
 
			audhave+=str[i]-'0';
		}
		if (audhave<str.length() && str[str.length()-1]!='0')
		friendreq+=str.length()-audhave;
	
	cout<<"Case #"<<f<<": "<<friendreq<<endl;
	f++;
	//cin.get();
	}
	return 0;
}