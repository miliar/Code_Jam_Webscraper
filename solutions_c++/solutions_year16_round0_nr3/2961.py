#include<iostream>
#include<cstdio>
#include<vector>
#include<cmath>
using namespace std;
bool check[1000010];
std::vector<long long int> v;
void seive()
{
	int n=1000000;
	check[0] = check[1] = 1;
	for (int p=2; p*p<=n; p++)
    {
        
        if (check[p] == false)
        {
            
            for (int i=p * p; i<=n; i+=p)
            {
                check[i] = true;
            }
        }
    }
} 
void facto()
{
	for(int i=2;i<=100000;i++)
	{
		if(!check[i])
		v.push_back(i);
	}
}
int main()
{
	seive();
	facto();
	int test; 
	/*for(int i=0;i<v.size();i++)
	{
		cout<<v[i]<<" ";
	}*/
		cin>>test;
	while(test--)
	{
		int n,j;
		long long int i;
		cin>>n>>j;
		int cnt=0;
		cout<<"Case #1"<<":\n";
		for(i= (1<<(n-1)) ; i< (1<<n) && cnt<j ; i++)
		{
			int a[18]={0};int k=0;long long int temp;
			long long int b[12]={0};b[2]=i;
			temp=i;
			if(i%2==1 && check[i])
			{

				while(temp!=0)
				{
					int r=temp%2;
					a[k++]=r;
					temp/=2;
				}

				for(int g=3;g<=10;g++)
				{
					for(int y=0;y<k;y++)
					b[g]=b[g]+((long long)pow(g,y))*a[y];
				}
			
				bool flag=1;
				
				//if(flag)
				//{
					//cnt++;

					
					/*for(int h=k-1;h>=0;h--)
					{
						cout<<a[h];
					}
					cout<<" ";*/
					int v2[12]={0};
					for(int o=2;o<=10;o++)
					{
						int e=0;
						while(e < v.size())
						{
							if(b[o]%v[e]==0)
							{
								v2[o]=v[e];
								break;
							}
							e++;
						}
					}
					for (int w = 2; w < 11; ++w)
					{
						if(v2[w]==0)
						{
							flag=0;
						}
					}
					if(flag==1)
					{
						cnt++;
						for(int h=k-1;h>=0;h--)
					{
						cout<<a[h];
					}
					cout<<" ";
					//cout<<"\n";
					for (int w = 2; w < 11; ++w)
					{
						cout<<v2[w]<<" ";
					}
					cout<<"\n";
					}
					
				//}
				



			}
		}
	}
	return 0;
}