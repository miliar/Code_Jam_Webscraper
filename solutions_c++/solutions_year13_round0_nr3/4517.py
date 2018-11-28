#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
using namespace std;

bool is_pal(int x);
int main()
{
		 freopen("C-small-attempt0.in", "r", stdin);
	    freopen("ouput.out", "w", stdout);

  int num_test;
 int num_fair;
 int beg,end;
 bool test;
 float root;
 int i_rot;

  scanf("%d",&num_test);
  for (int b = 0; b < num_test; b++)
  {
	  num_fair=0;
	  scanf("%d %d",&beg,&end);
	  for (int i = beg; i < end+1; i++)
	  {
		  test=is_pal(i);
		  if(test)
		  {
			root=sqrt((double)(i));
			i_rot=root;

			if(i_rot==root)
			{
			 test=is_pal(root);
		      
			 if(test)
				num_fair++;
			}
		  }
	  }

	  printf("Case #%d: %d\n",b+1,num_fair);
  }
}

bool is_pal(int x)
{
	string temp;
	stringstream ss;
	ss<<x;
	ss>>temp;

	int len=temp.length();
	for(int i=0; i<len/2; i++)
	{
	 if( temp[i]==temp[len-1-i])
	    continue;
	 else 
		 return false;
	
	}
return true;
}
