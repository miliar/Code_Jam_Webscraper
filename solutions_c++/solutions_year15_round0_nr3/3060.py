#include<iostream>
#include<vector>
#include<utility>

using namespace std;

int a[4][4];

void fill()
{
a[0][0] = 0;
a[0][1] = 1;
a[0][2] = 2;
a[0][3] = 3;
a[1][0] = 1;
a[1][1] = 4;
a[1][2] = 3;
a[1][3] = 6;
a[2][0] = 2;
a[2][1] = 7;
a[2][2] = 4;
a[2][3] = 1;
a[3][0] = 3;
a[3][1] = 2;
a[3][2] = 5;
a[3][3] = 4;	
}

int getResult(int prev, char c)
{
    int b;
    if(c == '1')
	b = 0;
    if(c == 'i')
	b = 1;
    if(c == 'j')
	b = 2;
    if(c == 'k')
	b = 3;
    if(prev == -1)
	return b;
    int neg=0;
    if(prev >= 4)
    {
	neg = 1;
        prev = prev-4;
    }
   int p = a[prev][b];
   if(neg)
   {
	if(p >= 4)
	   p = p-4;
        else
	   p = p+4;
   }
   return p;
}

void printAns(int N,int K, string s)
{
      int b[N*K];
      int prev = -1;
      for(int i=0;i<K;i++)
      {
	for(int j=0;j<N;j++)
	{
	    b[(i*N)+j] = getResult(prev,s[j]); 
	   prev = b[(i*N)+j]; 
	}
      }
     if(b[(N*K)-1] != 4)
     {
	cout << "NO";
	return;
     }
    bool found = false;
    int p;
    for(int i=0;i<(N*K);i++)
    {
	if(b[i] == 1)
	{
	  found = true;
	  p = i;
	  break;
	}
    }
    if(!found)
    {
	cout << "NO";
	return;
    }
   found = false;
   for(int i=p;i<(N*K);i++)
   {
	if(b[i] == 3)
	{
	   cout << "YES";
	   return;
	}
   }
   cout << "NO";
    
}
int main()
{
    fill();
    int T,N;
    cin >> T; 
    int j=0;
    while(T--)
    {
       cout << "Case #" << j+1 <<": ";
       int K;
       cin >> N >> K;
       string s;
       cin >> s;
       printAns(N,K,s);
       cout << endl;
       j++;
    }
  return 0;
}
