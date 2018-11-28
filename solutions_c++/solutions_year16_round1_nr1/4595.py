#include<iostream>
#include<string>
using namespace std;
int main()
{
	int T;
	cin>>T;
	int temp=0;
	while(temp<T)
	{
		string A;
		string S;
		cin>>A;
		int k=0;
		int b[2000];
		while(k<A.length())
		{
			b[k]=(int)A[k];
			k++;	
		}
		S=S+A[0];
		k=1;
		int z=0;
		while(k<A.length())
		{
			if((int)S[0]>b[k])
			{
				S=S+A[k];
			}
			else
			{
				S=A[k]+S;
			}
			k++;	
		}
		cout<<"Case #"<<(temp+1)<<": ";
		for(int i=0;i<S.length();i++)
		{
			cout<<S[i];
		}
		cout<<endl;
		temp++;
	}
	return 0;
}