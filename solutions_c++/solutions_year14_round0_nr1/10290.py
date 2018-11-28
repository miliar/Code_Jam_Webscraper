#include<iostream>
#include<algorithm>
#include<fstream>

using namespace std;

int main()
{
int card,r,T,cards[4][4],row[4],count,i,j,n;
cin>>T;

ofstream f;
f.open("output.txt");

n=1;

while(n<=T)
{
	count=0;	
	
	cin>>r;
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			cin>>cards[i][j];

	
	for(i=0;i<4;i++)
		row[i]=cards[r-1][i];

	cin>>r;
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			cin>>cards[i][j];

	sort(row,row+4);
	
	
	for(i=0;i<4;i++)
	{	
		j=0;
	
		while(cards[r-1][i]>=row[j] && j<4)
		{	//cout<<cards[r-1][i]<<"     "<<row[j]<<"\n";
			if(cards[r-1][i]==row[j])
				{
					count++;
					card=row[j];
				}
			j++;
		}

	}
	
	if(count==0)
		f<<"Case #"<<n<<": Volunteer cheated!\n";
	if(count==1)
		f<<"Case #"<<n<<": "<<card<<"\n";
	if(count>1)
		f<<"Case #"<<n<<": Bad magician!\n";

	n++;
}

f.close();
return(0);

}


	
