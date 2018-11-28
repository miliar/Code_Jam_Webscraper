#include <iostream>
#include <fstream>
using namespace std;
int abs(int a){
	return (a>0)?a:-a;
}

ofstream fout("outt.txt");

int heap[10001];
int T,n,x,y;
int main(){
	heap[0]=1;
	for(int i=1;i<=10000;i++){
		heap[i]=heap[i-1]+4*i+1;
	}
	cin>>T;
	fout.precision(10);
	fout<<fixed;
	for(int g=1;g<=T;g++){
		cin>>n>>x>>y;
		if(abs(x)+y==0){
			fout<<"Case #"<<g<<": "<<1<<endl;
			continue;
		}
		if(heap[(abs(x)+y)/2-1]>=n){
			fout<<"Case #"<<g<<": "<<0<<endl;
			continue;
		}
		if(heap[(abs(x)+y)/2]<=n){
			fout<<"Case #"<<g<<": "<<1<<endl;
			continue;
		}
		if(x==0){
			fout<<"Case #"<<g<<": "<<0<<endl;
			continue;
		}
		n-=heap[(abs(x)+y)/2-1];
		if(n>abs(x)+2*y){
			fout<<"Case #"<<g<<": "<<1<<endl;
			continue;
		}
		long double p=1.0,sl=0;
		for(int i=1;i<=n;i++){
			p/=2;
		}
		for(int i=1;i<=n;i++){
			p*=(long double)(n-i+1);
			p/=i;
			if(i>=y+1){
				sl+=p;
			}
			
		}
		fout<<"Case #"<<g<<": "<<sl<<endl;
	}
}