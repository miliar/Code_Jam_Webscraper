#include<iostream>
#include<math.h>
using namespace std;

int ispalin(int no)
{
	int th = no/1000;
	int hu = (no%1000)/100;
	int te = (no%100)/10;
	int on = no%10;
//	cout<<th<<hu<<te<<on;
	
	if(th == 0)
		{
			if(hu == 0)
			{
				if(te==0)
				{
					return 1;
				}
				else
					if(te==on)
						return 1;
			}
			else
				if(hu == on)
					return 1;
		}
	else
		if(th==on && hu ==te)
			return 1;
		
	return 0;
}

int nex_palin(int no, int stop)
{
	int i = no;

	while(i <= stop)
		{
		if(ispalin(i))
			return i;
		else
			{i = i+1;}
		}
	return 0;
}

int main()
{
	int T;
	cin>>T;
	int A[T],B[T];
	int cnt[T];
	//cout<<nex_palin(1220,1231);
	
	for(int iter = 0; iter<T; ++iter)
	{
		cin>>A[iter];
		cin>>B[iter];
		cnt[iter] = 0;
		int i = A[iter];
		while(i<=B[iter])
		{
		int pa = nex_palin(i,B[iter]);
		if(pa == 0)
			break;
		float t = sqrt(pa);
		if(!(t - int(t)) && (ispalin(t)))
			++cnt[iter];
		i = pa+1;
		}
		cout<<"Case #"<<iter+1<<": "<<cnt[iter]<<'\n';
	}
}
