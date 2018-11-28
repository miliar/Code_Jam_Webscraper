#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <stdlib.h>
using namespace std;
int gcd(int n,int m){return m==0?n:gcd(m,n%m);}
bool poss(int a, double n)
{
	if (n == 1)
	{
		return true;
	}
	else if((a=0) || (n<1))
	{
		return false;
	}
	else
	{
		return poss(a-1,n/2);
	}
}
int main(){
	int ntest;
	cin>>ntest;
	for(int test=0; test<ntest; test++){
		long long p, q, gen, g;
		gen=0;
		string temp;
		cin>>temp;
		int pos=temp.find_last_of("/");
		p = atoi((temp.substr(0, pos)).c_str());
		q = atoi((temp.substr(pos+1)).c_str());
		//cout<<p<<endl<<q;
		cout<<"Case #"<<test+1<<": ";
		g = gcd(p,q);
		p=p/g;
		q=q/g;
		if (poss(40,q)){
			while(true)
			{
				while(2*p<q)
				{
					gen++;
					q=q/2;
				}
				if (poss(40-gen,q))
				{
					cout<<gen+1;
					break;
				}
				else
				{
					cout<<"impossible";
					break;
				}
			}
		}
		else{
			cout<<"impossible";
		}
		//cout<<(long long)pow(2,40)%31488;
		cout<<endl;
	}
}