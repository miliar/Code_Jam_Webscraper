
//main includes
#include<iostream>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<cmath>


//other includes
#include<algorithm>
#include<climits>
#include<vector>
#include<queue>
#include<stack>
#include<bitset>
#include<set>
#include<deque>
#include<cstdlib>
#include<map>
#include <utility>

#define re



using namespace std;

#define FOR(a,b)        for(__typeof(b) i=(a);i<(b);i++)

int t,aMote,n;
int *motes;
void swap(int *a,int i , int j)
{
int temp = a[i];
a[i]=a[j];
a[j]=temp;
}

void qsort(int *a,int left,int right)
{
int i, last;

if (left >= right) 
return;
swap(a,left, (left + right)/2); 
last = left;
for (i = left + 1; i <= right; i++) 
if (a[i] < a[left])
swap(a, ++last, i);
swap(a, left, last);

qsort(a, left, last-1);
qsort(a, last+1, right);
}


void preprocess()
{
	cout<<endl<<"===INPUT===="<<endl;
	cout<<aMote<<endl;
	for(int i=0;i<n;i++)
		cout<<motes[i]<<"  ";
	cout<<endl;

}
int min(int a, int b)
{
	return a>b?b:a;
}
int solve(int val , int i , int count)
{
/*	int temp = aMote;
	int operation_count = 0;
	for(int i=0;i<n;)
	{
		while(i!=n && temp>motes[i])
		{
			temp += motes[i];
			i++;
		}
		if(i==n)
			break;
		if(temp+temp-1>motes[i])
		{
			temp += temp-1;
			operation_count++;
		}
		else
		{
			i++;
			operation_count++;
		}
	}
	return operation_count;*/

	if(i==n)
		return count;
	while(i!=n && val>motes[i])
		{
			val += motes[i];
			i++;
		}
		if(i==n)
			return count;
		if(val-1 <= 0 )
			return solve(val,i+1,count+1);
	return min(solve(val+val-1,i,count+1),solve(val,i+1,count+1));

}


int main(){
#ifdef re
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
freopen("log.txt","w",stderr);
#endif
cin>>t;
for(int i=1;i<=t;i++)
{

	cin>>aMote>>n;
motes = new int[n];
for(int j=0;j<n;j++){
cin>>motes[j];
}

qsort(motes,0,n-1);
//preprocess();
cout<<"Case #"<<i<<": "<<solve(aMote,0,0)<<endl;
}
//cout<<"hello world";

#ifdef re
//printf("\n  Time Taken  %.31f sec\n",(double)clock()/(CLOCKS_PER_SEC));

#endif
return 0;
}

