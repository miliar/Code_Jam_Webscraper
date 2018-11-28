#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<cstring>
#include<math.h>
using namespace std;
#define DATATYPE unsigned
#define LEN 10
void strrev(char *p)
{
  char *q = p;
  while(q && *q) ++q;
  for(--q; p < q; ++p, --q)
    *p = *p ^ *q,
    *q = *p ^ *q,
    *p = *p ^ *q;
}
bool check_palindrome(DATATYPE num){
	char str1[LEN], str2[LEN];
	sprintf(str1,"%d",num);
	strcpy(str2,str1);
   	strrev(str2);
	if( strcmp(str1,str2) == 0 )
		return true;
	else
		return false;
}
DATATYPE countfairNsquare(DATATYPE A, DATATYPE B){
	DATATYPE start, end;
	start = ceil(sqrt(A));
	end = floor(sqrt(B));
	DATATYPE count=0;
	for(DATATYPE n=start;n<=end;n++){
		if(check_palindrome(n))
			if(check_palindrome(n*n))
				count++;
	}
	return count;
}
int main(){
	DATATYPE T;
	DATATYPE A,B;
	cin>>T;
	for(DATATYPE t=0;t<T;t++){
		cin>>A>>B;
		cout<<"Case #"<<t+1<<": "<<countfairNsquare(A,B)<<endl;
	}
}
