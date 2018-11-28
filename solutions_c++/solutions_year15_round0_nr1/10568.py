#include <iostream>
using namespace std;

int main() 
{
	int op[1001];
	int i, smax, k, index=0, ppl, no;
	int t;
	string seq;
	cin>>t;
	for(k=0;k<t;k++)
	{	
		no=0;
		ppl=0;
		cin>>smax;
		cin>>seq;
		for(i=0;i<smax+1;i++)
		{
			if(((seq[i]-'0')!=0)&&(ppl>=i))
					ppl+=(seq[i]-'0');
			else if(((seq[i]-'0')!=0)&&(ppl<i))
				{
					no+=(i-ppl);
					ppl=ppl+no+(seq[i]-'0');
				}	
		}
		op[index++]=no;
	}
	for(i=0;i<t;i++)
		cout<<"Case #"<<i+1<<": "<<op[i]<<"\n";
	return 0;
}