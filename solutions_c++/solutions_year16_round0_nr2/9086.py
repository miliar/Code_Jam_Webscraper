//revenge of the pancakes problem

#include<iostream>
#include<string.h>

using namespace std;
bool IsDone(char []);

const int MAX = 105;

int main()
{
  int i,flag,count = 0,T,item_count = 1;
  char string[MAX];
 
  cin>>T;

  while(T--){
      cin>>string;

      //check if the entire string has the happy faces
      for(i = 0;string[i] != '\0';++i)
	if(string[i] != '-')
	  break;	 	 
      if(i == strlen(string)){
	cout<<"Case #"<<item_count<<": 1"<<endl;
        count = 0;
        item_count++;
	continue;
      }

      //check if all the cakes have the blank faces
       for(i = 0;string[i] != '\0';++i)
	 if(string[i] != '+')
	   break;	 
       if(i == strlen(string)){
          cout<<"Case #"<<item_count<<": 0"<<endl;
          count = 0;
          item_count++;
	  continue;
       }

       //check for the rest of the cases
       while(1)
	 {
	   if(string[0] == '-')
	     {
	       for(i = 0;string[i] != '+' && string[i] != '\0';++i)
		 string[i] = '+';
	     }
	   else
	     {
               for(i = 0;string[i] != '-' && string[i] != '\0';++i)
		 string[i] = '-';
	     }
	   count++;
	   if(strlen(string) == i || IsDone(string))
            {
	      cout<<"Case #"<<item_count<<": "<<count<<endl;
              count = 0;
              item_count++;
	      break;
	    }
	 }
  }
  return 0;
}

bool IsDone(char string[])
{
  int j;

  for(j = 0;string[j] != '\0';++j){
    if(string[j] == '+')
      continue;
    else
      break;
  }

  if(strlen(string) == j)
    return true;
  else
    return false;
}
