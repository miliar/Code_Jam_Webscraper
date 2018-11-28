#include <iostream>
#include <cstdio>
using namespace std;

int main(int argc, char *argv[]) {
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int cases;
	cin>>cases;
	int ccase=1;
	while(ccase<=cases){
		int n;
		int out=10;
		int array[10]={0,0,0,0,0,0,0,0,0,0};
		
		cin>>n;
		
		if(n==0)
			cout<<"Case #"<<ccase<<": INSOMNIA\n";
		else{
			int mult=1;
			
			while(out!=0){
				
				int aux=n*mult;
				while(aux!=0){
					if(array[aux%10]==0){
						array[aux%10]=1;
						out--;
					}
					aux=aux/10;
				}
				mult++;
			}
			cout<<"Case #"<<ccase<<": "<<n*(mult-1)<<"\n";
		}
		
		
		ccase++;
	}
	return 0;
}

