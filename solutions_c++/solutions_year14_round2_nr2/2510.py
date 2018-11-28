#define _for(x) for(int _i=0; _i <x ; _i++)    //for making x iterations
#define afor(a,x,v) for(int i=0; i<x; a[i]=v,i++)//For putting specific value in an array
//a=array, x= iterations, v= specific value to be inserted

#include<iostream>
#include<string>
#include<fstream>
#include<iomanip>
#include<conio.h>
#include<vector>

using namespace std;

int main()
{
    ifstream fin;
    fin.open("input.txt",ios::in);
    ofstream fout;
    fout.open("output.txt",ios::out);
    int T;
    fin>>T;

    long long  a,b,k,ct,i,j,g;

    _for(T)
    {
        fin>>a>>b>>k;
        ct = 0;

        for(i=0;i<a;i++) for(j=0;j<b;j++)
        {
            g = i & j;
            if(g<k)
            {
                ct ++;
                //cout<<g<<" ";
            }
        }


        fout<<"Case #"<<_i+1<<": "<<ct<<endl;
       //getch();
    }
}
