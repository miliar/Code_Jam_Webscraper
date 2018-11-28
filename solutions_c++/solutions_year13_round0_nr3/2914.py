
#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<math.h>

using namespace std;
ifstream input;
ofstream output;

int *arr;
char token[10];

void gettoken(){
	int  i = 0 ;
	char c = input.get() ;
	/* Skip all spaces */
    
	while(!input.eof() && (c==' '|| c == '\n' || c == '\t' ))
		c=input.get();	
	while(c != ' ' && c != '\t' &&	c!= '\n' )
	{  	   
	   token[i++] = c;
	   c = input.get();
	
	   if(input.eof())
		   break;
	}  token[i] = '\0';
	
}


bool palindrome(int no)
{
  int number = no;
  int temp = 0;
  int placeValue = 1;
  while (number>0)
    {
        temp = (temp*placeValue) + number % 10;
        number /= 10;
        placeValue = 10;
    }

    if(temp == no)
      return true;
    else
      return false;
}

bool isSquare(int no)
{
  double sqroot = sqrt(no);
  double i = sqroot - int(sqroot) ;
  if(i == 0)
    return true;
  else 
    return false; 
}

int solution(int start, int end)
{
  int answer = 0;
  for (int i = start; i<= end; i++)
  {
    if(palindrome(i) == true)
       {
         if(isSquare(i) == true)
          {
            if(palindrome(sqrt(i)) == true)
              {
                answer++;
              }
          }
       }   
  }
  return answer;
}

int main()
{
    input.open("C-small-attempt0.in", ios::in);
    int start, end;
    gettoken();
    int testCases = atoi(token);
    for(int i = 0; i<testCases; i++)
    {
       
       gettoken();
       start = atoi(token);
       gettoken();
       end = atoi(token);
       
       cout<<"Case #"<<i+1<<": "<<solution(start, end)<<"\n";
      
    }
    
	return 0;
}