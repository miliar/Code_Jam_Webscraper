//input file has been renamed as a.txt
# include<fstream.h>
ifstream inp;
ofstream op;
class magic
	{
		int t,arr1[4][4],arr2[4][4],temp1[4],temp2[4],out[100],r1,r2,i,j,count;
		int flag,num;
		public:
		magic();
		void getdata();
		void check();
		void display();
	}
magic::magic()
	{
		t=0;
		r1=0;
		r2=0;
		count=0;
		for(i=0;i<4;i++)
			{
				for(j=0;j<4;j++)
					{
						arr1[i][j]=0;
						arr2[i][j]=0;
					}
			}
		for(i=0;i<4;i++)
			{
				temp1[i]=0;
				temp2[i]=0;
			}
		for(i=0;i<100;i++)
			{
				out[i]=0;
			}

	}
void magic::getdata()
	{	inp>>t;
		while(count<=t)
			{
				inp>>r1;
				for(i=0;i<4;i++)
					{
						for(j=0;j<4;j++)
							{
								inp>>arr1[i][j];

								if(i+1==r1)
									{
									temp1[j]=arr1[i][j];
									}
							}
					}
				inp>>r2;
				for(i=0;i<4;i++)
					{
						for(j=0;j<4;j++)
							{
								inp>>arr2[i][j];
								if(r2==i+1)
									{
									temp2[j]=arr2[i][j];
									}
							}
					}
				check();
				++count;
			}
	}
void magic::check()
	{       flag=0;
		num=0;
		for(i=0;i<4;i++)
			{
			for(j=0;j<4;j++)
			{
				if(temp1[i]==temp2[j])
					{
						flag++;
						num=temp1[i];
					}
			}
			}
		if(flag==1)
			{
				out[count]=num;
			}
		else if(flag==0)
			{
				out[count]=num;
			}
		else if(flag>1)
			{
				out[count]=111;
			}
	}
void magic::display()
	{
		for(i=0;i<t;i++)
			{
				op<<"Case #"<<i+1<<": ";
				if(out[i]==0)
					op<<"Volunteer cheated!\n";
				else if(out[i]==111)
					op<<"Bad magician!\n";
				else
					op<<out[i]<<"\n";
			}
	}
void main()
	{
		inp.open("a.txt");
		op.open("out1.txt",ios::trunc);
		magic m;
		m.getdata();
		m.display();
		inp.close();
		op.close();
	}







