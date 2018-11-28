#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("../../output.txt");
ifstream fin("../../input.txt");


long long choose(long long a, long long b)
{
	if(a<b)
		return 0;
	if(b==0)
		return 1;
	return (a*choose(a-1,b-1))/b;
}

int count(int m, int n)
{
	int ret=0;
	if(n==0)
	{
		ret= 1 + choose(m-1,0) + choose(m-1,1) + choose(m-1,2) + choose(m-1,3);
	}
	else {
		ret= choose(m-1,0) + choose(m-1,1) + 2 * (1 + choose(m-1,0) + choose(m-1,1) + choose(m-1,2) + choose(m-1,3));
	}
	//cout << m << " " << n << " " << ret << endl;
	return ret;
}

int target[101];
int palin[101];
int product[101];

int runtest(int palinlen, int totlen, bool include)
{
	memset(product,0,sizeof(product));
	
	for(int i=0; i<palinlen; i++)
	{
		for(int j=0; j<palinlen; j++)
		{
			product[i+j]+=palin[i]*palin[j];
		}
	}
	
	for(int i=totlen-1; i>=0; i--)
	{
		if(target[i] > product[i])
			return 1;
		else if(target[i]<product[i])
			return 0;
	}
	
	if(include)
		return 1;
	else {
		return 0;
	}
}





int generateall(int totlen, int m, int togen, int n, int first, int mid, bool include)
{
	palin[0] = palin[2*m+n-1]= first;
	if(n==1)
	{
		palin[m]=mid;
	}
	
	int i,j,k;
	
	int ret = 0;
	
	ret+=runtest(2*m+n,totlen,include);
	
	if(togen==0)
		return ret;
	
	for(i=1; i<m; i++)
	{
		palin[i]=1;
		ret+=runtest(2*m+n, totlen, include);
		palin[i]=0;
	}
	
	if(togen==1)
		return ret;
	
	for(i=1; i<m; i++)
	{
		for(j=i+1; j<m; j++)
		{
			palin[i]=palin[j]=1;
			ret+=runtest(2*m+n, totlen, include);
			palin[i]=palin[j]=0;
		}
	}
	
	if(togen==2)
		return ret;
	
	for(i=1; i<m; i++)
	{
		for(j=i+1; j<m; j++)
		{
			for(k=j+1; k<m; k++)
			{
				palin[i]=palin[j]=palin[k]=1;
				ret+=runtest(2*m+n, totlen, include);
				palin[i]=palin[j]=palin[k]=0;
				
			}
		}
	}
	return ret;
}


int count(int m, int n,string a, bool include)
{
	int totlen = a.size();
	
	int i,j,k;
	
	for(i=a.size()-1; i>=0; i--)
	{
		target[i] = a[a.size()-1-i]-'0';
	}
	
	int ret = 0;
	
	if(n==0)
	{
		ret+=generateall(totlen, m, 0, n, 2, 0, include);
		ret+=generateall(totlen, m, 3, n, 1, 0, include);
	}
	else {
		ret+=generateall(totlen, m, 1, n, 1, 2, include);
		ret+=generateall(totlen, m, 0, n, 2, 1, include);
		ret+=generateall(totlen, m, 3, n, 1, 1, include);
		ret+=generateall(totlen, m, 0, n, 2, 0, include);
		ret+=generateall(totlen, m, 3, n, 1, 0, include);
	}
	//cout << m << " " << n << " " << ret << endl;
	return ret;
}


int lis[10];

bool ispalin(int x)
{
	int n = 0;
	
	while(x>0)
	{
		lis[n]=x%10;
		x/=10;
		n++;
	}
	
	for(int i=0; i<n; i++)
	{
		if(lis[i]!=lis[n-i-1])
			return false;
	}
	return true;
}

int brute(string a, bool include)
{
	int tgt = 0;
	
	for(int i=0; i<a.size(); i++)
	{
		tgt*=10;
		tgt+=(a[i]-'0');
	}
	
	int ret = 0;
	
	for(int i=1; ; i++)
	{
		if(!ispalin(i))
			continue;
		//cout << i << endl;
		int j = i*i;
		
		if(ispalin(j))
		{
			if(j < tgt || (j==tgt && include))
			{
				//cout << i << " " << j << endl;
				ret++;
			}
		}
		
		if(j>tgt)
			break;
	}
	return ret;
}


int countleq(string a, bool include)
{
	int ret = 0;
		
	if(a.size()>1)
		ret+=3;
	else if(include)
	{
		int val = a[0]-'0';
		
		if(val>=9)
			ret+=3;
		else if(val>=4)
			ret+=2;
		else if(val>=1)
			ret+=1;
	}
	else {
		int val = a[0]-'0';
		
		if(val>9)
			ret+=3;
		else if(val>4)
			ret+=2;
		else if(val>1)
			ret+=1;
	}

	
	for(int m=1; 4*m-1<=a.size(); m++)
	{
		int n;
		
		
		n = 0;
		
		int len;
		
		len = 4*m + 2*n - 1;
		
		if(len < a.size())
		{
			ret += count(m,n);
		}
		else if(len==a.size())
		{
			ret += count(m,n,a,include);
		}
		
		n=1;
		
		len = 4*m + 2*n - 1;
		
		if(len < a.size())
		{
			ret += count(m,n);
		}
		else if(len==a.size())
		{
			ret += count(m,n,a,include);
		}
	}
	
	cout << a << " " << include << " " << ret << endl;
	//cout << brute(a,include) << endl;
	
	return ret;
	
}



int main(void)
{
	int ttt;
	fin >> ttt;
	int ct = 0;
	string s;
	
	cout.precision(9);
	fout.precision(9);
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		int i,j,k;
		
		
		string a;
		string b;
		
		fin >> a >> b;
		
		int ans = countleq(b,true)-countleq(a,false);
		
		
		
		cout << "Case #" << ct << ": " << ans << endl;
		fout << "Case #" << ct << ": " << ans << endl;
		
		
		
		
		
		
		
		
		
		
		
	}
	
	
	return 0;
}

