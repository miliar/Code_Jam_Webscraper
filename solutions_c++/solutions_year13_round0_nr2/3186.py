
#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>

using namespace std;
ifstream input;
ofstream output;

int arr[100][100];
int arr1[100][100];
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

int findMaxRow(int i, int limit)
{
  int max = -1;
  for(int j = 0; j<limit; j++ )
  {
     if(arr[i][j] > max)
      max = arr[i][j];
  }
  return max;
}
 
int findMaxCol(int i, int limit)
{
  int max = -1;
  for(int j = 0; j<limit; j++ )
  {
     if(arr[j][i] > max)
      max = arr[j][i];
  }
  return max;
}

int cmp(int N, int M)
{
  int result = 1;
  for(int j = 0; j<N; j++)
    for(int k = 0; k<M; k++)
    {
      if(arr1[j][k] == arr[j][k])
        continue;
      else
      {
        return 0;
      }
    }
  return result;
}


int answer(int N, int M)
{

  for(int i = 0;i<N; i++)
  {
    int max = findMaxRow(i,M);
    
    for(int k = 0; k< M; k++)
    {
      if(arr1[i][k] > max)
        arr1[i][k] = max;
    }

    for(int j = 0; j < M; j++)
    {
        int max = findMaxCol(j, N);
        for(int k = 0; k< N; k++)
         {
          if(arr1[k][j] > max)
           arr1[k][j] = max;
         }
    }
  }
 
 return cmp(N, M);

}

int main()
{
    input.open("B-large.in", ios::in);
    int N,M;
    gettoken();
    int testCases = atoi(token);
    for(int i = 0; i<testCases; i++)
    {
       for(int j = 0; j<100; j++)
        for(int k = 0; k<100; k++)
         {
          arr1[j][k] = 100;
          arr[j][k] = 0;
         }

       gettoken();
       N = atoi(token);
       gettoken();
       M = atoi(token);
       for(int j = 0; j<N; j++)
         for(int k = 0; k<M; k++)
         {
          gettoken();
          arr[j][k] = atoi(token);
         }
       cout<<"Case #"<<i+1<<": ";
       int v = answer(N,M);
       if(v == 1)
        cout<<"YES\n";
       else if(v == 0)
        cout<<"NO\n";
    
      
    }
    
	return 0;
}