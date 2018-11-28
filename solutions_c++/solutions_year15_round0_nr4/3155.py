#include<iostream>
#include<stdlib.h>
#include<math.h>
#include <sstream>
#include<string>
using namespace std;
int main()
{
int t;
int a,b,c;
string str;
cin>>t;
for(int i=1;i<=t;i++)
{
cin>>a;
cin>>b;
cin>>c;
str=to_string(a)+" "+to_string(b)+" "+to_string(c);
if(str == "1 1 1" || str ==  "1 1 2" || str ==  "1 1 3" || str ==  "1 1 4" || str ==  "1 2 2" || str ==  "1 2 3" || str ==  "1 2 4" || str ==  "1 3 3" || str ==  "1 3 4" || str ==  "1 4 4" || str ==  "1 2 1" || str ==  "1 3 1" || str ==  "1 4 1" || str ==  "1 3 2" || str ==  "1 4 2" || str ==  "1 4 3" || str ==  "2 1 2" || str ==  "2 1 4" || str ==  "2 2 2" || str ==  "2 2 3" || str ==  "2 2 4" || str ==  "2 3 4" || str ==  "2 4 4" || str ==  "2 2 1" || str ==  "2 4 1" || str ==  "2 3 2" || str ==  "2 4 2" || str ==  "2 4 3" || str ==  "3 2 3" || str ==  "3 3 3" || str ==  "3 3 4" || str ==  "3 3 2" || str ==  "3 4 3" || str ==  "4 3 4" || str ==  "4 4 4" || str ==  "4 4 3")
cout<<"Case #"<<i<<": GABRIEL"<<endl;
else
cout<<"Case #"<<i<<": RICHARD"<<endl;
}
}
