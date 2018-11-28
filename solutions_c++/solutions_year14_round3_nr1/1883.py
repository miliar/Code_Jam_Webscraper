/* name of code*/
#include<iostream>
#include<cstring>
#include<iomanip>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<fstream>
#include<set>
#include<bitset>

#define lol long long
#define ull unsigned long long int

using namespace std;


#define cin fin
#define cout fout


ull gcd(ull a, ull b) {
	if (b == 0) {
		return a;
	} else {
		return gcd(b, a % b);
	}
}

int main()
{
	//ios_base::sync_with_stdio(false);
	int test_case,t=1;
	
	ifstream fin;
	ofstream fout;
	fin.open("A-small-attempt1.in");
	fout.open("asmall.txt");
	
	cin>>test_case;
	while(test_case--)
	{
		char str[200];
		cin>>str;
		char num[20];
		char den[20];
		int j=0,k=0,l=0;
		int len=strlen(str);
		while(str[j]!='/')
		{
			num[k++]=str[j++];
		}
		num[k]='\0';
		j++;
		while(j!=len)
		{
			den[l++]=str[j++];
		}
		den[l]='\0';
		ull n=atoi(num);
		ull d=atoi(den);
		ull x=gcd(n,d);
		n/=x;
		d/=x;
		ull temp=d;
		int tag=0;
		if(n>d) tag=1;
		else
		{
			while(temp>1)
			{
				if(temp%2 != 0)
				{
					tag=1;
					break;
				}
				else
				{
					temp/=2;
				}
			}
		}
		ull w = (d/n);
		ull count=0;
		while(w>1)
		{
			w/=2;
			count++;
		}
		if((d%n) !=0) count++;
		cout<<"Case #"<<t++<<": ";
		if(tag==1) cout<<"impossible"<<"\n";
		else cout<<count<<"\n";
	}
	return 0;
}

