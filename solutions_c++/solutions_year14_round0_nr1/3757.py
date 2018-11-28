#include<iostream>

using namespace std;







void main()
{

	int T=0;

	int r1=0,r2=0;

	int a[5][5],b[5][5];
	int count=0;
	int y=0;

	scanf("%d",&T);

	for(int i=1;i<=T;i++)
	{
		count=0;
		cin>>r1;

		for(int r=1;r<=4;r++)
		{
			for(int c=1;c<=4;c++)
			{
				scanf("%d",&a[r][c]);
			}

		}

		cin>>r2;

		for(int r=1;r<=4;r++)
		{
			for(int c=1;c<=4;c++)
			{
				scanf("%d",&b[r][c]);
			}

		}

   for(int c=1;c<=4;c++)
   {
	   for(int c2=1;c2<=4;c2++)
	   {
	       if(a[r1][c]==b[r2][c2])
		 {
			y=a[r1][c];
			count++;

	     }
	  }
   }

   if(count==1)
	   cout<<"Case #"<<i<<": "<<y<<endl;
   else if(count>1)
	   cout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
   else if(count==0)
   cout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;

      
	}//test loop ends



	

}
