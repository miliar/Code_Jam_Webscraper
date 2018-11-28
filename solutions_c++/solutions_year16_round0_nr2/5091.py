#include<iostream>
#include<string.h>
#include<algorithm>
#include<fstream>
using namespace std;

int main(){
	ofstream fout("ans2.txt");
	ifstream fin("inp2.IN");
	int t;
	fin>>t;
	int tt=0;
	while(tt++!=t){
		char a[100];
		fin>>a;
		int len=0;
		while(a[len]!='\0')
			++len;
		long long ans=0;
		
		int n=len-1;
		while(n>=0){
//			cout<<"the array is:\n";
//			for(int h=0;h<len;++h)
//				cout<<a[h]<<" ";
//			cout<<"\n";	
			while(n>=0&&a[n]=='+')
				n--;
			if(n==-1)
				break;
				
			if(a[0]=='+'){
				int ctr=0;
				while(a[ctr]=='+'){
					a[ctr]='-';
					++ctr;
				}
				ans+=2;
			}
			else
				++ans;
				
			int i=0,j=n;	
			for(;i<j;++i,--j){
				char temp=a[j];
				if(temp=='+')
					temp='-';
				else
					temp='+';
				int aux=a[i];
				
				if(aux=='+')
					aux='-';
				else
					aux='+';
						
				a[j]=aux;
				a[i]=temp;
			}
			if(i==j){
				if(a[i]=='+')
					a[i]='-';
				else 
					a[i]='+';	
			}				
		}
		
		
		fout<<"Case #"<<tt<<": "<<ans<<"\n";	
//		cout<<"\n\n\n\n\n";	
		
	}

}
