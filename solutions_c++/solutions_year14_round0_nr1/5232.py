 #include <iostream>
 #include <fstream>
 #include <string>

 using namespace std;

 int main()
{
	ifstream myfile ("i.txt");
	ofstream myfile2 ("o.txt");
	int t;
	myfile>>t;
	int max=t;
	int n;
	int b[17]={0};
	int save=0;
	int a[4][4];
		int n1;
		int i,j;
	int count=0;
		while(t>0)
		{
			myfile>>n;
			for(i=0;i<4;i++)
			{
				for(j=0;j<4;j++)
				{
					myfile>>a[i][j];
				}
			}
		for(j=0;j<4;j++)
		{
			b[a[n-1][j]]=1;
		}
		for(j=0;j<16;j++)
		{
		//	cout<<b[j]<<" ";
		}
		myfile>>n1;
		//cout<<endl;
		for(i=0;i<4;i++)
			{
				for(j=0;j<4;j++)
				{
					myfile>>a[i][j];
				}
			}
		for(j=0;j<4;j++)
		{
			b[a[n1-1][j]]++;
		}
		for(j=0;j<17;j++)
		{
		//	cout<<b[j]<<" ";
		}
		for(j=0;j<17;j++)
		{
			if(b[j]==2)
             {
             	count++;
             	save=j;
             }
		}
		if(count==1)
		{
			myfile2<<"Case #"<<max-t+1<<": "<<save<<endl;
		}
		if(count<1)
		{
         myfile2<<"Case #"<<max-t+1<<": "<<"Volunteer cheated!"<<endl;
		}
		if(count>1)
		{
		myfile2<<"Case #"<<max-t+1<<": "<<"Bad magician!"<<endl;
		}
		count=0;
		for(j=0;j<17;j++)
		{
			b[j]=0;
		}
t--;	
}


	return 0;
	
}
