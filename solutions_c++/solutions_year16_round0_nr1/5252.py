/*
 * a.cpp
 *
 *  Created on: Mar 23, 2016
 *      Author: kathrine
 */
#include <iostream>
#include<set>
#include<vector>
#include<cmath>
#include<iterator>
#include <fstream>
using namespace std;

int main()
{
	ifstream in;
	in.open("A-large.in");
	ofstream out;
	out.open("A-small.out");
long long t,n;
in>>t;
bool a[10];
long long c=0, tmp=1,tmp2;

for(int k=0;k<t;k++){
	in>>n;
	out<<"Case #"<<k+1<<": ";
	for(int i=0;i<10;i++)
		a[i]=false;
	c=0;
	tmp = 1;
	if(n==0){
		out<<"INSOMNIA"<<endl;

	}else{
	while(c<10){
		tmp2 = (tmp++)*n;
		while(tmp2>0){
			if(!a[tmp2%10]){
				a[tmp2%10]=true;
				c++;
			}
			tmp2/=10;
		}

	}
	out<<((tmp-1)*n)<<endl;
	}

}
in.close();
out.close();
  return 0;
}


