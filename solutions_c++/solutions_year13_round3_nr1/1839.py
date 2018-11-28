//============================================================================
// Name        : codejam_1c_conso.cpp
// Author      : sanjay kumar
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
	int t,n;
	cin>>t;
	string str;
	for(int i=1;i<=t;++i){
		cin>>str>>n;
		int l=n;
		int len = str.length();
		int ans=0;
		while( l <= len ){
			//cout<<"Considering str of size "<<l<<endl;
		   // int lasttype = -1; //conso - 0, vow-1
		    int count=0;

			for(int i=0;i<=len-l;++i){
				count=0;
				for(int j=i; j<i+l; ++j){
				//	cout<<"["<<j<<", "<<j+l-1<<"]"<<endl;
					//cout<<"char = "<<str[j]<<endl;
					if( str[j] == 'a'||
						str[j] == 'e'||
						str[j] == 'i'||
						str[j] == 'o'||
						str[j] == 'u' ){
			//			lasttype=1;
						count=0;
					}else{
						count++;
					}
					//cout<<"count = "<<count<<endl;
					if( count == n ){
						ans++;
						//cout<<"incrementing ans = "<<ans<<endl;

						break;
					}
				}
			}
			l++;

		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}
