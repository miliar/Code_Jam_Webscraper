//C=costof farm
//F=add rate
//X=target
//addingrate=2
#include <iostream>
#include <fstream>
#include <stdio.h>
using namespace std;
int main()
{
    ofstream fout("c:\\me2.txt");
    int i,num,j;
    cin>>num;
    double counter,timetable[100000],cost,speed,target,rate,max;
    char temp[50];
    for(i=0;i<num;i++)
    {
        max=10000;
        counter=0.0;
        rate=2.0;
        cin>>cost>>speed>>target;
        for(j=0;j<100000;j++)
        {
            timetable[j]=counter+target/rate;
            counter+=cost/rate;
            rate+=speed;
        }
        for(j=0;j<100000;j++)
        {
            if(max>timetable[j])
            max=timetable[j];
        }
        sprintf(temp, "%.7f", max);
        fout<<"Case #"<<i+1<<": "<<temp<<endl;


    }
    return 0;
}

