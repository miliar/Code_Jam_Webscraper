#include<bits/stdc++.h>
using namespace std;
int main()
{	
	ifstream fin ("input.txt");        
  	ofstream fout("A-small-practice.out");  
	int T;
	fin>>T;
	for(int t=1;t<=T;t++){
		string a;
		fin>>a;
		int n=a.length();
		bool flag=false;
		int i=0,ans=0;
		while(i<n){
			if(a[i]=='-' && flag==false){
				while(i<n && a[i]=='-'){
					i++;
				}
				flag=true;
				ans++;
			}
			else if(a[i]=='+' && flag==false){
				while(i<n && a[i]=='+'){
					i++;
				}
				flag=true;
			}
			else if(a[i]=='-'){
				while(i<n && a[i]=='-'){
					i++;		
				}
				ans+=2;
			}
			else if(a[i]=='+'){
				while(i<n && a[i]=='+'){
					i++;
				}
			}
		}
		fout<<"Case #"<<t<<": ";
		fout<<ans<<"\n";
	}
}
