#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#define cin fin
#define cout fout
using namespace std;

int calc(int a,int b,int k)
{
	int sum=0;
	if(a>b)
		swap(a,b);
	k=min(k,a);

	for(int i=0;i<a;i++)
		for(int j=0;j<b;j++)
			if((i&j)<k)
				sum++;
	return sum;


}

int main()
{
	fstream fin("b.in",fstream::in);
	fstream fout("b.out",fstream::out);
	
	int T;
	cin>>T;
	for(int t=0;t<T;t++)
	{
		int A,B,K;
		cin>>A>>B>>K;
		cout<<"Case #"<<t+1<<": "<<calc(A,B,K)<<endl;

	}
	fout.close();
	return 0;
}