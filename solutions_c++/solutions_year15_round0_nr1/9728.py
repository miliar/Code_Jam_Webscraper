#include<string>
#include<iostream>
#include<vector>
#include<stdio.h>

using namespace std;

int main() {
   //freopen("input.in", "r", stdin);
   freopen("A-small-attempt1.in", "r", stdin);
   //freopen("in", "r", stdin);
   int t;
   scanf("%d\n",&t);
   //cout<<t;
   for(int i = 0; i < t; i++)
   {
      string temp, *in;
      char str[1010],sm[5];
      gets(str);
      //cout<<str<<endl;
      //getline(std::cin,temp);
      in = new string(sm);
      temp = *in;
      //cout<<str<<endl;
      int smax = 0, j;
      for(j=0; str[j]!=' '; j++){
         //cout<<str[j]<<endl;
	 smax += smax*10 + str[j]-48;      
      }
      //cout<<"smax = "<<smax<<endl;
      int up = 0, need=0,k, total_need = 0;
      j++;

      for(k = 0;k<=smax;j++){
	 int next = str[j] - 48;
	 //cout<<"next ="<<next<<endl;
	 if(up >= k){
	    up += next;
	 }else{
	    need = k - up;
	    up += need + next;
	    total_need = total_need + need;
	 }
	 k++;
      }
      cout<<"Case #"<<i+1<<": "<<total_need<<endl;
   }
   return 0;
}
