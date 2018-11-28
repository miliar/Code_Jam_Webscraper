#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<cstdlib>
using namespace std;

int main(){
	int t,n,i,j,ca=0;;
	string a,b;
	cin>>t;
	while(t--){
		ca++;
		int l1,l2,c =0;
		cin>>n;
		cin>>a>>b;
		bool flag = true;
		l1 = a.length();
		l2 = b.length();
		for(i=0,j=0;i<l1 && j<l2 ;){
			if(a[i]==b[j]){
				i++;
				j++;
			}else{
				if(i>0 && j>0){
				
				if(a[i]==b[j-1]){
					c++;
					i++;

				}else{
					if(b[j]==a[i-1]){
						c++;
						j++;
					}else{
						flag = false;
						break;
					}
				}
				
				}
				else{
					flag = false;
					break;
				}
			}
		}
		while(i!=l1){
			if(i>0){
			if( a[i]==a[i-1]){
				c++;
				i++;
			}else{
				flag = false;
				break;
			}
		}else{
			flag = false;
			break;
		}
		}
		
		while(j!=l2){
			if(j>0){
			
			if( b[j]==b[j-1] ){
				c++;
				j++;
			}else{
				flag = false;
				break;
			}
		}
		else{
			flag = false;
			break;
		}
		}
		
	
			
		if(flag){
			cout<<"Case #"<<ca<<": "<<c<<endl;
		}else{
			cout<<"Case #"<<ca<<": Fegla Won"<<endl;
		}
		
		
	}
	
	return 0;
}
