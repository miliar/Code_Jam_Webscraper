#include<iostream>
#include<stdio.h>
#include<string>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{
    ifstream fin("A-small-attempt3.in");
    ofstream fout("output1.txt");
    int t=0,m=0;
    fin>>t;
    for(m=1;m<=t;m++)
    {
    int a,b,sum=0,count=0,flag=0,i=0;

    fin>>a>>b;
    vector<int> mote(b,0);
    for(i=0;i<b;i++)
    fin>>mote[i];
    sort(mote.begin(),mote.end());
    i=0,sum=a;
    int count1=0;
    while(1)
    {
        count1=0;
        if(sum>mote[i])
        sum=sum+mote[i];
        else
        {
            if(sum==1)
            {
                count+=(b-i);
                break;
            }
            while(sum<=mote[i])
            {sum+=(sum-1);count1++;}
            if(count1>=(b-i))
            flag=1;
            else
            {
            sum=sum+mote[i];
            count+=count1;
            }

        }

        if(flag==1)
        break;
        i++;
        if(i==b)
        break;
    }

    if(flag==1)
    count+=(b-i);
    //cout<<sum<<endl;

    fout<<"Case #"<<m<<": "<<count<<endl;
    //cout<<count1;

    }



}
