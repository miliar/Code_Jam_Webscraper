#include<bits/stdc++.h>
using namespace std;
long long int decode(string str,int l,int b)
{
	long long int ans=0;
	for(int i=l-1;i>=0;i--) ans+=(str[i]-'0')*pow(b,l-i-1);
	return ans;
}
string decodetostr(int i)
{
	string str;
	while(i>0)
	{
		int x=i%2;
		if(x==1) str+='1';
		else str+='0';
		i/=2;
	}
	return str;
}
long long int nontrivial(long long int x)
{
	for(long long int i=2;i<=sqrt(x);i++) if(x%i==0) return i;
	return 0;
}
int main()
{
	ifstream file1("C-small-attempt0.in");
	ofstream file2("file32.txt");
	int t;
	file1>>t;
	int n,j;
	file1>>n>>j;
	file2<<"Case #1:\n";
	long long int exp=pow(2,n-1);
	int numofans=0;
	for(long long int i=1+exp;i<=2*exp-1,numofans<j;i+=2) 
	{
		int done=1;
		string str=decodetostr(i);
		reverse(str.begin(),str.end());
		for(int b=2;b<=10;b++)
		{
			long long int ans=decode(str,n,b);
			if(!nontrivial(ans)) {done=0;break;}
		}
		if(done)
		{
			numofans++;
			file2<<str<<" ";
			for(int b=2;b<=10;b++)
			{
				long long int ans=decode(str,n,b);
				file2<<nontrivial(ans)<<" ";
			}
			file2<<endl;
		}
	}
}
