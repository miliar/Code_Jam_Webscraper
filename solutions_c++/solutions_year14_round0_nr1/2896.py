#include <iostream>
using namespace std;

int searchmat(int card,int row,int curr_mat[4][4])
{
	int ntimes = 0;
	for(int u=0;u<4;u++)
	{
		if(curr_mat[row][u]==card)
		ntimes = 1;
		
	}
	return ntimes;
}
int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int casea =1;casea<=t;casea++)
	{
		
		int firstmat[4][4];
		int foundcard[17];
		int secondmat[4][4];
		for(int i=1;i<=16;i++)
		{
			foundcard[i]=0;
		}
		int a1,a2;
		cin>>a1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			cin>>firstmat[i][j];
		}
		cin>>a2;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			cin>>secondmat[i][j];
		}
		a1--;
		a2--;
		for(int i=0;i<4;i++)
		{
			foundcard[firstmat[a1][i]]+=searchmat(firstmat[a1][i],a1,firstmat);
			foundcard[secondmat[a2][i]]+=searchmat(secondmat[a2][i],a2,secondmat);
		}
		bool alreadyfound = false;
		int prevfound = -1;
		int ncardsfound=0;
		int magmessedup = 0;
		for(int i =1;i<=16;i++)
		{
			if(alreadyfound==true&&foundcard[i]==2)
			{
				magmessedup = 1;
				ncardsfound++;
			}
			else if(foundcard[i]==2)
			{
				alreadyfound = true; 
				ncardsfound++;
				prevfound=i;
			}
		}
		if(ncardsfound==1)
		{
			cout<<"Case #"<<casea<<": "<<prevfound<<endl;
		}else if(ncardsfound==0)
		{
			cout<<"Case #"<<casea<<": Volunteer cheated!"<<endl;
		}else if(magmessedup==1)
		{
			cout<<"Case #"<<casea<<": Bad magician!"<<endl;
		}
		
	}
	return 0;
}