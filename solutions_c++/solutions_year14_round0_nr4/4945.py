#include <bits/stdc++.h>

using namespace std;



double naomi[10],ken[10];

int find_ans2(int a)
	{
		int count = 0;
		int i,j=0;
		
		i=0;
		
		while(i<a)
		{
			
			if(ken[i] > naomi[j])
			{
				i++;
				j++;
				count++;
			}

			else
			{
				i++;
			}
		}
		
		return a-count;
		
	}

int find_ans(int a)
	{
		

		int count=0;

		int i,j=0;
		
		i=0;
		
		while(i<a)
		{
			
			if(naomi[i] > ken[j])
			{
				i++;
				j++;
				count++;
			}

			else
			{
				i++;
			}
		}

		return count;
		
	}


int main(void)
	{
		//freopen("input.txt","r",stdin);
		//freopen("output.txt","w",stdout);
		
		
		

		int i,t,n,j;

		cin >> t;
	
	
		for(i=0;i<t;i++)
		{
			for(j=0;j<10;j++)
			{
				naomi[j] = 0;
				ken[j] = 0;
			}
			
			cin >> n;

			for(j=0;j<n;j++)
			{
				cin >> naomi[j];
			}

			for(j=0;j<n;j++)
			{
				cin >> ken[j];
			}


			std::sort(naomi, naomi+n);
			std::sort(ken, ken+n);
		
			printf("Case #%d: %d %d\n",i+1,find_ans(n),find_ans2(n));
			

		}


	}
