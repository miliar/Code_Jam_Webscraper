/**
*************************************************************************
* Name: Mohit Malpani
*************************************************************************
*
* Copyright 2015 by mhtmalpani
*
************************************************************************/

#include<iostream>
#include<stdlib.h>

using namespace std;

int main( void )
{
    int max_shyness[110];
    char audienceOfShyness[110][1010];
    int i,j;
    int totalAudience;
    int addedGuest;
    int testCases;
    int difference;


    freopen("A-large.in","r",stdin);

    cin>>testCases;

    for(j=0;j<testCases;j++)
    {
        cin>>max_shyness[j];

        for(i=0;i<=max_shyness[j];i++)
        {
            cin>>audienceOfShyness[j][i];
        }
    }


    for(j=0;j<testCases;j++)
    {
        totalAudience = audienceOfShyness[j][0] - '0';
        addedGuest = 0;

        for(i=1;i<=max_shyness[j];i++)
        {
            difference = i - totalAudience;

            if(audienceOfShyness[j][i]=='0')
                continue;

            if(difference > 0)
            {
                addedGuest += difference;
                totalAudience += difference;
            }

            totalAudience += audienceOfShyness[j][i] - '0';
        }

        cout<<"Case #"<<j+1<<": "<<addedGuest<<endl;
    }


	return 0;
}
