#include<stdio.h>
#include<conio.h>
#include<iostream.h>
#include<fstream.h>


void main()
{
     int c;
     int r1,r2,x,y,z,w,result;
     int arr1[16],arr2[16];
     int ca1[4],ca2[4];

     ofstream myfile;
     myfile.open("Output3.text");

     ifstream infile;
     infile.open ("myfile3.in");


     clrscr();

     cout<<"Enter No of Cases";
     infile>> c ;


     for(int ptr=1;ptr<=c;ptr++)
     {

	x=0;
	y=0;
	z=0;
	w=0;

	cout<<"Enter Row1 \n";
	infile>>r1;
	cout<<"Enter arrengement1 \n";

	for(int i=0;i<=15;i++)
	{
		infile>>arr1[i];
	}

	cout<<"Enter Row2 \n";
	infile>>r2;
	cout<<"Enter arrengement2 \n";
	for(int j=0;j<=15;j++)
	{
		infile>>arr2[j];
	}

	int p1=(r1-1)*4;
	int p2=(r2-1)*4;

	for(int p=0;p<=3;p++)
	{
		ca1[p]= arr1[p1];
		p1++;

	}
	for(int q=0;q<=3;q++)
	{
		ca2[q]= arr2[p2];
		p2++;

	}

	if((ca1[0]==ca2[0])||(ca1[0]==ca2[1])||(ca1[0]==ca2[2])||(ca1[0]==ca2[3]))
	{
		x=1;
	}
	if((ca1[1]==ca2[0])||(ca1[1]==ca2[1])||(ca1[1]==ca2[2])||(ca1[1]==ca2[3]))
	{
		y=1;
	}
	if((ca1[2]==ca2[0])||(ca1[2]==ca2[1])||(ca1[2]==ca2[2])||(ca1[2]==ca2[3]))
	{
		z=1;
	}
	if((ca1[3]==ca2[0])||(ca1[3]==ca2[1])||(ca1[3]==ca2[2])||(ca1[3]==ca2[3]))
	{
		w=1;
	}
	       myfile<<"Case #"<<ptr<<":"<<" ";

	if(x==1 && y==0 && z==0 && w==0)
	{
		result=ca1[0];
		myfile<<result<<"\n";
	}
	else if(x==0 && y==1 && z==0 && w==0)
	{
		result=ca1[1];
		myfile<<result<<"\n";
	}
	else if(x==0 && y==0 && z==1 && w==0)
	{
		result=ca1[2];
		myfile<<result<<"\n";
	}
	else if(x==0 && y==0 && z==0 && w==1)
	{
		result=ca1[3];
		myfile<<result<<"\n";
	}
	else if(x==0 && y==0 && z==0 && w==0)
	{
		myfile<<"Volunteer cheated! \n";
	}

	else
	{
		myfile<<"Bad magician! \n";
	}

  }
  myfile.close();
     getch();


}