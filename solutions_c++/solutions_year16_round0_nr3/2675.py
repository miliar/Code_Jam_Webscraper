#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

ll ar[11];
ll pan[11][16];

ll cekprim(ll mas){
	ll i;
	for(i=2;i<=sqrt(mas);i++){
		if(mas%i==0){
			return i;
		}
	}
	return -1;
}

bool bis(ll bil){
	ll val=cekprim(bil);
	if(val==-1){
		return false;
	}
	ll bas,ca,i;
	ar[2]=val;
	bitset<16> foo(bil);
	for(bas=3;bas<=10;bas++){
		ca=0;
		for(i=0;i<16;i++){
			ca+=foo[i]*pan[bas][i];
		}
		val=cekprim(ca);
		if(val==-1){
			return false;
		}
		ar[bas]=val;
	}
	return true;
}

int main(){
	freopen ("myfile.txt","w",stdout);
	
	//generator x pangkat y
	ll i,j;
	for(i=2;i<=10;i++){
		pan[i][0]=1;
		pan[i][1]=i;
	}
	for(i=2;i<16;i++){
		for(j=2;j<=10;j++){
			pan[j][i]=pan[j][i-1]*pan[j][1];
		}
	}
	ll left=50,bil;
	scanf("%*d %*lld %*lld");
	printf("Case #1:\n");
	for(bil=(1<<15)+1;bil<=((1<<16)-1)&&left>0;bil+=2){
		bitset<16> foo(bil);
		if(bis(bil)){
			left--;
			cout<<foo;
			for(i=2;i<=10;i++){
				printf(" %lld",ar[i]);
			}
			printf("\n");
		}
	}
	
	fclose (stdout);
}
