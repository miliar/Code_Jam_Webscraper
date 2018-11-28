#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    ifstream infile;
    ofstream outfile;
    infile.open("B-large.in");
    outfile.open("B-large.out");
    int T;
    int t = 0;
    int l, b;
    int** lawn;
    bool** r;
    infile >> T;
    while(t < T)
    {
            t++;
            infile >> l >> b;
            lawn = new int*[l];
            r = new bool*[l];
            for(int i = 0; i < l; i++)
            {        
                     lawn[i] = new int[b];
                     r[i] = new bool[b];
                     for(int j = 0; j < b; j++)
                     {        
                              infile >> lawn[i][j];
                              r[i][j] = false;
                     }
            }
            
            for(int i = 0; i < l; i++)
            {
                    for(int j = 0; j < b; j++)
                    {
                            bool n = true;
                            for(int k = 0; k < b; k++)
                                    if(lawn[i][j] < lawn[i][k])
                                    {             
                                                  n = false;
                                                  break;
                                    }
                            if(n == false)
                            {
                                 n = true;
                                 for(int k = 0; k < l; k++)
                                    if(lawn[i][j] < lawn[k][j])
                                    {
                                                  n = false;
                                                  break;
                                    }
                            }
                            if(n)
                                 r[i][j] = true;
                    }
            }
            
            bool n = true;
            for(int i = 0; i < l; i++)
                    for(int j = 0; j < b; j++)
                    {
                            if(r[i][j] == false)
                            {
                                       n = false;
                                       break;
                            }
                    }
            if(n == false)
            {
                outfile << "Case #" << t << ": NO" << endl; 
            }
            else
            {
                outfile << "Case #" << t << ": YES" << endl;
            }
                                                       
            for(int i = 0; i < l; i++)
            {
                    delete [] lawn[i];
                    delete [] r[i];
            }
            delete [] lawn;
            delete [] r;
    }
    return 0;
}
