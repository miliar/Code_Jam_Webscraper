#include <iostream>
#include <string>
#include <cmath>


using namespace std ;




int main(){
	string s;
	long long maxs,people=0,cnt=0,t;
	cin>>t;

	for (int i=0; i<t; i++){
		cnt=0;
		cin>>maxs>>s;
		people=s[0]-'0';
		for (int j=0,n=s.size();j<n; j++){
			if (people>=j && j!=0){
				people+=s[j]-'0';
			}
			else if (people<j){
				cnt+=(j-people);
				people+=(j-people)+(s[j]-'0');

			}
		}
		cout<<"Case #"<<i+1<<": "<<cnt<<endl;

	}

}


