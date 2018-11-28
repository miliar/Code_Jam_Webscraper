#include<iostream>
#include<vector>
#include<cmath>
#include<cstdio>
//#define DEBUG
using namespace std;


int ndigits = 17;
vector<long long int> fs;

bool palin(long long int n)
{
	char arr[ndigits];
	int pos = 0;
	while(n) {
		arr[pos] = (n%10)+0x30;
		n/=10;
		pos++;
	}
	arr[pos] = '\0';	
			
	for(int i=0, j=strlen(arr)-1; i<j; i++, j--)
		if(arr[i] != arr[j]) return false;
	
	return true;
}

void computeTable() 
{
	
	long long int n = 10000000;
	for(long long int i=1; i<=n; i++) {
		if(! palin(i)) continue;
		long long int sq = i*i;
		if(palin(sq))
			fs.push_back(sq);
	}
	#ifdef DEBUG
		for(long long int i=0; i<fs.size(); i++)
			cout<<fs[i]<<" ";
		cout<<endl;
	#endif
}

long long int bsearch(long long int n)
{
	long long int left = 0;
	long long int right = fs.size()-1;
	long long int middle;
	#ifdef DEBUG
		cout<<"\t\t searching for "<<n;
	#endif
	while(left <= right) {
		middle = (left+right)/2;
		if(fs[middle] == n) return middle;
		else if(fs[middle] > n) right = middle-1;
		else left = middle+1;
	}
	
	return middle;
}

long long int interval(long long int a, long long int b)
{
	long long int l = bsearch(a);
	long long int r = bsearch(b);	
	#ifdef DEBUG
		cout<<"\tinitial L: "<<l<<"\n\tinitial R:"<<r<<endl;
	#endif
	
	while(fs[l] < a) l++;
	while(fs[r] > b) r--;
	
	#ifdef DEBUG
		cout<<"\tFinal L: "<<l<<"\n\tFinal R:"<<r<<endl;
	#endif
	if(l<=r)
		return r-l+1;
	else
		return 0;
}

int main()
{
	freopen("ip.txt", "r", stdin);
	freopen("op.txt", "w", stdout);
	
	int t;
	cin>>t;
	computeTable();
	for(int tc=1; tc<=t; tc++) {
		long long int a,b;
		cin>>a>>b;
		#ifdef DEBUG
			cout<<"case "<<tc<<endl;
		#endif
		cout<<"Case #"<<tc<<": "<<interval(a,b)<<endl;
	}
	return 0;
}
	


