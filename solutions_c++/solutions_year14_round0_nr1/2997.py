#include<iostream>
#include<fstream>


using namespace std;

void main()
{
	fstream fs,os;
	int comb1[4],comb2[4],ans=0,t,row1,row2,cnt=0,val=1,temp;

	fs.open("magic1.in",ios::in);
	os.open("sol.txt",ios::out);
	fs>>t;
	fs.get();

	while(t>0)
	{
		
		fs>>row1;
		fs.get();

		for(int i=0;i<4;i++)
		{
				for(int j=0;j<4;j++)
			{
				if(i==row1-1)
				{
					fs>>comb1[j];
					fs.get();
				}
				else
					{
					fs>>temp;
					fs.get();
			
				}
				}
		}

		fs>>row2;
		fs.get();

		for(int i=0;i<4;i++)
		{
				for(int j=0;j<4;j++)
			{
				if(i==row2-1)
				{
					fs>>comb2[j];
					fs.get();
				}
				else
					{
					fs>>temp;
					fs.get();
			
				}
				}
		}	

		for(int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
			{
				if(comb1[i]==comb2[j])
					{
					cnt++;
					ans=comb1[i];
					}
				}
		}

		

		if(cnt==1)
			os<<"Case #"<<val<<" "<<ans<<"\n";
		else if(cnt==0)
			os<<"Case #"<<val<<" "<<"Volunteer cheated!\n";
		else
			os<<"Case #"<<val<<" "<<"Bad magician!\n";

		val++;
		t--;
		cnt=0;
	}

	os.close();
	fs.close();
}




