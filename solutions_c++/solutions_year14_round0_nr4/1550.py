//
//  main.cpp
//  jam3
//
//  Created by Vipul Verma on 12/04/14.
//  Copyright (c) 2014 Vipul Verma. All rights reserved.
//

#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
	int t,n,i,j,x,y,k=1;
	float naomi[1000],ken[1000];
	FILE *fin=fopen("D-large.in","r");
    FILE *fout=fopen("D-large.out","w");
    fscanf(fin,"%d",&t);
    while(t--)
    {
        fscanf(fin,"%d",&n);
    	for(i=0;i<n;i++)
    	{
    		fscanf(fin,"%f",&naomi[i]);
    	}
    	for(i=0;i<n;i++)
    	{
    		fscanf(fin,"%f",&ken[i]);
    	}
    	sort(naomi,naomi+n);
    	sort(ken,ken+n);
    	y=0;
    	i=0,j=0;
    	while(i<n)
    	{
    		if(naomi[i]>ken[j])
    		{
    			j++;
    			y++;
    		}
    		i++;
    	}
    	i=0,j=0;
    	x=0;
    	while(i<n)
    	{
    		if(j==n)
    			break;
    		if(naomi[i]<ken[j])
    		{
    			x--;
    			i++;
    		}
    		j++;
    	}
    	x+=n;
    	fprintf(fout,"Case #%d: %d %d\n",k,y,x);
    	k++;
    }
	return 0;
}