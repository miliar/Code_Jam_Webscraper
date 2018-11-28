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
    int i,j,k,m,n,p,q,s,t;
    ifstream myfile;
    myfile.open("/Users/jigyayadav/Downloads/D-large.in-2.txt");
    ofstream outfile;
    outfile.open("/Users/jigyayadav/Downloads/outFileLarge5.txt");
    myfile>>t;
    vector<double> ken(1100);
    vector<double> naomi(1100);
    vector<bool> ken1(1100);
    vector<bool> naomi1(1100);
    int deceit, fair, flag;
    for(s=1;s<=t;s++)
    {
        deceit=0;
        fair=0;
        myfile>>n;
        for(i=0;i<n;i++)
        {
            myfile>>naomi[i];
        }
        for(i=0;i<n;i++)
        {
            myfile>>ken[i];
        }
        outfile.precision(4);
        outfile.setf(ios::fixed, ios::floatfield );
        sort(naomi.begin(), naomi.begin()+n);
        sort(ken.begin(), ken.begin()+n);
        fill(ken1.begin(), ken1.begin()+n+5, false);
        fill(naomi1.begin(), naomi1.begin()+n+5, false);
        
        //Fair War Output
        for(i=0;i<n;i++)
        {
            flag=0;
            for(j=0;j<n;j++)
            {
                if(ken1[j]==false && ken[j]>naomi[i])
                {
                    ken1[j]=true;
                    flag=1;
                    break;
                }
            }
            if(flag==0)
            {
                fair++;
                for(j=0;j<n;j++)
                {
                    if(ken1[j]==false)
                    {
                        ken1[j]=true;
                        break;
                    }
                }
            }
        }
        
        
        fill(ken1.begin(), ken1.begin()+n+5, false);
        fill(naomi1.begin(), naomi1.begin()+n+5, false);

        
        //Deceitful War Output
        
        for(i=n-1;i>=0;i--)
        {
            flag=0;
            for(j=0;j<n;j++)
            {
                if(naomi1[j]==false && ken[i]<naomi[j])
                {
                    naomi1[j]=true;
                    flag=1;
                    break;
                }
            }
            if(flag==0)
            {
                for(j=0;j<n;j++)
                {
                    if(naomi1[j]==false)
                    {
                        naomi1[j]=true;
                        break;
                    }
                }
            }
            else
            {
                deceit++;
            }
        }
        outfile<<"Case #"<<s<<": "<<deceit<<" "<<fair<<endl;
    }
    myfile.close();
    outfile.close();
    return 0;
}