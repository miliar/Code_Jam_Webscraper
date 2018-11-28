#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include <iterator>

#include<ctype.h>

#include <algorithm>
#include <iomanip>

#include <string>
#include <sstream>

#include<cstring>
using namespace std;
int main() {
	char p[1000];

	FILE *f = fopen("in2.txt", "r");
    FILE *f1 = fopen("out_2.txt", "w");
    int l=0,i,ii,s,j,num;

  fscanf(f, "%d",&num);


    for (ii=0; ii<num; ii++)
	{

    	s=0;

        fscanf(f,"%s",&p);

    l=strlen(p);


    for(i=l-1;i>=0;i--)
	{
		if (p[i]=='-')
            {
            s++;
            for(j=i;j>=0;j--)
            {
            if(p[j]=='-')
                p[j]='+';


          else
                p[j]='-';


            }


		}}
fprintf(f1,"Case #%d: %d \n", ii+1,s);



 }
    return 0;
}

