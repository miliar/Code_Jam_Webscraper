#include <iostream>
#include <cmath>


using namespace std;

const long long int mod=1000000000000000;

long long int num=0,w=1, a[50][10],p=0;

long long int prime(long long int s, long long int k){
	long long int i,m;

	m=sqrt(s);
	for(i=3;i<=m;i+=2)
		if(s%i==0){
			a[p][k-1]=i;
			return s;
		}

	return -1;
}

long long int convert(long long n){
	long long int i,m=0,k=1,j;
	j=num;
	while(j!=0){
		i=j%10;
		m+=(k*i);
		k*=n;
		j/=10;
	}
	return m;
}

void toBinary(long long int n){
    if (n / 2 != 0) {
        toBinary(n / 2);
    }
    //printf("%d", n % 2);
    num+=(n%2)*mod/w;
    w*=10;
}

int main(){
	long long int i,t,j,k,s,f,flag;
	cin>>t>>i>>j;
	for(i=32769;i<65536;i+=2){
		toBinary(i);
		//cout<<num<<" ";
		k=num/mod;
		flag=0;
		if(k%10==1){
			for(k=2;k<=10;k++){
				s=convert(k);
				f=prime(s,k);
				if(f==-1){
					flag=1;
					break;
				}
			}
			if(flag==0){
				a[p][0]=num;
				p++;
			}
			if(p==50)
				break;
		}
		num=0;
		w=1;

	}

	cout<<"Case #"<<1<<": "<<endl;
	for(i=0;i<50;i++){
		for(j=0;j<10;j++)
			cout<<a[i][j]<<" ";
		cout<<endl;
	}

	return 0;
	}