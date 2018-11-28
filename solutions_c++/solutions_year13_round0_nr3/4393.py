#include<iostream>
#include<stdio.h>
#include<string>
#include<fstream>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
using namespace std;

bool is_fair(int num)
{
	int m = 0, j=0;
	m = num;
	while(m)
	{
		j = j*10 + m%10;
		m = m/10;
	}

	if (j == num)
	{return true;}
	return false;
}


int main()
{
    ifstream infile;
    infile.open("C-small-attempt0.in", ifstream::in);
    ofstream outfile;
    outfile.open("C-small-attempt0.out", ofstream::out);


     int T, A, B, result;
     char line[10001];
     if (!infile.is_open())
    {
        cout<<"Failed open file"<<endl;
        return 0;
    } 

    infile.getline(line,10001);
    sscanf(line, "%d", &T);
    cout<<T<<endl;

    float rootlow, roothigh;
    int lowint, highint;
    int cursquare = 0;
	char *infosplits;

    for (int l=0; l<T; l++)
    {
        infile.getline(line,10001);
        infosplits = strtok(line, " "); 
        sscanf(infosplits, "%d", &A);
        infosplits = strtok(NULL, " "); 
        sscanf(infosplits, "%d", &B);
		//cout<<A<<" "<<B<<endl;

        // now find the num
        rootlow = sqrt((float)A);
        roothigh = sqrt((float)B);
        lowint = (int) rootlow;
        highint = (int) roothigh;
		//cout<<lowint<<" "<<highint<<endl;
		result = 0;
        for (int i = lowint; i<highint+1; i++)
        {
        	if (is_fair(i))
        	{
        		cursquare = i*i;
				if ((cursquare >= A) &&(cursquare <= B))
				{
        			if (is_fair(cursquare))
        			{
        				result++;
        			}
				}
        	}
        }
        outfile<<"Case #"<<l+1<<": "<<result<<"\n";

    }
    infile.close();
    outfile.close();
    return 0;
}