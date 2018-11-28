#include<iostream>
using namespace std;
#include<stdio.h>
#include <fstream>
#include<climits>
#include<math.h>
#include<vector>
#include<stdlib.h>

/*
1=1
i=2
j=3
k=4
*/

int table[5][5] = {{0,0,0,0,0},
                    {0,1,2,3,4},
                    {0,2,-1,4,-3},
                    {0,3,-4,-1,2},
                    {0,4,3,-2,-1}};

int8_t lookup[10001][10001];

vector<int> wrong;
long long x, length;
int t,l,curr,k,i,j,cc, index;

void makeTable(long long start, long long stop)
{
    long long mid;
    if (start==stop)
        lookup[start][stop] = table[wrong[start%l]][wrong[stop%l]];
    else
    {
        mid = floor((start+stop)/2.0);
        makeTable(start, mid);
        makeTable(mid+1,stop);

        cout<<"combining "<<start<<" : "<<stop<<endl;
        for(index = mid+1; index <= stop; index++)
        {
            lookup[start][index] = table[abs(lookup[start][index-1])][wrong[index%l]];
            if(lookup[start][index-1]<0)
                lookup[start][index] = -1*lookup[start][index];
        }
        for(index = mid; index>=start; index--)
        {
            if(lookup[index][stop]==0)
            {
                lookup[index][stop] = table[wrong[index%l]][abs(lookup[index+1][stop])];
                if (lookup[index+1][stop]<0)
                       lookup[index][stop] = -1*lookup[index][stop];
            }
        }
    }
}

int compute(long long start, long long stop)
{


    int eval = 1;
    int base = start%l;
    bool sign = 0;
    curr = 0;


    if (lookup[start][stop] != 0)
        return lookup[start][stop];

    else if(start<l*x-1 && lookup[start+1][stop]!=0) //start start+1 --------stop
    {
        eval = table[wrong[base]][abs(lookup[start+1][stop])];
        if(lookup[start+1][stop]<0)
        {
            eval = -1*eval;
        }
        lookup[start][stop] = eval;
        //cout<<"eval : "<<eval<<endl;
        return eval;

    }

    else if(stop>0 && lookup[start][stop-1]!=0) //start-----stop-1 stop
    {
        eval = table[abs(lookup[start][stop-1])][wrong[stop%l]];
        if(lookup[start][stop-1]<0)
        {
            eval = -1*eval;
        }
        lookup[start][stop] = eval;
        //cout<<"eval : "<<eval<<endl;
        return eval;
    }


    else
    {
        for(index = start; index <= stop; index++)
        {
            curr = curr%l;
            eval = table[abs(eval)][wrong[(base+curr)%l]];
            curr++;

            if(eval<0)
                sign = !sign;

            if (!sign)
                lookup[start][index]=abs(eval);
            else
                lookup[start][index]=-1*abs(eval);


        }
        //cout<<"eval : "<<(int)lookup[start][stop]<<endl;

        return lookup[start][stop];
    }
}


int main()
{

	char val;
	bool flag;
	ifstream fin("C-small-attempt0.in");
	//ifstream fin("A-large.in");
	//ifstream fin("test.txt");
	ofstream fout("output.txt");

	if(!fin.is_open())
        cout<<"file not loaded"<<endl;

	//cout<<LONG_LONG_MAX;

	fin>>t;
	cout<<t;
	//t = ((int)num-'0');

	for(int cc=1; cc<=t; cc++)
    {

        flag =0;
        fin.get(val); //next line

        fin>>l;
        fin>>x;

        cout<<"l: "<<l<<" x: "<<x<<endl;

        fin.get(val); //next line

        length = l*x;
        for(i=0; i <=length; i++)
            for(j=0; j<= length; j++)
                lookup[i][j]=0;

        for(i=0; i<l; i++)
        {
            fin.get(val);

            //cout<<"val : "<<val<<endl;

            if (val =='i')
                wrong.push_back(2);
            else if (val =='j')
                wrong.push_back(3);
            else if (val =='k')
                wrong.push_back(4);
        }

        /*makeTable(0,length);
        cout<<"done making!"<<endl;

        for(i=0; i<length-2; i++)
        {
            if(lookup[0][i]==2)
            {
                for(j=i+1; j<length-1; j++)
                {
                    //cout<<"i: "<<i<<" j: "<<j<<endl;
                    if(lookup[i+1][j]==3 && lookup[j+1][length-1]==4)
                     {
                         flag=1;
                         break;
                     }
                }
            }
            if(flag==1)
                break;
        }*/

        for(i=0; i<length-2; i++)
        {
            if(compute(0,i)==2)
            {
                for(j=i+1; j<length-1; j++)
                {
                    //cout<<"i: "<<i<<" j: "<<j<<endl;
                    if(compute(i+1,j)==3 && compute(j+1,length-1)==4)
                     {
                         flag=1;
                         break;
                     }
                }
            }
            if(flag==1)
                break;
        }

        if (flag)
            cout<<"Case #"<<cc<<": YES"<<endl<<endl;
        else
            cout<<"Case #"<<cc<<": NO"<<endl<<endl;

        if (flag)
            fout<<"Case #"<<cc<<": YES"<<endl;
        else
            fout<<"Case #"<<cc<<": NO"<<endl;

        wrong.clear();
    }
}

