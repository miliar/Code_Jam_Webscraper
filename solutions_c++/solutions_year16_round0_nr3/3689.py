#include <iostream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <fstream>
#include <map>
#include <cstring>
using namespace std;

ofstream output;
char a[2] = {'0','1'};
int sourceTo10(string,int,int);
int factor(unsigned long long int);

int sourceTo10(string source,int n,int base) 
{
  unsigned long long int decimal=0,l=0;
  for(int k = n-1 ; k >= 0; k--)
    {
      decimal += (source[k]-'0')*pow(base,l);
      l = l + 1;
    }
  return factor(decimal);
}

int factor(unsigned long long int n)
{
  if(n < 4) return -1;
  if(n%2 == 0) return 2;
  for(unsigned long long int i = 3; i <= sqrt(n); i=i+2)
    {
      if(n%i==0) return i;
    }
  return -1;
}

int final(string new_str,int orig)
{
  int score[9];
  score[0] = sourceTo10(new_str,orig,2);
  if(score[0] == -1) return -1;
  score[1] = sourceTo10(new_str,orig,3);
  if(score[1] == -1) return -1;
  score[2] = sourceTo10(new_str,orig,4);
  if(score[2] == -1) return -1;  
  score[3] = sourceTo10(new_str,orig,5);
  if(score[3] == -1) return -1;
  score[4] = sourceTo10(new_str,orig,6);
  if(score[4] == -1) return -1;
  score[5] = sourceTo10(new_str,orig,7);
  if(score[5] == -1) return -1;
  score[6] = sourceTo10(new_str,orig,8);
  if(score[6] == -1) return -1;
  score[7] = sourceTo10(new_str,orig,9);
  if(score[7] == -1) return -1;
  score[8] = sourceTo10(new_str,orig,10);
  if(score[8] == -1) return -1;
  output<<new_str<<" ";
  for(int l = 0; l <= 8; l++) {
    output<<score[l]<<" ";
  }
  output<<endl;
  return 0;
}

// Rec("", n-2, n-2, j, &count);
void Rec(string current, int numDigits, int orig, int j, int *count) {
  int effDigits;
  if(numDigits==0) 
    {
      string new_str = "1" + current + "1";
      if(*count < j) 
	{
	  if(final(new_str,orig+2) == 0) *count = *count + 1;
	}
      else return;
    }
  else if(*count < j) 
    {
      for(int p = 0 ; p < 2 ; p++)
	{
	  if(*count < j) Rec(current+a[p], numDigits-1, orig, j, count);                  	      
	  else return;
	}
    }
  else return;	 
}

int main() { 
  output.open("output.txt");
  int t;
  cin >> t;
  int n,j;
  for(int i=1;i<=t;i++) {
    output << "Case #" << i << ": "<<endl;
    cin>>n;
    cin>>j;
    int count = 0;
    Rec("", n-2, n-2, j, &count);
  } 
  return 0; 
}
