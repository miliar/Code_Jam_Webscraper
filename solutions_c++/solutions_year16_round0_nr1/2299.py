#include <iostream>
#include <fstream>
using namespace std;
int main(){
	//ifstream fin ("A-small-attempt0.in");
	//ofstream fout ("A-small-attempt0.out");
	ifstream fin ("A-large.in");
	ofstream fout ("A-large.out");
	int t,i,j,k,r;
	long long n,ans,temp;
	bool found;
	int c[10];
	fin>>t;
	for(i=1;i<=t;++i){
		ans=0;
		for(k=0;k<10;++k){
			c[k]=0;
		}
		found=false;
		fin>>n;
		if(n==0){
			fout<<"Case #"<<i<<": "<<"INSOMNIA"<<"\n";
		}else{
			j=1;
			while(!found){
				ans=n*j;
				found=true;
				temp=ans;
				while(temp>0){
					r=temp%10;
					c[r]=1;
					temp/=10;
				}
				for(k=0;k<10;++k){
					if(c[k]==0){
						found=false;
						break;
					}
				}
				++j;
			}
			fout<<"Case #"<<i<<": "<<ans<<"\n";
		}
	}
	return 0;
}
