#include <iostream>
#include <cmath>

#define OK 1023//1111111111

using namespace std;

typedef struct S 
{
 unsigned int b : 10;
} S;

S numbers;

void solve(int x);
void extract_numbers(int x);

int main(void)
{
  numbers.b=0;
  
  int T;
  int x;
  cin>>T;
  
  int data[T];
  
  for(int i=1; i<=T;i++)
  {
    cin>>data[i-1];
    
   
  }
  
  for(int i=1 ; i<=T;i++)
  {
    numbers.b=0;
    x=data[i-1];
   
    cout<<"Case #"<<i;
    solve(x); 
    
  }
  
  
  return 0;
  
}

void solve(int x)
{
  if(!x)
  {
    cout<<": INSOMNIA"<<"\n";
    return;
  }
  
  
  int k =1;
  do
  {
    //cout<<x*k<<"\n";
    extract_numbers(x*k);

    k++;
  }
  while(numbers.b != OK);
  cout<<": "<<x*(k-1)<<"\n";
  
}

void extract_numbers(int x)
{
  while(x)
  {
    int u = (x%10);
    numbers.b = numbers.b | (1<<u);
    x=floor(x/10);
  }
}
