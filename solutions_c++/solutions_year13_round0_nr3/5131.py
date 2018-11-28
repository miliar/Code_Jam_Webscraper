#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;
long long int A,B;
int T;
ofstream fout("out.txt");
long long int sol[10000],h=0;
bool is_pal(long long int g){
	int arr[20],f=0;
	while(g>0){
		arr[f++]=g%10;
		g/=10;
	}
	for(int i=0;i<f/2;i++){
		if(arr[i]!=arr[f-1-i])return false;
	}
	return true;
}
int main(){
	for(long long int i=1;i<=10000000;i++){
		if(is_pal(i)){
			if(is_pal(i*i)){
				sol[h++]=i*i;
			}
		}
	}
	cin>>T;
	int sl;
	for(int tt=1;tt<=T;tt++){
		sl=0;
		cin>>A>>B;
		for(int i=0;i<h;i++){
			if(sol[i]>=A && sol[i]<=B){
				sl++;
			}
		}
		fout<<"Case "<<tt<<": "<<sl<<endl;
	}
}