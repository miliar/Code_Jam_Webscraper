#include<iostream>
#include<algorithm>
#include<cstring>
#include <stdlib.h>
#include <fstream>
using namespace std;
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin>>n;
	int index=0;
	while(n--){
		int m;
		
		cin>>m;
		string s;
		cin>>s;
		m=s.length();
		int a=0,ans=0;
		for(int i =0;i<m;i++){
			if(s[i]-'0'){
				if(i<=a)
				a +=s[i] -'0';
				else {
				ans+= (i-a);
				a=i+(s[i]-'0');		
				}	
			}
			/*else{
				if(i>a)
				{
					ans+= (i-a);
					a=i;
				}
			}*/
		}
		cout<<"Case #"<<index+1<<": "<<ans<<endl;
		index++;
	}
	return 0;
}

