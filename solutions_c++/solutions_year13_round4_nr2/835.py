#include <iostream>
#include <fstream>
using namespace std;

ofstream fout("out.txt");
int t;
long long n,p;
long long p2[55];
int main(){
	p2[0]=1;
	for(int i=1;i<55;i++){
		p2[i]=2*p2[i-1];
	}
	cin>>t;
	for(int y=1;y<=t;y++){
		cin>>n>>p;
		int sol1=-1,sol2=-1;
		
		int pe;
		for(int i=p2[n]-1;i>=0;i--){
			long long kkk=p2[n];
			pe=p2[n]-1-i;
			while(pe>0){
				kkk/=2;
				pe--;
				if(kkk<=p){
					sol1=i;
					break;
				}

				pe/=2;
			}
			if(sol1!=-1){
				break;
			}
		}
		
		for(int i=p2[n]-1;i>=0;i--){
			int pp=p;
			pe=i;
			long long kkk=p2[n];
			while(pe>0){
				
				kkk/=2;
				pe--;
				pe/=2;
				pp-=kkk;
			}
			if(pp>0){
				sol2=i;
				break;
			}
		}
		fout<<"Case #"<<y<<": "<<sol2<<" "<<sol1<<endl;
	}
}