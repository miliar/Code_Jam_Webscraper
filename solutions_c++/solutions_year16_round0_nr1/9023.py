#include<iostream>
using namespace std;
#include<stdio.h>
#include <fstream>

int main()
{
	int t =0, val, ans, left, temp, q, j;
	bool flag;
	int arr[10];

	//ifstream fin("A-small-attempt0.in");
	ifstream fin("A-large.in");
	//ifstream fin("test.txt");
	ofstream fout("output.txt");

	fin>>t;
	for(int i=1; i<=t; i++)
    {
        left = 10; j=0;
        flag = true;

        for(int index = 0; index<10; index++)
            arr[index]=0;
        //fill(arr, arr+10, 0);
        //fin.get(val);//next line
        if(fin.eof())
            break;
        fin>>val;

        if(val==0)
            flag = false;

        while(left>0 && flag)
        {
            j++;
            temp = j*val;
            //cout<<temp<<endl;
            while(temp)
            {
                q = temp%10;
                temp /= 10;

                if(arr[q]==0)
                {
                    arr[q]=1;
                    left--;
                }


                if(j>1000)
                {
                    cout<<"overflowing..! for "<<val;
                    flag = false;
                    break;
                }
            }

        }

        if(flag)
        {
            fout<<"Case #"<<i<<": "<<j*val<<endl;
            cout<<"Case #"<<i<<": "<<j*val<<endl;
        }
        else
        {
            fout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
        }

    }

    fin.close();
    fout.close();
}
