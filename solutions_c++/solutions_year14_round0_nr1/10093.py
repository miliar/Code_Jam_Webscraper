#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;
int main()
{
  freopen("A-small-attempt2.in","rt",stdin);
  freopen("output","wt",stdout);
  int cards1[4][4],cards2[4][4],row,col;
  int cases,q,count,no;
  cin>>cases;
  for(q=0;q<cases;q++)
    {
      cin>>row;
      row=row-1;
      count=0;
      for(int i=0;i<4;i++)
	{
	  for(int j=0;j<4;j++)
	    {
	      cin>>cards1[i][j];
	    }
	}
      cin>>col;
      col=col-1;
      for(int i=0;i<4;i++)
	{
	  for(int j=0;j<4;j++)
	    {
	      cin>>cards2[i][j];
	    }
	}
      for(int i=0;i<4;i++)
	{
	  for(int j=0;j<4;j++)
	    {
	      if(cards1[row][i]==cards2[col][j])
		{
		  count++;
		  no=cards1[row][i];
		}
	    }
	}
      if(count==0)
	cout<<"\nCase #"<<q+1<<": Volunteer cheated! ";
      else if(count==1)
	cout<<"\nCase #"<<q+1<<": "<<no;
      else
	cout<<"\nCase #"<<q+1<<": Bad magician!";
    }
  return 0;
}
