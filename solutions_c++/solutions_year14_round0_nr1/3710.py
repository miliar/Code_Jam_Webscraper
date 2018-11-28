#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	vector<long> grid1, grid2;
	long gR1, gR2, i, j, temp, temp1, val;
	long cases,ccount=1,count=1;
	
	string str,out;
	scanf("%ld\n",&cases);
	while(cases--)
	{
		grid1.clear();
		cin>>gR1;
		i=0;
		while(i<16)
		{
			cin >> temp;
			grid1.push_back(temp);
			i++;
		}

		grid2.clear();
		cin>>gR2;
		i=0;
		while(i<16)
		{
			cin >> temp;
			grid2.push_back(temp);
			i++;
		}

		count = 0;
		temp = (gR1-1)*4;
		temp1 = (gR2-1)*4;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(grid1[temp+i]==grid2[temp1+j])
				{
					count++;
					val = grid2[temp1+j];
				}
			}	
		}
		
		if(count==1)
			cout<<"Case #"<<ccount<<": "<<val<<endl;
		else if(count>1)
			cout<<"Case #"<<ccount<<": Bad magician!"<<endl;
		else
			cout<<"Case #"<<ccount<<": Volunteer cheated!"<<endl;

		ccount++;
	}


	return 0;
}