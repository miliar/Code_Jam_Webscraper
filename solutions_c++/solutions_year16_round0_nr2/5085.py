#include<fstream>
using namespace std;
ifstream cin("B-large.in");
ofstream cout("B-large.out");
string s;
int t,n,in,rez;
bool u;
int main(){
	cin>>t;
	for(int o=1;o<=t;o++){
		cin>>s;
		n=s.length();
		u=true;
		rez=0;
		int i=0;
		while(u){
				i=0;
				if(s[i]=='-'){
					in=i;
					while(s[i]=='-'&&i<n)i++;
					for(int j=in;j<i;j++)s[j]='+';
					
					rez++;
				}else{ in=i;
					   while(s[i]=='+'&&i<n)i++;
					   if(i==n)u=false;
					   for(int j=in;j<=i;j++)s[j]='-';
					   rez++;
					}
			}
			 cout<<"Case #"<<o<<": "<<rez-1<<"\n";	
	}
   
}
