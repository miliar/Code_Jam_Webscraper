#include<iostream>
#include<stdio.h>

using namespace std;

int main() {
   freopen("A-large.in", "r", stdin);
   int t;
   scanf("%d\n",&t);
   for(int i = 0; i < t; i++)
   {
      char input[1020];
      gets(input);
      int sm = 0, j;
      for(j=0; input[j]!=' '; j++){
	 sm = sm*10 + (input[j]-48); 
      }
      int standing = 0, n=0,k, tn = 0;
      j++;

      for(k = 0;k<=sm;j++){
	 int next = input[j] - 48;
	 if(standing >= k){
	    standing += next;
	 }else{
	    n = k - standing;
	    standing += n + next;
	    tn = tn + n;
	 }
	 k++;
      }
      cout<<"Case #"<<i+1<<": "<<tn<<endl;
   }
   return 0;
}
