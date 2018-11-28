#include <iostream>
#include <fstream>
#include <string.h>
#include <stdlib.h>
//1=o,-1=m
using namespace std;

char multiply(char c1,char c2,int *x)
{
	switch(c1)
	{
		case 'o':
		{switch(c2){
			case 'o': return 'o';
			case 'i': return 'i';
			case 'j': return 'j';
			case 'k': return 'k';
		}}
		case 'i':
		{switch(c2){
			case 'o': return 'i';
			case 'i': *x=!*x;return 'o';
			case 'j': return 'k';
			case 'k': *x=!*x;;return 'j';
		}}
		case 'j':
		{switch(c2){
			case 'o': return 'j';
			case 'i': *x=!*x;return 'k';
			case 'j': *x=!*x;return 'o';
			case 'k': return 'i';
		}}
		case 'k':
		{switch(c2){
			case 'o': return 'k';
			case 'i': return 'j';
			case 'j': *x=!*x;return 'i';
			case 'k': *x=!*x;return 'o';
		}}
	}
}

int main()
{
	char *c,*tempc,nchar,nstring[4];
	ifstream fi;
	ofstream fo;
	fi.open("input.in");
	fo.open("ouput1.txt");
	int testc,neg=0;
	int slen,x,n,j;
	fi>>testc;
	for(int i=0;i<testc;i++)
	{
		neg=0;
		strcpy(nstring,"ooo");
		fi>>slen>>x;
		n=slen*x;
		//cout<<"n="<<n<<endl;
		c=(char*)malloc((n+2)*sizeof(char));

		tempc=(char*)malloc((slen+1)*sizeof(char));
		fi>>tempc;
		strcpy(c,tempc);
		for(j=0;j<x-1;j++)
			strcat(c,tempc);
		c[n]='o';c[n+1]='\0';
		//cout<<c<<endl;
		j=0;
		nchar=c[0];
		while(j<=n-1)
		{
			if(nchar=='i')
				{
					j++;
					nstring[0]=nchar;
					break;
				}

			nchar=multiply(nchar,c[j+1],&neg);
			//cout<<neg<<endl;
			j++;
		}
		/*if(j==n-1&&nchar!='i')
		{
			if(c[j]=='i')
				nchar='i';
		}*/

		//cout <<j<< " "<<nchar;
		//int m=j;
		//cout<<" MMMMMMMMMMMMMM"<<m<<" ";
		nchar=c[j];
		while((j<=n-1))
		{
			if(nchar=='j')
				{
					j++;
					nstring[1]=nchar;
					break;
				}
			nchar=multiply(nchar,c[j+1],&neg);
			//cout<<neg<<endl;
			j++;
		}
		//cout << nchar;




		nchar=c[j];
		while((j<=n-1))
		{
			//cout<<"hi"<<j<<endl;
			/*if(nchar=='k')
				{
					j++;
					nstring[2]=nchar;
					break;
				}*/
			nchar=multiply(nchar,c[j+1],&neg);
			//cout<<neg<<endl;
			j++;
		}
		//cout << ncharr<<endl;
		if(nchar=='k')
				{
					j++;
					nstring[2]=nchar;
				}

		cout<<neg<<" "<<nstring<<endl;
		fo<<"Case #"<<i+1<<": ";
		if((!neg)&&(!strcmp(nstring,"ijk")))
			fo<<"YES";
		else
			fo<<"NO";
		fo<<endl;

		free(c);
		free(tempc);
	}
	fi.close();
	fo.close();
	return 0;
}
