#include <iostream>
#include <string>
#include <cstdio>
using namespace std;
int T,n;
string s;

bool vow(char a) {
	if((a=='a')||(a=='e')||(a=='i')||(a=='o')||(a=='u')) return 1;
	return 0;
}

bool good(string x){
	//cout<<x<<endl;	
	int l=x.size();
	for(int i=0;i<=l-n;i++) {
		int z=0;
		for(int j=0;j<n;j++) {
			z+=!vow(x[i+j]);	
	 	}
	 	//cout<<z<<endl;	
	 	if(z==n) return 1;
	}
	return 0;
}

int main(){
 	freopen("a.in","rt",stdin);
 	freopen("a.out","wt",stdout);
 	cin>>T;	
 	for(int x=1;x<=T;x++) {
 		int ans=0;
 		cin>>s>>n;
 		int l=s.size();
 		for(int i=0;i<l;i++) {
 		 	for(int j=i;j<l;j++) {
 		 		ans+=good(s.substr(i,j-i+1));	
 		   	}
 		}
 		printf("Case #%d: %d\n",x,ans);
	}	
 	return 0;
}
