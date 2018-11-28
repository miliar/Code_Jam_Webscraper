#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;


bool huiwen(long long int i){
	char a[20];
	int j=0;
	while(i!=0){
		a[j++]=i%10L;
		i=i/10L;
	}
	for(int k=0;k<(j+1)/2;++k){
		if(a[k]!=a[j-k-1])
			return false;
	}
	return true;
}

int main()
{
	int T;
	long long int A,B;
	int k=0;
	long long int i,a,b;

	freopen("I:/C-small-attempt0.in", "r", stdin);
	cin>>T;
	bool no=false;
	int cou=0;
	while(k++<T){
		cin>>A>>B;
		cou=0;
		a=ceil(sqrt((long double)A));
		b=floor(sqrt((long double)B));
		for(i=a;i<=b;++i){
			if(huiwen(i) && huiwen(i*i)) 
				++cou;
		}
	

		cout<<"Case #"<<k<<": "<<cou<<endl;
	}//while
	fclose(stdin);
	return 0;
}