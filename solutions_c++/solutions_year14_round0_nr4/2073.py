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

#define cin fin
#define cout fout

using namespace std;


int main()
{
	//ios_base::sync_with_stdio(false);
	ifstream fin;
	ofstream fout;
	fin.open("D-large.in");
	fout.open("2.txt");
	int t=1;
	int test_case;
	cin>>test_case;
	while(test_case--)
	{
		int n;
		cin>>n;
		double a[10002];
		double b[10002];
		for(int i=0;i<n;i++)
		cin>>a[i];
		for(int i=0;i<n;i++)
		cin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		int i=0,j=0;
		int count1=0;
		while(i<n && j<n)
		{
			if(a[i] > b[j])
			{
				count1++;
				j++;
				i++;
			}
			else i++;
		}	
		int k=0,l=0;
		int count2=0;
		while(k<n && l<n)
		{
			if(b[k] > a[l])
			{
				count2++;
				l++;
				k++;
			}
			else k++;
		}
		count2=n-count2;
		cout<<"Case #"<<t<<": "<<count1<<" "<<count2<<"\n";
		t++;
	}
	return 0;
}
