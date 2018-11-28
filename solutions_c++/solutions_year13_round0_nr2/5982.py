#include <fstream>
#include <iostream>
#include <conio.h>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int T,N,M;
    int flag,ch;
    int variety[100];
    int *row=NULL;
    int *col=NULL;
    int **lawn=NULL;
    ifstream fin("B.in");
    ofstream fout("B.out");
    vector<int> v;
    fin>>T;
    for(int i=0; i<T; i++)
    {
        for(int j=0; j<100; j++)
            variety[j]=0;
        v.clear();
        fin>>N>>M;
        lawn = new int*[N];
        row = new int[N];
        col = new int[M];
        for(int k=0; k<M; k++)
            col[k]=0;
        for(int j=0; j<N; j++)
        {
            lawn[j] = new int[M];
            row[j]=0;
            for(int k=0; k<M; k++)
            {
                fin>>lawn[j][k];
                if(variety[lawn[j][k]]==0)
                    v.push_back(lawn[j][k]);
                variety[lawn[j][k]]++;
            }
        }
        sort(v.begin(), v.end());
        for(vector<int>::iterator iter = v.begin(); iter!=v.end(); iter++)
        {
            flag=0;
            ch = *iter;
            for(int j=0; j<N; j++)
            {
                if(row[j]==1)
                    continue;
                for(int k=0; k<M; k++)
                {
                    if(col[k]==1)
                        continue;
                    if(lawn[j][k]==ch)
                    {
                        flag = 0;
                        for(int l=0; l<N; l++)
                        {
                            if(lawn[l][k]>ch)
                            {
                                flag = 1;
                                break;
                            }
                        }
                        if(!flag)
                        {
                            col[k] = 1;
                            break;
                        }
                        flag = 0;
                        for(int l=0; l<M; l++)
                        {
                            if(lawn[j][l]>ch)
                            {
                                flag = 1;
                                break;
                            }
                        }
                        if(!flag)
                        {
                            row[j] = 1;
                            break;
                        }
                        else
                        {
                            fout<<"Case #"<<i+1<<": NO"<<endl;
                            flag = 2;
                            break;
                        }
                    }
                }
                if(flag == 2)
                    break;
            }
            if(flag == 2)
                break;
        }
        if(flag != 2)
        {
            fout<<"Case #"<<i+1<<": YES"<<endl;
        }
        for(int j=0; j<N; j++)
            delete[] lawn[j];
        delete[] lawn;
        delete[] row;
        delete[] col;
    }
}
