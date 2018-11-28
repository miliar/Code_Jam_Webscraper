/*Author :KK
*/
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cmath>

#define MAX 100000
using namespace std;
int main()

{
unsigned long long bug_eye,num,result,garbage,inner,bug,T,tc,y,z,i,r,t;
unsigned long long count,flag;


cin>>T;

for(tc=0;tc<T;tc++){


cin>>r>>t;
//inner = r*r;

bug=r;
result=0;
garbage=0;
bug_eye=0;

while (garbage<t || garbage==t){

if (garbage==0)
num=(bug+1)*(bug+1) - bug*bug;
else
num=num+4;

result = result + num;

garbage=result;
bug_eye++;
bug++;

}


if (garbage>t || bug_eye !=1)
bug_eye--;


cout<<"Case #"<<tc+1<<": "<<bug_eye<<"\n";
}
return 0;
}
