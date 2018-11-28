#include <iostream>

using namespace std;

#define max 101

int main()
{
	int arr[max][max],arz[max][max],com[max],com1[max],equls[max],all[max];
	int test,a,b,c,sel,temp,equl=0;

	cin>>test;

	for(a=1;a<=test;a++)
	{
		cin>>sel;
		for(b=1;b<=4;b++)
		{
			for(c=1;c<=4;c++)
			{
				cin>>arr[b][c];
			}
			if(b==sel)
			{
				for(c=1;c<=4;c++)
				{
					temp=arr[b][c];
					com[c]=temp;
				}
			}
		}
		cin>>sel;
		for(b=1;b<=4;b++)
		{
			for(c=1;c<=4;c++)
			{
				cin>>arz[b][c];
			}
			if(b==sel)
			{
				for(c=1;c<=4;c++)
				{
					temp=arz[b][c];
					com1[c]=temp;
				}
			}
		}
		for(b=1;b<=4;b++)
		{
			for(c=1;c<=4;c++)
			{
			if(com[b]==com1[c])
			{
				temp=com[b];
				equl++;
				equls[a]=temp;
			}
			}
		}
		all[a]=equl;
		equl=0;
	}

	
	for(a=1;a<=test;a++)
	{
		if(all[a]>1)
			cout<<"Case #"<<a<<": Bad magician!"<<endl;
		else if(all[a]==0)
			cout<<"Case #"<<a<<": Volunteer cheated!"<<endl;
		else
			cout<<"Case #"<<a<<":"<<" "<<equls[a]<<endl;
	}
}