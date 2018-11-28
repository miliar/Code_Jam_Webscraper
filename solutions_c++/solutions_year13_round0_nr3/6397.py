#include<iostream>
#include<string.h>
using namespace std;
int main()
{
char strn[80];
cout<<"Enter the string: ";
cin.getline(strn,80);
int len=strlen(strn);

bool flag=true; 

for(int c=0;c!=len/2;c++){
if(flag){
if(strn[c]!=strn[len-c-1]){
flag=false; 
}

}
else
{
break;
}
}


if(flag){
cout<<"Palindrome";}
else
{
cout<<"Not Palindrome";
}

cin.get();
return 0;
}
