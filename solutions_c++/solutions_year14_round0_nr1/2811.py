#include <iostream>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <map>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <fstream>

using namespace std;
int fastread()
{
    int input;
    char c=0;
    while (c<33) c=getchar();
    input=0;
    while (c>33)
    {
        input=input*10+c-'0';
        c=getchar();
    }
    return input;
}


int main()
{
    int i,j,k,a,b;
    vector< vector<int> > arr1( 10, vector<int> (10) );
    vector< vector<int> > arr2( 10, vector<int> (10) );
    ifstream myfile;
    myfile.open("/Users/jigyayadav/Downloads/A-small-attempt0.in.txt");
    ofstream outfile;
    outfile.open("/Users/jigyayadav/Downloads/outFile1.txt");
    int t,s,cnt,ans;
    myfile>>t;
    for(s=1;s<=t;s++)
    {
        cnt=0;
        myfile>>a;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                myfile>>arr1[i][j];
            }
        }
        myfile>>b;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                myfile>>arr2[i][j];
            }
        }
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(arr1[a][i]==arr2[b][j])
                {
                    cnt++;
                    ans=arr1[a][i];
                }
            }
        }
        if(cnt==1)
        {
            outfile<<"Case #"<<s<<": "<<ans<<endl;
        }
        else if(cnt>1)
        {
            outfile<<"Case #"<<s<<": Bad magician!"<<endl;
//            printf("Case %d: Bad magician!", s);
        }
        else if(cnt==0)
        {
            outfile<<"Case #"<<s<<": Volunteer cheated!"<<endl;
//            printf("Case %d: Volunteer cheated!", s);
        }
    }
    myfile.close();
    outfile.close();
    return 0;
}