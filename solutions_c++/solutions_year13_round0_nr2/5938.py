#include <iostream>
#include <fstream>
#include <stdlib.h>
using namespace std;



bool check(int *tab, int N, int M);

int main()
{
    fstream fp, fpOut;
    fp.open("B-small-attempt2.in");
    //fp.open("A-large.in");
    fpOut.open("output.out");
    if (!fp.is_open()) {
     exit(1);
     }

	if (!fpOut.is_open()) {
     exit(1);
     };
	int T, N, M;
	string line, pom;
	getline(fp, line);
	T = atoi(line.c_str());





    for (int t = 0; t<T; t++)
    {
        bool result=true;
        int c,d;
        getline(fp, line);
        for(c=0; line[c]!=' '; c++);
        pom = line.substr(0,c);
        N = atoi(pom.c_str());


        for(d=c; line[d]!='\0'; d++);
        pom = line.substr(c,d-c);
        M = atoi(pom.c_str());


        int tab[N][M];

                int pocz = 0;
        for(int i=0; i<N; i++)
        {
            getline(fp,line);
           // for(int l=0; l<line.length(); l++) cout<<line[l];
                int k=0;
                for(int j=0; j<M; j++)
                {
                   while(line[k]==32) k++;
                   tab[i][j]=line[k];

                   k++;
                }

        }

        int count = 0;
        if (N<=1 || M<=1) 	    result = true;
        else
        {
            for (int i = 0; i<N; i++)
            {
                count = 0;
                for (int j = 0; j<M-1; j++)
                {

                    if(tab[i][j]>tab[i][j+1])
                    {

                        if(result==false) break;

                        for(int k = 0; k<N-1; k++)
                        {

                        if(tab[k][j+1]!=tab[k+1][j+1])
                        {


                            result = false;
                            break;
                        }
                        }
                        count = j+1;
                    }
                    else if (tab[i][j]<tab[i][j+1])
                    {

                        if(result==false) break;

                        for(int m=count; m<=j; m++)
                        for(int k = 0; k<N-1; k++)
                        if(tab[k][m]!=tab[k+1][m])
                        {

                            result = false;
                            break;
                        }
                    }
                }
            }

        }
        //cout<<t+1<<")"<<result<<endl;
        if (result==true) fpOut<<"Case #"<<t+1<<": YES"<<endl;
        else fpOut<<"Case #"<<t+1<<": NO"<<endl;
    }
    fp.close();
    fpOut.close();
    return 0;
}




