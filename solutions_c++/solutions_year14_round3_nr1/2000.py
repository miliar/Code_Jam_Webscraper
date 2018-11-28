#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
using namespace std;
long long power[41];

long long Gcd(unsigned long long a, unsigned long long b)
{
    if(b == 0)
        return a;
    return Gcd(b, a % b);
}

void Calc(int casenum, unsigned long long P, unsigned long long Q, ofstream &outfile)
{
	long long gcd = Gcd(Q,P);
	if(gcd!=1)
	{
		Q/=gcd;
		P/=gcd;
	}
	unsigned long long re = Q&(Q-1);
	if(re!=0)
	{
		//cout<<"Case #"<<casenum<<": impossible"<<endl;
		outfile<<"Case #"<<casenum<<": impossible"<<endl;
		return;
	}
	//int a=1,b=40;
	//while(a<=b)
	//{
	//	int mid = (a+b)/2;
	//	long long right = P*power[mid], left = P*power[mid-1];
	//	if(right>=Q && left<Q)
	//	{
	//		cout<<"Case #"<<casenum<<": "<<mid<<endl;
	//		outfile<<"Case #"<<casenum<<": "<<mid<<endl;
	//		break;
	//	}
	//	else if(right < Q)
	//		a=mid+1;
	//	else b=mid-1;
	//}
	for(int i=1;i<=40;i++)
	{
		P*=2;
		if(P>=Q)
		{
			//cout<<"Case #"<<casenum<<": "<<i<<endl;
			outfile<<"Case #"<<casenum<<": "<<i<<endl;
			break;
		}
	}
}
void init()
{
	power[0]=1;
	for(int i=1;i<=40;i++)
		power[i] = power[i-1]*2; 
}
int main()
{
	//init();
	ifstream infile;
	ofstream outfile;
	infile.open("A-small-attempt2.in");
	outfile.open("A-small-attempt2.out");
	int T;
	//cin>>T;
	infile>>T;
	unsigned long long P,Q;
	string str;
	for(int i=0;i<T;i++)
	{
		//cin>>str;
		infile>>str;
		P=atol(str.c_str());
		str = str.substr(str.find('/')+1,str.size()-1);
		Q = atol(str.c_str());
		Calc(i+1,P,Q,outfile);
	}
	infile.close();
	outfile.close();
	return 0;
}