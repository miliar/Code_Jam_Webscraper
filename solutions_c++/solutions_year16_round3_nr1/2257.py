#include<bits/stdc++.h>
using namespace std;

int main()
{
	int test;
	cin >> test;
	
	int coun=1;
	
	ifstream infile;
	infile.open("A.in");
	
	ofstream outfile;
	outfile.open("result.txt");
	
	while(test--)
		{
			int n;
			cin >> n;
			int count[n];
			int temp[n];
			
			int i=0;
			for(i=0;i<n;i++)
				{
					cin >> count[i];
					temp[i]=count[i];
				}
			
			cout << "Case #"<<coun++<<": ";
			
			int flag=2;	
			while(flag==2)
			{
			flag=1;
			int max1=INT_MIN;
			int max2=INT_MIN;
			int index1=0;
			int index2=0;
			
			for(i=0;i<n;i++)
				{
					temp[i]=count[i];
				}
				
			sort(temp,temp+i);
			
			max1=temp[n-1];
			max2=temp[n-2];
			
			if(max1!=max2)
				{
					for(i=0;i<n;i++)
						{
							if(count[i]==max1)
								index1=i;
							if(count[i]==max2)
								index2=i;
						}

				}
			else
				{
					for(i=0;i<n;i++)
						if(count[i]==max1)
							index1=i;
					int j=index1+1;
					
					for(j=index1+1;j<n;j++)
						if(count[j]==max2)
							index2=j;
				}

			if(max1==max2&&index1!=index2) 
				{
					cout << index1 << index2 << " ";
					count[index1]--;
					count[index2]--;
				}
			else
				{
					cout << index1 << index1 << " ";
					count[index1]-=2;
				}
			
			for(i=0;i<n;i++)
				if(count[i]>0)
					flag=2;

			}
				
		}
	return 0;
}
