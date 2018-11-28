#include <fstream>
#include <iostream>
#include <string>
using namespace std;
int getCell(int i, int j, int N, int *b)
{
    return b[N*i+j];
}

bool isPatternValid(int M, int N, int *b)
{
    int *maxR = new int[M];
    int *maxC = new int[N];

    for(int i = 0; i < M; ++i)
    {
        maxR[i] = getCell(i,0,N,b);
        for (int j = 0; j < N; ++j)
        {
            if(maxR[i] < getCell(i,j,N,b))
            {
                maxR[i] =  getCell(i,j,N,b);
            }
        }
    }
    for(int j = 0; j < N; ++j)
    {
        maxC[j] = getCell(0,j,N,b);
        for (int i = 0; i < M; ++i)
        {
            if(maxC[j] < getCell(i,j,N,b))
            {
                maxC[j] =  getCell(i,j,N,b);
            }
        }
    }

    for(int i=0; i<M; ++i)
    {
        for(int j=0; j<N; ++j)
        {
            int val = getCell(i,j,N,b);
            if(val < maxR[i] && val <maxC[j])
            {
                delete [] maxR;
                delete [] maxC;
                return false;
            }
        }
    }
    delete [] maxR;
    delete [] maxC;

    return true;
}

int main()
{
   string line;
   int numberOfTC;   
   if (true)
   {
       int M, N;
       
       cin >> numberOfTC;
       for(int k=1; k<=numberOfTC; ++k)
       {
           cin >> M;
           cin >> N;
           int *b = new int [M*N];
           for(int i =0; i < M; ++i)
           {
               for (int j=0; j < N; ++j)
               {
                    cin >> b[N*i+j];
               }
           }
           if(isPatternValid(M,N,b))
           {
               cout << "Case #" << k << ": YES" << std::endl;
           }
           else
           {
               cout << "Case #" << k << ": NO" << std::endl;
           }
       }
   }
   return 0;
}

