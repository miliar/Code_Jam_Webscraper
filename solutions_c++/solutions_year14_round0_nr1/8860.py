#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream cin;
	ofstream cout;
	int t;
	cin.open("C:\\Users\\Admin\\Downloads\\A-small-attempt5.in");
	cout.open("C:\\Users\\Admin\\Downloads\\out.txt");
	cin>>t;
	int y=1;
	while(t--)
	{
		int i,j,a1,a2,arr1[4][4],arr2[4][4];
		cin >> a1;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin >> arr1[i][j];
			}
		}
		cin >> a2;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin >> arr2[i][j];
			}
		}
		int x,p[17]={0},q[17]={0},count=0;
		for(i=0;i<4;i++)
		{
		   p[arr1[a1-1][i]]++;
		   q[arr2[a2-1][i]]++;
        }
		for(i=0;i<17;i++)
		{
			if(p[i]==q[i] && p[i]!=0)
			{
			    count++;
			x=i;
			}
		}
		if(count==0)
		cout << "Case #"<<y<< ": Volunteer Cheated!" << endl;
		else if(count==1)
		cout <<  "Case #"<<y<<": "<< x <<endl;
		else
		cout << "Case #"<<y<< ": Bad Magician!" <<endl;
		y++;
	}
	cin.close();
	cout.close();
	return 0;
}
