/*
 * =====================================================================================
 *
 *       Filename:  1.cpp
 *
 *    Description:
 *
 *        Version:  1.0
 *        Created:  04/09/2016 08:21:03 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Gaurav (disisbig), giganticgemmic@gmail.com
 *   Organization:  PEC University of Technology,Chandigarh
 *
 * =====================================================================================
 */

#include<bits/stdc++.h>
using namespace std;
int main()
{
ifstream fin;
ofstream fout;
fin.open("input");
fout.open("output");

int T;
fin>>T;

for(int t=1;t<=T;t++)
{
long long  n,count=0;
fin>>n;
int arr[10]={0};
if(n==0)
fout<<"Case #"<<t<<": INSOMNIA"<<endl;
else
{
int i=1;
long long  num2=n;
long long  num1=n;

while(count<10)
{
int temp=10;
while(num2!=0)
{
if(arr[num2%temp]==0)
{
arr[num2%temp]=1;
count++;
}

if(count==10)
{
fout<<"Case #"<<t<<": "<<num1<<endl;
break;
}
else
{
num2/=temp;
}

}

i++;
num2=i*n;
num1=num2;
}
}
}
return 0;
}
