#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cassert>
using namespace std;

int main()
{   
    FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-large.out", "w", stdout);
    int testcases=0;
    //cout<<"enter num of test cases"<<endl;
    cin>>testcases;
    int t=1;
    while(testcases !=0)
    {
    
    int num=0;
    int array[10]={0,0,0,0,0,0,0,0,0,0};
    //cout<<"enter the number N"<<endl;
    cin>>num;
    
    cout<<"Case #"<<t<<": ";
    bool flag = true;
    int i = 1;
    int score =0;
    if(num == 0)
    {
        flag= false;
        //m<<"INSOMNIA"<<endl;    
        cout<<"INSOMNIA"<<endl;
        
    }
    while(flag == true)
    {   score=i*num;
        //cout<<score<<endl;
        int y = score;
        while(score)
        {
            array[score%10]=1;
            //printf("%d\n", score % 10);
            score /= 10;
        }
        i++;
        int x=3;
        for(int j=0;j<10;j++)
        {
            x=x*(array[j]);
            
        }
        if(x != 0)
        {
            flag=false;
            cout<<y<<endl;
            //myfile<< y <<endl;
        }
    }
        testcases--;
        t++;
    }
    exit(0);
}