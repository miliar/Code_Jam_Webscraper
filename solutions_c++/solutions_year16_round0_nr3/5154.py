#include <bits/stdc++.h>
using namespace std;
long long arr[11][33];
long long divs[11];
long long isprime(long long num)
{
	for (long long  i=2;i*i<=num;i++)
		if (num%i==0) { return i; }
	return -1;
}
long long base(int num,string s)
{
	long long sum=0;
	for (int i=0;i<(int)s.size();i++)
	{
		sum+=(s[i]-'0')*arr[num][i];
	}
	return sum;
}
int main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("ou.txt");
	int t;
	fin>>t;
arr[2][0]=1; arr[3][0]=1; arr[4][0]=1; arr[5][0]=1; arr[6][0]=1; arr[7][0]=1; arr[8][0]=1; arr[9][0]=1; arr[10][0]=1;
	long long p2=1; long long p3=1; long long p4=1; long long p5=1; long long p6=1; long long p7=1; long long p8=1; long long p9=1; long long p10=1;
	for (int i=1;i<33;i++)
	{
		p2*=2; p3*=3; p4*=4; p5*=5; p6*=6; p7*=7; p8*=8; p9*=9; p10*=10;
arr[2][i]=p2; arr[3][i]=p3; arr[4][i]=p4; arr[5][i]=p5; arr[6][i]=p6; arr[7][i]=p7; arr[8][i]=p8; arr[9][i]=p9; arr[10][i]=p10;
	}
for (int T=1;T<=t;T++)
{
	int counter=0;
	int n,j;
	fin>>n>>j;
	fout<<"Case #"<<T<<":"<<endl;
	for (long long i=arr[2][n-1];i<arr[2][n];i++)
	{
		if (i%2==0) continue;
		long long div2=isprime(i);
		if( div2==-1) continue;
		divs[2]=div2;
long long x=i;
string s="";
while (x)
{
	if (x%2==0) s+='0';
	else s+='1';
	x/=2;
}
bool fnd=true;
for (int k=3;k<=10;k++)
{
	long long sum=base(k,s);
long long xx=isprime(sum);
if (xx==-1) {fnd=false; break;}
else divs[k]=xx;
}
if (fnd) {counter++; reverse(s.begin(),s.end()); fout<<s<<" "; for (int k=2;k<11;k++) fout<<divs[k]<<" "; fout<<endl;}
if (counter==j) break;
}
}
}
