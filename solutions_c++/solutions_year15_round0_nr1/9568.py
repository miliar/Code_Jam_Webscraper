#include<iostream>
#include<cstdio>
using namespace std;

int ar[1005];
char br[1005];
int cr[1005];
int main()
{
	int T;
	cin>>T;
	
	for(int a=0;a<=T-1;a++){
		
		int smax;
		cin>>smax;
		
		cin>>br;
		
		for(int b=0;b<=smax;b++){
			
			if(br[b]=='0'){
				ar[b]=0;
			}
			if(br[b]=='1'){
				ar[b]=1;
			}
			if(br[b]=='2'){
				ar[b]=2;
			}
			if(br[b]=='3'){
				ar[b]=3;
			}
			if(br[b]=='4'){
				ar[b]=4;
			}
			if(br[b]=='5'){
				ar[b]=5;
			}
			if(br[b]=='6'){
				ar[b]=6;
			}
			if(br[b]=='7'){
				ar[b]=7;
			}
			if(br[b]=='8'){
				ar[b]=8;
			}
			if(br[b]=='9'){
				ar[b]=9;
			}
		}
		
		int m=0,n=0;
		
		for(int c=0;c<=smax;c++){
			
			m=m+ar[c]-1;
			
			if(m<n){
				
				n=m;
			}
			
			
		}
		
		cr[a]=-n;
	}
	
	for(int a=0;a<=T-1;a++){
		
		cout<<"case #"<<a+1<<": "<<cr[a]<<endl;
	}
	return 0;
}
