#include <iostream>

using namespace std;

int match(int *A,int *B,int &var)
{
	int count = 0;
	for(int i=0;i<4;++i)
		for(int j=0;j<4;++j)
		{
			if(A[i]==B[j]){count++; var = A[i];}
		}
	return count;
}

int main()
{
	int T;
	cin>>T;
	for(int i=0;i<T;++i)
	{
		int x,v,*A,*B;
		A = new int(4);
		B = new int(4);
		cin>>x;
		for(int k=1;k<x;++k)
			for(int p=0;p<4;++p) cin>>v;
		for(int p=0;p<4;++p) cin>>A[p];
		for(int k=0;k<=(3-x);++k)
			for(int p=0;p<4;++p) cin>>v;
		cin>>x;
		for(int k=1;k<x;++k)
			for(int p=0;p<4;++p) cin>>v;
		for(int p=0;p<4;++p) cin>>B[p];
		for(int k=0;k<=(3-x);++k)
			for(int p=0;p<4;++p) cin>>v;
		switch(match(A,B,v))
		{
			case 0:cout<<"Case #"<<i+1<<": Volunteer cheated!\n";
				break;
			case 1:cout<<"Case #"<<i+1<<": "<<v<<endl;
				break;
			default:cout<<"Case #"<<i+1<<": Bad magician!\n";
				break;
		}	
	}
}