#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;

int main(){
	ofstream fout("ans.txt");
	ifstream fin("inp.IN");
	int t;
	long long n,orig,i;
	fin>>t;
	int tt=0;
	while(tt++!=t){
		fin>>n;
		if(n==0){
			fout<<"Case #"<<tt<<": INSOMNIA\n";
		}else{
			i=1;
			int a[10]={0};
			int index;
			while(1){
				orig=i*n;
				while(orig>0){
					index=orig%10;
					a[index]=1;
					orig/=10;
				}
				
				++i;
				int j=0;
				for(;j<10;++j)
					if(a[j]==0)
						break;
				if(j==10)
					break;		
			}
			long long ans=(i-1)*n;
			fout<<"Case #"<<tt<<": "<<ans<<"\n";	
		}
		
	}

}
