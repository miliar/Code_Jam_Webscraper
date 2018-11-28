#include<iostream>
void reverse (char*,int);
int find (char*,int);
using namespace std;

int length;

int main()
{
  int cse=0;
  cin>>cse;
  for(int c=1;c<cse+1;c++)
    {
      char* pancake=new char[100];
      for(int i=0;i<100;i++)
	{
	  pancake[i]=0;
	}
      cin>>pancake;
      length=0;
      //get how many pancake
      for(length;;length++)
      {
	if(pancake[length]==0)
	  break;
      }
      length--;
      //main  fliping!
      int count=0;
      //if is + at the end, length-1
      for(length;length>=0;)
	{
	  if(pancake[length]=='+')
	    {
	      length--;
	      continue;
	    }
	  else if(pancake[length]=='-')
	    {
	      if(pancake[0]=='-')
		{
		  reverse(pancake, length);
		  count++;
		  continue;
		}
	      if(pancake[0]=='+')
		{
		  int plus =find(pancake, length);
		  reverse(pancake,plus);
		  count++;
		  continue;
		}
	    }
	}
      cout<<"Case #"<<c<<": "<<count<<endl;
    }
  return 0;
}
void reverse(char* pancake, int i)
{
  char* temp=new char[i+1];
  for(int j=0;j<=i;j++)
    temp[j]=pancake[j];

  for(int j=0;j<=i;j++)
    {
      if (temp[i-j]=='+')
	pancake[j]='-';
      else if (temp[i-j]=='-')
	pancake[j]='+';
    }
  delete temp;
}

int find(char* pancake, int i)
{
  for(i;i>=0;i--)
    {
      if(pancake[i]=='+')
	return i;
    }
  return i;
}
