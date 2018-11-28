#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

int is_palindrome(unsigned long long n)
{
	unsigned long long t=n,rev=0;
	while(t>0) {
		rev=(rev*10)+(t%10);
		t=t/10;
	}
	if(rev==n) return 1;
	else return 0;
}

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("C-large-1.in");
	fout.open("C-large-1.out");
	int t,fair_count,ans_count;
	unsigned long long a,b,start,end,ans[100];
	
	ans_count=0;
	for(unsigned long long i=1;i<=10000000;i++) {
		if(!is_palindrome(i)) continue;
		if(!is_palindrome(i*i)) continue;
		ans[ans_count]=i;
		ans_count++;
	}
	
	fin>>t;
	for(int count=1;count<=t;count++) {
		fin>>a>>b;
		start=sqrt(a);
		end=sqrt(b);
		if((start*start)<a) start++;
		fair_count=0;
		for(int i=0;i<ans_count;i++) {
			if((ans[i]>=start) && (ans[i]<=end)) fair_count++;
		}
		fout<<"Case #"<<count<<": "<<fair_count<<"\n";
	}
	
	return 0;
}
