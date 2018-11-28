#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	int k = 1;
	while(t--){
		int size;
		cin>>size;
		string s;
		cin>>s;
		int ans =0;
		int man = 0;
		for(int i =0; i < s.size();i++){
			if(s[i] != '0'){
				if(man < i){
					ans += i-man;
					man += i-man;

//				}else{
			    	
				}
				man += s[i] -48;
			} 
		}
		cout<<"Case #"<<k<<": "<<ans<<endl;
		k++;
	}
	return 0;
}

