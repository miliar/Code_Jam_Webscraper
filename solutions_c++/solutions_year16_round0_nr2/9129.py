#include<iostream>
using namespace std;
#include<stdio.h>
#include <fstream>

int main()
{
	int t =0,j, val, flip=0;
	string line;
	bool flag;

	//ifstream fin("B-small-attempt0.in");
	ifstream fin("B-large.in");
	//ifstream fin("test.txt");
	ofstream fout("output.txt");

	fin>>t;
	getline(fin,line);
	for(int i=1; i<=t; i++)
    {
        flip = 0;
        //fin.get(val);//next line
        if(fin.eof())
            break;
        getline(fin,line);

        j = line.length()-1;

        while(line[j]=='+')
            j--;

        while(j>=0)
        {
            if(line[j]=='+')
            {
               while(line[j]=='+')
                    j--;
                flip++;
            }

            if(line[j]=='-')
            {
               while(line[j]=='-')
                    j--;
                flip++;
            }

        }

        fout<<"Case #"<<i<<": "<<flip<<endl;
        cout<<"Case #"<<i<<": "<<flip<<endl;

    }

    fin.close();
    fout.close();
}
