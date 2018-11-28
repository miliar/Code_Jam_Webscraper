// do3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
#include <stdlib.h>
using namespace std;
#define I 2
#define J 3
#define K 4
//output stuff
int casesol[101];
int ncase;
/*
void output()
{
	for(int i=1;i<=ncase;i++)
	{
	printf("Case #%d: %d\n",i,casesol[i]);
	}
}
*/
void main()
{
		freopen("file.in", "r", stdin);
		freopen("file.out", "w", stdout);
		scanf("%d",&ncase);
		int lsize,x;
		int qns[5][5]={0,0,0,0,0,0,1,I,J,K,0,I,-1,K,-J,0,J,-K,-1,I,0,K,J,-I,-1};
		for(int j=1;j<=ncase;j++){
			string nl,l;
			l="";
			cin>>lsize;
			cin>>x;
			cin.ignore();
			getline(cin,nl);
			for(int i=0;i<x;i++)
				l+=nl;
			l+=" ";
			int i2,result;
			bool idid=false;
			bool jdid=false;
			bool kdid=false;
			replace( l.begin(), l.end(), 'i', '2');
			replace( l.begin(), l.end(), 'j', '3');
			replace( l.begin(), l.end(), 'k', '4');
			result=l[0]-'0';
			for(int i=1;i<l.length();i++){
				if(result==I && !idid) {
					result=l[i]-'0';
					idid=true;
					continue;
				}
				if(result==J && !jdid && idid) {
					result=l[i]-'0';
					jdid=true;
					continue;
				}
				if(result==K && !kdid && jdid && i==l.length()-1) {
					kdid=true;
					break;
				}
				i2=l[i]-'0';
				if(result<0)
					result=-qns[-result][i2];
				else
					result=qns[result][i2];	
			}
			if(idid && jdid && kdid)
				printf("Case #%d: YES\n",j);
			else
				printf("Case #%d: NO\n",j);
}
}
