#include <iostream>
#include <string>
#include <cstring>
#include <stdlib.h>
using namespace std;

int main ()
{
int T = 0;
string str;
getline(cin, str);
T = atoi(str.c_str());
//char x;
//cin>>x;
//cout<<T<<endl;
int C1[T];
for(int j1=0; j1<T; j1++)
{
C1[j1]=0;
}
string l1[T];
int N;
for (int i1 = 0; i1 < T; i1++){
getline(cin, l1[i1]);
}

for(int i2 = 0; i2 < T; i2++)
{
string l = l1[i2];
N=l.length();
//cout<<N<<endl;
int C = 0;
//cout<<line<<endl;
//cout<<N<<endl;
//cout<<line[0];'
char k;
if(l.find('-')==string::npos)
{
C1[i2] = 0;
//cout<<"hi"<<endl;
//cout<<N<<endl;
}
else if(N==0)
{
C1[i2] = 1;
cout<<"hello"<<endl;
}
else{
while(l.find('-')!=string::npos){
k = l[0];
int i = 0;
for(; l[i+1] == k; i++);
if(k=='-')
for(int m = 0; m<=i; m++)
l[m] = '+';
if(k=='+')
for(int m = 0; m<=i; m++)
l[m] = '-';
C++;
}
C1[i2] = C;
//cout<<N<<endl;
}
}
for(int i3 = 0; i3 < T; i3++)
cout<<"Case #"<<i3+1<<": "<<C1[i3]<<endl;
}
