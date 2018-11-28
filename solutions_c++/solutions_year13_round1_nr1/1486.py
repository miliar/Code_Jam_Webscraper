#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>

using namespace std;

ifstream input;

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


double are(int r)
{
  return r*r;
}

int main()
{
    input.open("A-small-attempt0.in", ios::in);
    int start, end, paint;
    double v = 0;
    gettoken();
    int testCases = atoi(token);
    int count = 0;
    for(int i = 0; i<testCases; i++)
    {
      gettoken();
      start = atoi(token);
      gettoken();
      paint = atoi(token);
      count = 0;
      v = 0;
      while(v <= paint)
      {
        end = start + 1;
        int  n = are(end) - are(start);
        v +=n;
        if(v <= paint)
        count ++;
        start = end + 1;
      }
     cout<<"Case #"<<i+1<<": "<<count<<"\n";
    }
    
	return 0;
}