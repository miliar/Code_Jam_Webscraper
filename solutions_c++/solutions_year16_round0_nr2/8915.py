#include <iostream>
#include <fstream>
#include <cstdlib>
#include <time.h>
#include <vector>
#include <cstring>

using namespace std;

int main(){
	int t,i,j,l,count,x,len;
	string s,temp;
	cin>>t;
	int k = t;
	while(k){
		cin>>s;
		len = s.length();
		count = 0;
		while(1){
			j = -1;
			// cout<<"---------------------------------------------------------------"<<endl;
			// cout<<"hey "<<count<<endl;
			// for(i = 0;i<len;i++){
			// 	cout<<s[i];
			// }
			// cout<<endl;
			for(i = 0;i<len;i++){
				if(s[i] == '-')
					j = i;
			}
			if(j == -1){
				cout<<"Case #"<<t-k+1<<": "<<count<<endl;
				break;
			}	
			else{
				temp = s;
				if(s[0]!='+'){//agar pehla wala + nahi hai toh
					for(i = j;i>=0;i--){
						if(temp[i] == '-')
							s[j-i] = '+';
						else if(temp[i] == '+')
							s[j-i] = '-';
					}
				}//iske baad bata
				else{
					for(i = 0;i<j;i++){
						if(s[i] == '+'){
							l = i;
						}
						else 
							break;
					}
					for(i = l;i>=0;i--){
							s[l-i] = '-';
					}
				}
			}
			count++;	
		}
		k = k-1;
	}
}
