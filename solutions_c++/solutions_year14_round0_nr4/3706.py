#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	int t,n;
	float kem[1000],nem[1000];
	in>>t;
	for(int k=0;k<t;k++)
	{
		int f1[1000]={0},f2[1000]={0},cnt=0,lim=0;
		int s1=0,s2=0;
		in>>n;
     	for(int i=0;i<n;i++)
	    in>>nem[i];
	    for(int i=0;i<n;i++)
	    in>>kem[i];
	    sort(kem,kem+n);
	    sort(nem,nem+n);
	    for(int i=0;i<n;i++)
	    {
			for(int j=lim;j<n;j++)
			{
				if(kem[i]>=nem[j])
				{
					lim=j+1;
					cnt++;
					break;
				}
			}
		}
		s1=n-cnt;
		cnt=0;
		int i=n-1,j=n-1;
		while(i>=0 && j>=cnt)
		{
			if(kem[i]>=nem[j])
			{
				cnt++;
				i--;
			}
			else
			{
				j--;
				i--;
				s2++;
			}
		}
		out<<"Case #"<<k+1<<": "<<s2<<" "<<s1<<endl;
	}
	return 0;
}










