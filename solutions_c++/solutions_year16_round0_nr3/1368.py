#include<iostream>
#include<math.h>
#include<omp.h>
using namespace std;

const int branch=16;
int t,T;
int N,N2,J,L,c,c2,i,j,b[40],b2[40],count,prime,rem;
unsigned long long int n[11],mul;
unsigned long long int f[11],sqt;

void small(){
	L=1<<N;
	for(c=(L>>1)+1;/*(c<L)&&*/(count<J);c+=2){
		prime=0;
		for(i=1,j=0;i<L;i<<=1,++j){
			if(c&i)
				b[j]=1;
			else
				b[j]=0;
		}
		for(i=2;i<=10;++i){
			n[i]=0;
			for(j=N-1;j>=0;--j)
				n[i]=n[i]*i+b[j];
			if(n[i]%2==0){
				f[i]=2;
			}
			else{
				sqt=(unsigned long long int)sqrt(n[i]);
				for(j=3;j<=sqt;j+=2){
					if(n[i]%j==0){
						f[i]=j;
						break;
					}
				}
				if(j>sqt){
					prime=1;
					break;
				}
				if(n[i]%f[i])
					cout<<n[i]<<' '<<f[i]<<' '<<n[i]%f[i]<<'\n';
			}
		}
		if(prime)
			continue;
		else{
			++count;
			for(i=N-1;i>=0;--i)
				cout<<b[i];
			for(i=2;i<=10;++i)
				cout<<' '<<f[i];
			cout<<'\n';
		}
	}
}

void large(){
	N2=N;
	rem=N-branch;
	N=branch;
	mul=(1<<rem)+1;

	for(i=1,j=0;j<=rem;i<<=1,++j)
		if(mul&i)
			b2[j]=1;
		else
			b2[j]=0;
	for(i=2;i<=10;++i){
		f[i]=0;
		for(j=rem;j>=0;--j)
			f[i]=f[i]*i+b2[j];
	}
	c=(1<<(N-1))+1;
	for(count=0;count<J;c+=2){
		c2=c*mul;
		for(i=1,j=0;j<N2;i<<=1,++j)
			if(c2&i)
				b[j]=1;
			else
				b[j]=0;

		n[3]=0;
		for(j=N2-1;j>=0;--j)
			n[3]=n[3]*3+b[j];
		if(n[3]%f[3])
			continue;

		for(i=2;i<10;++i){
			n[i]=0;
			for(j=N2-1;j>=0;--j)
				n[i]=n[i]*i+b[j];
		}

		/*
		for(i=2;(i<3)&&(n[i]%f[i]==0);++i);
		if(i<10)
			continue;
		*/

		for(i=N2-1;i>=0;--i)
			cout<<b[i];
		for(i=2;i<=10;++i)
			cout<<' '<<f[i];
		cout<<'\n';
		++count;
	}
}

int main(){
	cin>>T;
	for(t=1;t<=T;++t){
		count=0;
		cin>>N>>J;
		cout<<"Case #"<<t<<":\n";
		if(N>3){
			if(N<=branch)
				small();
			else
				large();
		}
	}
	return 0;
}
