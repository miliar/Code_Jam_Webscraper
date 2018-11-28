#include<bits/stdc++.h>
using namespace std;
bool d[15],fin;
long long aux,num;
int t;
int main(){
	cin >> t;
	for(int cases=1;cases<=t;cases++){
		cin >> num;
		if(num==0) cout << "Case #"<<cases<<": INSOMNIA"<<endl;
		for(int i=0;i<10;i++) d[i]=0;
		for(int i=1;i<100;i++){
			aux=num*(long long)i;
			d[aux%10]=1;
			while(aux/10!=0){
				aux/=10;
				d[aux%10]=1;
			}
			fin=true;
			for(int k=0;k<10;k++) if(!d[k]) fin=false;
			if(fin){
				cout << "Case #"<<cases<<": "<<num*i<<endl;
				break;
			}
		}
	}
}

