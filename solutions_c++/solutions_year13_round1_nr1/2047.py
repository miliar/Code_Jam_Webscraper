#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

int loadFile (unsigned long long int t[1000], unsigned long long int r[1000])
{
	int numberOfCases=0;

	ifstream fs ("input.in");
	if (fs.is_open())
	{
		fs >> numberOfCases;

		for (int i=0; i<numberOfCases; i++)
		{
			fs >> r[i] >> t[i] ;
		}
	}
	else
		printf ("Error opening/creating file");
	fs.close();

	return numberOfCases;
}

void saveFile (unsigned long long int result, int caseNumber)
{
	ofstream fs ("output.txt", ios::app);

	if (fs.is_open())
	{
		fs << "Case #" << caseNumber + 1 << ": " << result << endl;
	}
	else
		printf ("Error opening/creating file");
	fs.close();
}

int main(void)
{

    unsigned long long int t[1000], r[1000], counter;
    int numberOfCases = loadFile(t, r), i,j,k;

    for(i=0;i<numberOfCases;i++)
    {
        counter=0;
        printf("%d", i);
        do
        {
            if((long long int)(t[i]-(2*r[i]+1))>0)
            {
                counter++;
                t[i]-=(2*r[i]+1);
                r[i]+=2;

            }
            else if((long long int)(t[i]-(2*r[i]+1))==0)
            {
                t[i]=0;
                counter++;
            }
            else
            {
                t[i]=0;
            }
        }while(t[i]!=0);

        saveFile(counter, i);
    }

    system("PAUSE");
}
