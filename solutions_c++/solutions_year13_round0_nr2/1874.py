#include<iostream>
#include<stdio.h>
#include<vector>
using namespace std;

int main()
{
	int kase=0;
		int first =1;
		cin>>kase;
		while(first<=kase)
		{
			vector< vector<int> >vec;
			vector<vector<int> >copy;
			int N,M;
			cin>>N>>M;
			for(int i=0;i<N;i++)
			{
				vector<int>temp(M);
				vec.push_back(temp);
				copy.push_back(temp);
				for(int j=0;j<M;j++)
				{
					cin>>vec[i][j];
					copy[i][j]=101;
				}
			}

			vector<int>max(M);
			vector<int>rowMax(N);
			
				for(int col=0;col<M;col++)
				{
					for(int row=0;row<N;row++)
					{
					if(vec[row][col]>max[col])
						max[col]=vec[row][col];
					}
			}
			for(int j=0;j<N;j++)
			{
				for(int i=0;i<M;i++)
				{
				if(vec[j][i]>rowMax[j])
					rowMax[j]=vec[j][i];
				}
			}
			for(int j=0;j<M;j++)
			{
				for(int i=0;i<N;i++)
				{
					copy[i][j]=max[j];
				}
			}
			
			for(int j=0;j<N;j++)
			{
				for(int i=0;i<M;i++)
				{
					if(copy[j][i]>rowMax[j])
					copy[j][i]=rowMax[j];
				}
			}
			bool result = false;
			for(int j=0;j<N;j++)
			{
				for(int i=0;i<M;i++)
				{
					if(copy[j][i]!=vec[j][i])
					{
					cout<<"Case #"<<first<<": "<<"NO"<<endl;
					result = true;
					break;
					}
				}
				if(result == true)
				break;
			}
			if(result == false)
			cout<<"Case #"<<first<<": "<<"YES"<<endl;
			first++;
		}
		return 0;
}