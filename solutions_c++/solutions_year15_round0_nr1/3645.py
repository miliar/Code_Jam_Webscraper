#include <bits/stdc++.h>
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("output_file_name.out","w",stdout);
	int T;
	cin>>T;
	for(int j=0;j<T;j++){
		int smax;
		cin>>smax;
		string s;
		cin>>s;
		long long standing = 0;
		long long needed = 0;
		for(int i=0;i<s.size();i++){
			if(standing<i){
				needed+=(i-standing);
				standing++;
			}
			standing+=((int)s[i]-48);
		}
		cout<<"Case #"<<(j+1)<<": "<<needed<<endl;
	}
	return 0;	
}