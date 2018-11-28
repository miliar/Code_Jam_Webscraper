#include <iostream>
#include <cstdio>
using namespace std;
bool completo(int num[]){
	if(num[0]*num[1]*num[2]*num[3]*num[4]*num[5]*num[6]*num[7]*num[8]*num[9] == 1) return true;
	else return false;
}
void numeros(int num[],int n){
	while(n!=0){
		num[n%10]=1;
		n=n/10;
	}
}
int main(int argc, char *argv[]) {
	int t,i,n,j,l;
	freopen("A-large.in","r",stdin);
	freopen("Counting Sheep.out","w",stdout);
	
	cin>>t;
	for(i=1; i<=t; i++){
		cin>>n;
		
		if(n==0) cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		else{
			int num[10]={0,0,0,0,0,0,0,0,0,0};
			j=1;
			while(!completo(num)){
				l=j*n;
				numeros(num,l);
				j++;
			}
			cout<<"Case #"<<i<<": "<<l<<endl;
		}
		
		
	}
	
	return 0;
}

