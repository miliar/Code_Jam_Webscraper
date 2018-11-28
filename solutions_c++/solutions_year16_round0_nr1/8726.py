#include <iostream>
#include <fstream>
using namespace std;

int main() {
	// your code goes here
	ifstream fin("A-large.in");
	ofstream fout("output.txt");
	long long n,T,temp,rem,ans;
	fin>>T;
	for(int t=1;t<=T;t++)
	{
		fin>>n;
		if(n==0)
		{
		fout<<"Case #"<<t<<":"<<" INSOMNIA"<<endl;
		continue;
		}
		int arr[10]={0},count=10,i=1;
		while(count)
		{
			temp=n*i;
			ans=temp;
			while(temp)
			{
				rem=temp%10;
				temp/=10;
				if(arr[rem]==0)
				{
					arr[rem]++;
					count--;
				}
			}
			i++;
		}
		fout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}
