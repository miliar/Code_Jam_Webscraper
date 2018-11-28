#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>


using namespace std;

int ctable[4][4]={{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};
char s[10001];

void test()
{
	

	long long l,x;
	register long long i,N,r=0;
	
	cin>>l>>x;
	cin>>s;

	N=l*x;
		
	r=ctable[0][s[0]-'h'];
	for(i=1;i<N && r!=2;i++)
	{
		r=((r<0)?-1:1)*ctable[labs(r)-1][s[i%l]-'h'];
	}
		
	if(r==2)
	{
		r=ctable[0][s[i%l]-'h'];
			
		for(i=i+1;i<N && r!=3;i++)
		{
			r=((r<0)?-1:1) * ctable[labs(r)-1][s[i%l]-'h'];
		}

		if(r==3)
		{
			r=ctable[0][s[i%l]-'h'];
			for(i=i+1;i<N;i++)
			{
				r=((r<0)?-1:1) * ctable[labs(r)-1][s[i%l]-'h'];
			}
			
			if(r==4)
			{
				cout<<"YES";
				return ;
			}
		}
	}

	cout<<"NO";
}




int main()
{
	long long T,i;
	cin>>T;
	for(i=1;i<=T;i++)
	{
		cout<<"Case #"<<i<<": ";
		test();
		cout<<"\n";
	}
	return 0;
}




