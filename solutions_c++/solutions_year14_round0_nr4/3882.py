#include<iostream>
using namespace std;

int main()
{
	int t,n;
	double bNaomi[1020];
	double bKen[1020];
	int bKendone[1020];
	double temp;
	int dWarNless, dWarKmore;
	int dWarPts, warPts;
	int KenTop,KenBottom,candidate;
	int dNaomiTop,dNaomiBottom,dKenTop,dKenBottom;
	cin>>t;
	for(int cases=1;cases<=t;cases++)
	{
		cin>>n;
		for(int i=0;i<n;i++)
			cin>>bNaomi[i];
		
		for(int i=0;i<n;i++)
			cin>>bKen[i];
			
		for(int i=0;i<n;i++)
			bKendone[i] = 0;
			
		dWarNless = 0;	
		for(int i=0;i<n;i++)
			for(int j=i+1;j<n;j++)
			{
				if(bNaomi[j] < bNaomi[i])
				{
					temp = bNaomi[j];
					bNaomi[j] = bNaomi[i];
					bNaomi[i] = temp;
				}
			}
			
		for(int i=0;i<n;i++)
			for(int j=i+1;j<n;j++)
			{
				if(bKen[j] < bKen[i])
				{
					temp = bKen[j];
					bKen[j] = bKen[i];
					bKen[i] = temp;
				}
			}	
		
		dWarPts = 0;
		dNaomiTop = dKenTop = n-1;
		dNaomiBottom = dKenBottom = 0;
		
		for(int i=0;i<n;i++)
		{
			if(bNaomi[dNaomiTop] > bKen[dKenTop])
			{
				dWarPts++;
				dNaomiTop --;
			}
			
			dKenTop --;
		}
		
		
		KenTop = n-1;
		KenBottom = 0;
		warPts = 0;
		
		for(int i=n-1;i>=0;i--)
		{
			if(bNaomi[i] > bKen[KenTop])
			{
				warPts ++;
				bKendone[KenBottom] = 1;
				while(bKendone[KenBottom] == 1)
					KenBottom ++;
			}
			else
			{
				for(int j = KenTop;j>=KenBottom;j--)
				{
					if(bKendone[j]==0 && bKen[j] > bNaomi[i])
					{
						candidate = j;
					}
				}
				
				bKendone[candidate] = 1;
				if(candidate == KenTop)
				{
					while(bKendone[KenTop] == 1)
						KenTop--;
				}
				else if(candidate == KenBottom)
				{
					while(bKendone[KenBottom] == 1)
						KenBottom ++;
				}
			}	
		}
		
		cout<<"Case #"<<cases<<": "<<dWarPts<<" "<<warPts<<endl;
	}
}
