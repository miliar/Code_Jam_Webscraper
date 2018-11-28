#include<bits/stdc++.h>
using namespace std;
int maxi=0;
void func(long long p){
	map<int,int>m;
	int r=0;
	for(int i=1;i<1000;i++){
		long long h=p*i;
		while(h!=0){
			int g=h%10;
			if(m[g]==0){
				m[g]=1;
				r++;
				if(r==10){
					cout<<p*i<<endl;
					
					return;
				}
			}
			h/=10;
		}
	}
}
int main(){
	long long a,b,c,d,e,f=0,g,h;
	freopen("A-large.in","r",stdin);
	freopen("output_file.out","w",stdout);
	cin>>a;
	while(a--){
		cin>>b;
		
	
		if(b==0) cout<<"Case #"<<++f<<": INSOMNIA"<<endl;
		else{
			cout<<"Case #"<<++f<<": ";
			func(b);
		}
	
	}
}
