/*
 * a.cpp
 *
 *  Created on: Mar 23, 2016
 *      Author: kathrine
 */
#include <iostream>
#include<set>
#include<string>
#include<cmath>
#include<iterator>
#include <fstream>
using namespace std;
long long ans[9];
long long base(long long nb,int b,int n){
	long long ans=0;
	for(int i=0;i<n;i++){
		ans+=((nb>>i)&1)*pow(b,i);
	}
	return ans;
}
bool isprime(long long a,int base){
	for(int i=2;i<=sqrt(a);i++){
		if(a%i==0){
			ans[base-2]=i;
			return false;
		}
	}
	return true;
}
string tobinary(long long &a){
	string ans="";
	while(a>0){
		//cout<<ans<<endl;
		ans=char((a%2)+48)+ans;
		a/=2;
	}

	return ans;
}
int main()
{
	ifstream in;
	in.open("C-small-attempt0.in");
	ofstream out;
	out.open("C-small.out");
	for(int i=0;i<9;i++){
		ans[i]=0;
	}
int t,n,jj,times=0;
in>>t;
int counter = 0;
long long tmp,nb;
long long max=0;
for(int k=0;k<t;k++){
	in>>n>>jj;
	max=0;
	out<<"Case #"<<k+1<<":"<<endl;
	for(int i=0;i<n-2;i++){
		max+=(1<<i);
	}
	//cout<<max<<endl;
	for(int j=0;j<=max;j++){
		nb = (1<<(n-1))+(j<<1)+1;
		counter = 0;

		for(int i=2;i<=10;i++){
			tmp = base(nb,i,n);
			if(isprime(tmp,i)){
				break;
			}else
				counter++;
		}

		if(counter==9){

			out<<tobinary(nb)<<" ";
			for(int i=0;i<9;i++){
				out<<ans[i]<<" ";
			}
			out<<endl;
			times++;
			if(times==jj)
				break;
		}
	}



}
in.close();
out.close();
  return 0;
}

