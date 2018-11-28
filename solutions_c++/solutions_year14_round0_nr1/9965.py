#include<iostream>
#include<string>
#include<fstream>
using namespace std;
struct c{
	string h;
	int x;
	bool inti;
	c()
	{
		h="";
		inti=false;
	}
};
int main()
{
	ofstream o("output.txt",ios::app);
	int time=0,row_one,row_two;
	ifstream in("A-small-attempt6.in");
	
in>>time;
time++;
int total=time;
	c *p=new c[time];
	int frow[16];
	int nrow[16];
	int x=0,i,j;
	int finalanswer=0;
	int check=0;
	
	while(time!=0)
	{
		finalanswer=0;check=0;

		in>>row_one;
		in>>frow[0]>>frow[1]>>frow[2]>>frow[3];
		in>>frow[4]>>frow[5]>>frow[6]>>frow[7];
		
		in>>frow[8]>>frow[9]>>frow[10]>>frow[11];
		
		in>>frow[12]>>frow[13]>>frow[14]>>frow[15];

		in>>row_two;
		
		in>>nrow[0]>>nrow[1]>>nrow[2]>>nrow[3];
	
		in>>nrow[4]>>nrow[5]>>nrow[6]>>nrow[7];
		
		in>>nrow[8]>>nrow[9]>>nrow[10]>>nrow[11];
		
		in>>nrow[12]>>nrow[13]>>nrow[14]>>nrow[15];
		
		if(row_two==1 && row_one==1)
		{
			for(j=0;j<=3;j++)
				{
				for( i=0;i<=3;i++)
					{
						if(frow[j]==nrow[i])
						{
							finalanswer=frow[j];
							check++;
						}
					}
				}
		}

		if(row_two==1 && row_one==2)
		{
			for(j=4;j<=7;j++)
				{
				for( i=0;i<=3;i++)
					{
						if(frow[j]==nrow[i])
						{
							finalanswer=frow[j];
							check++;
						}
					}
				}
		}
			if(row_two==1 && row_one==3)
		{
			for(j=8;j<=11;j++)
				{
				for( i=0;i<=3;i++)
					{
						if(frow[j]==nrow[i])
						{
							finalanswer=frow[j];
							check++;
						}
					}
				}
		}
	if(row_two==1 && row_one==4)
		{
			for(j=12;j<=15;j++)
				{
				for( i=0;i<=3;i++)
					{
						if(frow[j]==nrow[i])
						{
							finalanswer=frow[j];
							check++;
						}
					}
				}
		}
	/////////////////////////////////////////////////////////////////////////////////////////////
	if(row_two==2 && row_one==1)
		{
			for(j=0;j<=3;j++)
				{
				for( i=4;i<=7;i++)
					{
						if(frow[j]==nrow[i])
						{
							finalanswer=frow[j];
							check++;
						}
					}
				}
		}

		if(row_two==2 && row_one==2)
		{
			for(j=4;j<=7;j++)
				{
				for( i=4;i<=7;i++)
					{
						if(frow[j]==nrow[i])
						{
							finalanswer=frow[j];
							check++;
						}
					}
				}
		}

			if(row_two==2 && row_one==3)
		{
			for(j=8;j<=11;j++)
				{
				for( i=4;i<=7;i++)
					{
						if(frow[j]==nrow[i])
						{
							finalanswer=frow[j];
							check++;
						}
					}
				}
		}
	if(row_two==2 && row_one==4)
		{
			for(j=12;j<=15;j++)
				{
				for( i=4;i<=7;i++)
					{
						if(frow[j]==nrow[i])
						{
							finalanswer=frow[j];
							check++;
						}
					}
				}
		}

	///////////////////////////////////////////////////////////////////////////////
	if(row_two==3 && row_one==1)
		{
			for(j=0;j<=3;j++)
				{
				for( i=8;i<=11;i++)
					{
						if(frow[j]==nrow[i])
						{
							finalanswer=frow[j];
							check++;
						}
					}
				}
		}

		if(row_two==3 && row_one==2)
		{
			for(j=4;j<=7;j++)
				{
				for( i=8;i<=11;i++)
					{
						if(frow[j]==nrow[i])
						{
							finalanswer=frow[j];
							check++;
						}
					}
				}
		}

			if(row_two==3 && row_one==3)
		{
			for(j=8;j<=11;j++)
				{
				for( i=8;i<=11;i++)
					{
						if(frow[j]==nrow[i])
						{
							finalanswer=frow[j];
							check++;
						}
					}
				}
		}
	if(row_two==3 && row_one==4)
		{
			for(j=12;j<=15;j++)
				{
				for( i=8;i<=11;i++)
					{
						if(frow[j]==nrow[i])
						{
							finalanswer=frow[j];
							check++;
						}
					}
				}
		}


//////////////////////////////////////////////////////////////////////////////////////
	if(row_two==4 && row_one==1)
		{
			for(j=0;j<=3;j++)
				{
				for( i=12;i<=15;i++)
					{
						if(frow[j]==nrow[i])
						{
							finalanswer=frow[j];
							check++;
						}
					}
				}
		}

		if(row_two==4 && row_one==2)
		{
			for(j=4;j<=7;j++)
				{
				for( i=12;i<=15;i++)
					{
						if(frow[j]==nrow[i])
						{
							finalanswer=frow[j];
							check++;
						}
					}
				}
		}

			if(row_two==4 && row_one==3)
		{
			for(j=8;j<=11;j++)
				{
				for( i=12;i<=15;i++)
					{
						if(frow[j]==nrow[i])
						{
							finalanswer=frow[j];
							check++;
						}
					}
				}
		}
	if(row_two==4 && row_one==4)
		{
			for(j=12;j<=15;j++)
				{
				for( i=12;i<=15;i++)
					{
						if(frow[j]==nrow[i])
						{
							finalanswer=frow[j];
							check++;
						}
					}
				}
		}
////////////////////////////////////////////////////////////
	if(check>1)
	{
		p[x].h="Bad magician!";
		p[x].inti=false;
	}
	if(check==0)
	{
	p[x].h="Volunteer cheated!";
	p[x].inti=false;
	}
	if(check==1)
		{
			p[x].x=finalanswer;
			p[x].inti=true;
		}
	x++;
	time--;
	}
	for( i=1;i<total;i++)
	{
		o<<"Case #"<<i<<": ";
		if(p[i-1].inti==true)
		{
			o<<p[i-1].x<<endl;
		}
		else
			o<<p[i-1].h<<endl;
	}
	
	return 0;
}