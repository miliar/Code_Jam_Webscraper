#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t ;
	cin>>t;
	string s;
	for(int x = 1 ; x <= t ; x++){
		cin>>s;
		int ans=0;
		bool flag = false , f =true;
		int y=0;
		while(!flag){
			for(int i = 0 ; i < s.size() ; i++){
				if(s[i]=='-'){
					y=i;
				if(s[i]=='+'&&y!=0)
					break;
				}
			}
			if(s[y]=='-'){
			for(int i = 0 ; i <= y ; i++){
				if(s[i]=='-')s[i]='+';
				else s[i]='-';
			}
			
			ans++;
			}
			y=0;
			for(int i = 0 ; i < s.size() ; i++){
				if(s[i]=='-'){flag=false;break;}
				else flag=true;
			}
		}
		cout<<"Case #"<<x<<": "<<ans<<"\n";
	}

}