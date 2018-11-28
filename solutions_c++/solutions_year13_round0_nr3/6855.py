#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;

bool palindrome(unsigned long long &number)
{
unsigned long long copy = number;
unsigned long long reversenumber = 0;
while(copy!=0)
{
reversenumber= reversenumber*10 + copy%10;
copy/=10; 
}
return (number==reversenumber);
}

int main()
{
vector <unsigned long long> memoizer;
memoizer.assign(100000000,-1);
int cn=1;
cin>>cn;
int *input=new int[cn*2];
int *output=new int[cn];
for(int a=0; a < cn*2; a++)
{
cin>>input[a];
}

for(int a=0,out=0; a < cn*2; a+=2,out++)
{
output[out]=0;

for(unsigned long long b=(unsigned long long)ceil(sqrt(input[a])); 
b <=floor(sqrt(input[a+1])); b++)
{ 
if(memoizer[b]==1)
++output[out];
if(memoizer[b]==-1)
{
++memoizer[b];
if(palindrome(b))
{
unsigned long long c=b*b;
if(palindrome(c))
{
++output[out];
++memoizer[b];
}
}
}

} 
} 


for(int a=1; a <=cn; a++)
{
printf("Case #%d: %d\n",a,output[a-1]);
} 

}
