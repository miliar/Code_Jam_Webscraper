#include <iostream>
#include <fstream>
#include<bits/stdc++.h>
using namespace std;

#define ll long long int

int main()
{

	ifstream myfile("input1l.in");
	ofstream outfile("outputl.txt");
	ll t,n;
	int tno=1;
	//cin>>t;
	myfile>>t;

	while(t--)
	{
		int j=1,i,array[10]={0};
		//cin>>n;
		myfile>>n;
		int flag=0;
		int mark=0;
		int ans=0;


		if(n==0)
		{
			//cout<<"Case #"<<tno<<":"<<" "<<"INSOMNIA"<<endl;tno++;
			outfile<<"Case #"<<tno<<":"<<" "<<"INSOMNIA"<<endl;tno++;
		}
		else
		{
			for(i=n;flag==0;i=j*n)
			{
				ans=i;
				while(i>0)
				{
					mark=i%10;
					array[mark]++;
					i=i/10;
				}
				j++;

				for(int k=0;k<10;k++)
				{
					if(array[k]==0){
					flag=0; break;
					}
					else
					flag=1;
				}


			}

			//cout<<"Case #"<<tno<<":"<<" "<<ans<<endl;
			outfile<<"Case #"<<tno<<":"<<" "<<ans<<endl;
			tno++;
		}

	}

	return 0;

}
