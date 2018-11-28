#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;
int a1[4];
int a2[4];
int main()
{
	//freopen("in.txt","r" , stdin);
	//freopen("out.txt","w" , stdout);
	int T =0 ;
	cin>>T;
	int n1 , n2;
	int temp;
	for(int iter =1 ; iter <= T;++iter)
	{
		cin>>n1;
		for(int i=0 ; i< 4;++i)
		{
			for(int j=0 ; j< 4;++j)
			{
				cin>>temp;
				if(i+1==n1)
				{
					a1[j] = temp;
				}
			}
		}



		cin>>n2;
		for(int i=0 ; i< 4;++i)
		{
			for(int j=0 ; j< 4;++j)
			{
				cin>>temp;
				if(i+1==n2)
				{
					a2[j] = temp;
				}
			}
		}



		//
		int find_ =0;
		int num =0;
		for(int i=0 ; i<4;++i)
		{
			for(int j=0;j<4;++j)
				if(a1[i]== a2[j])
				{
					++find_;
					num = a1[i];
				}
		}
		
		cout<<"Case #"<<iter<<": ";
		if(find_==1)
		{
			cout<<num<<endl;
		}
		else if(find_==0)
		{
			cout<<"Volunteer cheated!\n";
		}
		else
		{
			cout<<"Bad magician!\n";
		}

	}


	return 0;
}