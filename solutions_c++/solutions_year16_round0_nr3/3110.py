#include<bits/stdc++.h>
using namespace std;

long long smallest_divisor(long long num)
{
	int i,lim=sqrt(num);
	
	for(i=2;i<=lim;++i)
	if(num%i == 0)
		return i;
	
	return num;
}

long long rep[11] = {0};

int to_binary(bool arr[],int num)
{
	int n=0;
	while(num)
	{
		arr[n] = num%2;
		n++;
		num /= 2;
	}
	return n;
}

long long rep_value(bool arr[], int n, int base)
{
	int i;
	long long p=1,val=0;
	
	for(i=0;i<n;++i,p*=base)
		val += arr[i]*p;
	
	return val;
}

bool is_jamcoin(bool arr[], int n,long long rep_list[])
{
	if(arr[0] != true || arr[n-1] != true)
		return false;
	
	int i;
	long long rep,div;
	
	for(i=2;i<11;++i)
	{
		rep = rep_value(arr,n,i);
		div = smallest_divisor(rep);
		if(div == rep)
			return false;
		rep_list[i] = div;
	}
	
	return true;
}



int main()
{
	fstream fin,fout;
	fin.open("C-small-attempt2.in",ios::in);
	fout.open("small1-out.txt",ios::out);
	
	int t,q;
	fin>>t;
	for(q=0;q<t;++q)
	{
		fout<<"Case #"<<q+1<<":\n";
		
		int N,J;
		fin>>N>>J;
		
		long long lim = pow(2,N),i,rep_list[11];
		bool arr[N];
		int n,r;
		
		for(i=lim/2; i<lim && J ;++i)
		{
			to_binary(arr,i);
			
			if(is_jamcoin(arr,N,rep_list))
			{
				for(r=N-1;r>=0;--r)
					fout<<arr[r];
				fout<<" ";
	
				for(r=2;r<11;++r)
					fout<<rep_list[r]<<" ";
				fout<<"\n";
				J--;
			}
		}
	}
	
	fout.close();
	fin.close();
	/**/
	return 0;
}
