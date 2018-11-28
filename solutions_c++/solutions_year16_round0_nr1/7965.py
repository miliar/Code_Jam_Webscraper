#include<bits/stdc++.h>
using namespace std;
ifstream fin ("in.txt");
ofstream fout ("out.txt");

bool check(long long int arr[])
{
	for(long long int i=0;i<10;i++)
		if(arr[i]==0) return false;
	
	return true;
}

bool get_int(long long int arr[], long long int a)
{
	while(a!=0)
	{
		arr[a%10]++;
		a/=10;
	}
	if(check(arr)) return true;
	return false;
}

int main()
{
	long long int t;
	fin >> t;
	for(long long int g=1;g<=t;g++)
	{
		long long int x;
		fin >> x;
		long long int arr[10];
		for(long long int i=0;i<10;i++) arr[i]=0;
		long long int b=x;
		while(!get_int(arr, x) && x!=0 && pow(2,63)-1-x>=b) x+=b;
		if(x==0 || pow(2,63)-1-x<b) fout << "Case #" << g << ": " << "INSOMNIA\n";
		else fout << "Case #" << g << ": " << x << endl;
	}
	return 0;
}
		
