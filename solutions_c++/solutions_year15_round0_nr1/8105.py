#include <iostream>
#include<stdio.h>
using namespace std;
int main() {
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,stnd,ppl,smax,k=1;
	cin>>t;
	while(t--)
	{
		stnd=0;
		ppl=0;
		cin>>smax;
		char *a;
		int *b;
		a = new char[smax+1];
		b = new int[smax+1];
		cin>>a;
		for(int i=0;i<smax+1;i++)
		{
			b[i] = (int)a[i] - 48;
		}
	
		stnd=b[0];
		for(int j=1;j<smax+1;j++)
		{
			if(stnd>=j)
			{
				stnd = stnd + b[j];
			}
			else if(stnd<j && b[j]!=0)
			{
				ppl = ppl + j - stnd;
				stnd = j + b[j];
			}
		}
		
		printf("Case #%d: %d",k,ppl);
		cout<<endl;
		k++;
	}
	return 0;
}
