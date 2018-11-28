#include<iostream>
#include<algorithm>
#include<vector>
#include<fstream>
using namespace std;
int main()
{
	ifstream fin("c_.in");
	ofstream fout("c.out");
	int t,ans=0,temp,num,temp1,ans1=0;
	fin>>t;
	for(int cas=0;cas<t;cas++)
	{
		fin>>num;
		vector<float> naomi(num),mike(num);
		int i=0;
		for(i=0;i<num;i++)
		{
			fin>>naomi[i];
		}
	
		for(i=0;i<num;i++)
		{
			fin>>mike[i];
		} 
		sort(naomi.begin(),naomi.end());
		sort(mike.begin(),mike.end());
		temp=0;
		int num1;
		num1=num;
		for(int k=0;k<num1;k++)
		{
			while(naomi[temp]<mike[k])
			{
				temp++;
				num1--;
			}
			while(temp<num)
			{
				if(mike[k]<naomi[temp])
				{
					ans++;	// not declared
					temp++; // not declared 
					break;
				}
				temp++;
			}
		}
		temp1=0;
		for(int h=0;h<num;h++)
		{
			while(temp1<num)
			{
				if(naomi[h]<mike[temp1])
				{
					ans1++;
					
					temp1++;
					break;
				}
				temp1++;
			}
		}
		fout<<"Case #"<<cas+1<<": "<<ans<<" "<<num-ans1<<endl; 
		ans=0;
		ans1=0;
	}
		return 0;
}	
		
			
			
	
	

