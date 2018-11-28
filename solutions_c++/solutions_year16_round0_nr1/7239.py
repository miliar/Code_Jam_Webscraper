#include "stdafx.h"

#include <iostream>

using namespace std;

int main(int argc, char * argv[])
{


	freopen("sample.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	
	cin>>T;
	for(int testcase =1;testcase<=T;testcase++)
	{
		int N;

		cin>>N;
		cout<<"Case #"<<testcase<<": ";
		bool found =0;
		int ctr=0;
		int visited[10];

		for(int i=0;i<10;i++)
		{
			visited[i]=0;
		}
		int itr=1;
		while(1)
		{
		    int temp =itr*N;
			itr++;
			if(found )
			{
				break;
			}
			if(N==0  )
			{
				cout<<"INSOMNIA"<<endl;
				break;
			}
			
			
			int Answer =temp;
			while(temp>0)
			{
				int R = temp%10;
				
			    temp = temp/10;

				if(visited[R]!=1)
				{
					visited[R] =1;
					ctr++;
					if(ctr>9)
					{
						cout<<Answer<<endl;
						found=1;
						break;
					}
				}
			}
			
			
		}
		
	}
 return 0;
}