#include<bits/stdc++.h>
using namespace std;
int main(){
    ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("A-large.out");
	int t,k,i;
	long long int n,m;
	fin>>t;
	for(i=1;i<=t;i++)
	{
		set<int> myset;
		fin>>n;
        if(n==0)
        {
            fout<<"Case #"<<i<<": INSOMNIA"<<endl;
            continue;
        }
		m=n;
		k=1;
		while(myset.size()!=10)
		{
			m*=k;
			while(m>0)
			{
				myset.insert(m%10);
				m/=10;
			}
			m=n;
			k++;
		}
		fout<<"Case #"<<i<<": "<<m*(k-1)<<endl;
	}
	return 0;
}
