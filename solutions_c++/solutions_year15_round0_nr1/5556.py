#include<iostream>
using namespace std;
#include<stdio.h>
#include <fstream>

int main()
{
	int t =0,j,k, friends, total, S;
	char num;
	ifstream fin("A-small-attempt1.in");
	//ifstream fin("test.txt");
	//fin >> t;
	ofstream fout("output.txt");

	//fin.get(num);
	fin>>t;
	//t = ((int)num-'0');

	for(int i=1; i<=t; i++)
    {

        fin.get(num);//next line
        if(fin.eof())
            break;

        friends =0;
        total = 0;

        fin>>j;
        /*fin.get(num);
        j =((int)num-'0');*/
        cout<<j<<endl;
        fin.get(num);// space

        for(k=0;k<=j;k++)
        {
            fin.get(num);
            cout<<(int)num-'0'<<endl;

            if (k> total && ((int)num-'0')!=0)
            {
                friends += (k-total);
                total += friends;
            }
            total+=((int)num-'0');
            //cout<<"friends : "<<friends<<endl;
            //cout<<"total : "<<total<<endl;
        }

        fout<<"Case #"<<i<<": "<<friends<<endl;
        cout<<"Case #"<<i<<": "<<friends<<endl;
    }

    fin.close();
    fout.close();
}
