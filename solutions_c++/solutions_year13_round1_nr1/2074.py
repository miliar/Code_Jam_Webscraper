// Bullseye.cpp : Defines the entry point for the console application.
//
// my.cpp : Defines the entry point for the console application.
//
//#define BBB a
#include "stdafx.h"
#pragma once
#include <stdio.h>
#include <tchar.h>
#include <SDKDDKVer.h>
#include <math.h>
#include <iostream>
#include <math.h>
#include <cmath>


#define _USE_MATH_DEFINES
using namespace std;

int main()
{
	int a;

	FILE *ifptr,*ofptr;
	ofptr = fopen("A-small-attempt0-op.TXT","w"); /* open for writing */
	ifptr = fopen("A-small-attempt0.in","r");
	 
	int T,i,j,k,flag=0,caseno=0;
	int r,t;
	int ctr =0;
	int bring=0;
const double PI = 4.0*atan(1.0);	
	int arr[12][12];
	char temp[16];

	a = getc(ifptr) ;

   while (a!= EOF)
   {
	   i=0;
	   while(a!=' ' && a!='\n')
		   {
			   temp[i++]=a;
			   a = getc(ifptr);
			}
	T=atoi(temp);
	cout<<"T= "<<T<<"\n";
	while(T--)
	{
		ctr=0;
		a = getc(ifptr);
		i=0;
		while(a!=' ' && a!='\n')
		   {
			   temp[i++]=a;
			   a = getc(ifptr);
			}
		temp[i]='\0';
		r=atoi(temp);
		cout<<"r="<<r;
		
		a = getc(ifptr);
		i=0;
		while(a!=' ' && a!='\n' &&a!=EOF)
		   {
			   temp[i++]=a;
			   a = getc(ifptr);
			}
		temp[i]='\0';
		t=atoi(temp);
		cout<<"\t t ="<<t;
		
		double area;
		double tt = t;
		bring = r;
		while(1)
		{
		//area = PI*(((bring+1)*(bring+1))-((bring)*(bring)));
			area = (((bring+1)*(bring+1))-((bring)*(bring)));
		if(tt>=area)
			{
			ctr++;
			bring+=2;
			(tt)-=area;

			}
		else 
			break;
		}
		cout<<"\t ans = "<<ctr<<'\n';		
	fprintf(ofptr,"Case #%d: %d \n",++caseno,ctr);
	}
	a = getc(ifptr);
   
   }

	fclose(ofptr);
	fclose(ifptr);
//#endif	
	//cout<<"\n press any key to exit";
	//cin>>a;
	return 0;
}