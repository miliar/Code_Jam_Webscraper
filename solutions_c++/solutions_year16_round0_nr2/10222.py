#include <iostream>  
#include <string>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
using namespace std; 
int pancakes(string);
int main() {
  int t;
  string n;
  cin >> t;  
  for (int i = 1; i <= t; ++i) {
    cin >> n;
    if(n.size()>=0&&n.size()<=10)   
        cout << "Case #" << i << ": " <<pancakes(n)<< endl;
    else{i--;}
  }
}
int pancakes(string n)
{
   int enc, fin=0, cnt=0;
   string s;
   do{
   enc=n.find_last_of("-"); 
   if(enc==-1)
	fin=1;
   else{
	for(int i=0;i<=enc;i++)
		if(n[i]=='-')n[i]='+';
		else n[i]='-';
     for(int k=0;k<enc;k++)
         s[k]=n[k];       
     n.replace(enc,enc,string(s.rbegin(),s.rend()));
     cnt++; 
     } 
   }     
   while(fin!=1);
   return cnt;
}
