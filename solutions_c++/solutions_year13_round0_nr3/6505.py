#include<iostream.h>
#include<string.h>
#include<conio.h>
#include<math.h>
#include<stdlib.h>
#include<stdio.h>

int palin(float x)
{
	int temp=x;
	float digit;
	float rev=0;
     do
     {
	 digit = temp%10;
	 rev = (rev*10) + digit;
	 temp = temp/10;
     }while(temp!=0);
     //cout << " The reverse of the number is: " << rev << endl;
     if (x == rev)
     {
	 // cout << " The number is a palindrome";
		return 1;
	}else
       {
       //	cout << " The number is not a palindrome";
	return 0;
	}
}


void main()
{
	int l,h;
       //	l=1;
       //	h=4;
	int x=0;
	//x=l;
	int count=0;
	clrscr();
	int no=0;
	FILE *fp=fopen("input1.txt","r");
	FILE *fo=fopen("outpu.txt","a");
	fscanf(fp,"%d",&no);
       //	cout<<no<<endl;
	int cases=0;
	while(cases!=no)
       {
	count=0;
	fscanf(fp,"%d",&l);
      //	fscanf(fp,"%d",&count);
	fscanf(fp,"%d",&h);
	cout<<l<<"\t"<<h<<endl;
      //	fclose(fp);
	float q,a;
	x=l;
	while(x!=h+1)
	{
		a=palin(x);
		if(a==1)
		{
		     float b=sqrt(x);
	      //	     cout<<"No."<<x<<" "<<b<<endl;
		     q=palin(b);

		}
		else
			q=0;
			//	cout<<"no. not";
		if(q==1)
		{
	      //		cout<<"root:"<<x<<endl;
			count++;
		}
	    //	else
	    //	 	cout<<"square not";
		x=x+1;
	}
	fprintf(fo,"%s%d: %d\n","Case #",(cases+1),count);
      //	fprintf(fo,"%d",count);
	cout<<"Case#"<<cases+1<<":"<<count<<endl;
	cases++;
       }
       fclose(fo);
       fclose(fp);
       getch();
}