#include <iostream>
using namespace std;
#include <string>
#include <vector>

std::vector<int> indices(std::string a,int n){
	std::vector<int> first; 
	for(int i=0; i+n<=a.length(); i++){
		std::string b=a.substr(i,n);
		if((b.find("a")!=std::string::npos) || (b.find("e")!=std::string::npos) ||
		   (b.find("i")!=std::string::npos) || (b.find("o")!=std::string::npos) || (b.find("u")!=std::string::npos));
		else first.push_back(i);
	}
	return first;
}

int main(){
	int t;
	cin>>t;
	for(int j=1;j<=t;j++){
		std::string a;
		std::vector<int> vec;
	    int n,ans=0;
	    cin>>a;
	    cin>>n;
	    vec=indices(a,n);
		ans=ans+vec.size();
	    for(int k=n+1; k<=a.length(); k++)
			for(int l=0; l+k<=a.length(); l++) 
				for(int m=0; m<vec.size(); m++){
					if((l+k>=vec[m]+n) && (l<=vec[m])){
						ans++;break;
					}
				}
		cout<<'\n'<<"Case #"<<j<<": "<<ans;
	}
}
