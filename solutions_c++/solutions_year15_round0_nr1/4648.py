#include <iostream>
#include <cstdio>
#include <algorithm>
#include <fstream>

using namespace std;

int main()
{
    ofstream outfile("output.in");
    ifstream infile("A-large.in");
    int i,j,t,sm,current,people_count,count; //sm for s max, current for current shyness level
    char ch;
    while(infile)
    {
    infile>>t;
    infile.get(ch);
    for(i=1;i<=t;i++)
    {
        infile>>sm;
        infile.get(ch);
        people_count=0;
        count=0;
        for(j=0;j<=sm;j++)
        {

            infile.get(ch);
            current=ch-'0';
            people_count+=current;
            if(current==0)
            {
                if(j>=people_count)
                    {
                        people_count++;
                        count++;
                    }
            }
        }
        infile.get(ch);
        outfile<<"Case #"<<i<<": "<<count<<endl;
    }
        outfile.close();
    }

    return 0;
}
