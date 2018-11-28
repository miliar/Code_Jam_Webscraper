#include <fstream>
#include <iostream>
#include <string>
#include <math.h>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stdio.h>
#include <stack>
#include <algorithm>
#include <list>
#include <ctime>
#include <memory.h>
#include <assert.h>
#include <stdlib.h>
#include <cmath>

#define eps 1e-9
#define bs 1000000007
#define bsize 512
#define loop(i,start,end) for(int i=start;i<end;i++)
#define MOD 1000000007
#define modulus 1
using namespace std;
#define ll long long


int main()
{
	long long int t;
	long long int n,*sen,*sen2,i,j,max=0,k;
	cin>>t;
	for(i=0;i<t;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		max=0;
		cin>>n;
		sen=new long long int[n];
		sen2=new long long int[n];
		long long int maxsize=0;
		for(j=0;j<n;j++)
		{
			cin>>sen[j];
			maxsize+=sen[j];
			if(sen[j]>max)
			{
				max=sen[j];
			}
			sen2[j]=sen[j];
		}
		sort(sen2,sen2+n);
		
		while(maxsize>0)
		{
			max=0;
			for(j=0;j<n;j++)
			{
				if(sen[j]>max)
				{
					max=sen[j];
				}
			}
			int flag=0;
			long long int max2=0,sum=0;
			for(j=0;j<n;j++)
			{
				if(sen[j]==max && sen[j]>1)
				{
					sen[j]-=2;
					for(k=0;k<n;k++)
					{
						if(sen[k]>max2)
						{
							max2=sen[k];
						}
						sum+=sen[k];
					}
					if(max2>(sum/2) && max2<=(sum+1)/2)
					{
						sen[j]+=1;
						char ch=j+65;
					//	cout<<"Place1"<<endl;
						cout<<ch<<" ";
						maxsize--;
					}
					else if(max2>(sum+1)/2)
					{
						sen[j]+=1;
						char ch=j+65;
					//	cout<<"Place1"<<endl;
						cout<<ch;
						maxsize-=2;
						for(k=0;k<n;k++)
						{
							if(max2==sen[k])
							{
								sen[k]--;
								char ch=k+65;
								cout<<ch<<" ";
								break;
							}
						}
					}
					else
					{
						char ch=j+65;
						//cout<<"Place2"<<endl;
						cout<<ch<<ch<<" ";
						maxsize-=2;
					}
					break;
				}
				else if(sen[j]==max)
				{
					sen[j]-=1;
					char ch=j+65;
					//cout<<"Place4"<<endl;
					cout<<ch;
					max2=0;
					sum=0;
					int flag=0;
					for(k=0;k<n;k++)
					{
						if(sen[k]>max2)
						{
							max2=sen[k];
						}
						sum+=sen[k];
					}
					for(k=0;k<n;k++)
					{
						if(sen[k]==max2 && max2>0)
						{
							sen[k]--;
							
							long long int max3=0;
							for(long long int h=0;h<n;h++)
							{
								if(max3<sen[h])
								{
									max3=sen[h];
								}
							}
							//cout<<"Max3! "<<max3<<" Sum ! "<<sum<<endl;
							if(max3>(sum-1)/2)
							{
								sen[k]++;
								
								//cout<<"Hello!"<<endl;
								break;
							}
							char ch=k+65;
						//	cout<<"Place3"<<endl;
							cout<<ch<<" ";
							flag=1;
							break;
						
						}
					}
					if(flag==0)
					{
						cout<<" ";
						maxsize--;
						break;
					}
					
					maxsize-=2;
					break;
					
				}
			}
		}
		cout<<endl;
	}	

	return 0;
}

