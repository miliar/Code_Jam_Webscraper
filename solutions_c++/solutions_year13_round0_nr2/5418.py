#include <algorithm> 
#include <iostream>
#include <string>
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
using namespace std;


#include<fstream>
ifstream fin("input.txt");
ofstream fout("output.txt");

#define PB push_back  
#define MP make_pair  
#define SZ(v) ((int)(v).size())  
#define FOR(i,a,b) for(int i=(a);i<(b);++i)  
#define REP(i,n) FOR(i,0,n)  
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)  
#define REPE(i,n) FORE(i,0,n)  
#define FORSZ(i,a,v) FOR(i,a,SZ(v))  
#define REPSZ(i,v) REP(i,SZ(v))  
typedef long long ll;  

int POWR[10] = {10, 100, 1000, 10000, 100000, 1000000, 10000000};

int T[100][100];
int N, M;
int largetRow_clmIdx [100];
int largetClm_rowIdx [100];


void initRowClmArray()
{
  for (int i=0;i<100;i++)
  {
      largetRow_clmIdx[i] = 0xFFFF;
      largetClm_rowIdx[i] = 0xFFFF;
  }

}

int isRowLargest(int i, int j)
{
   if(largetRow_clmIdx[i] != 0xFFFF)
   {
      if(T[i][j] == T[i][largetRow_clmIdx[i]])
         return 1;
      else
        return 0;
   }

   for(int k=j+1;k<M;k++)
   {
      if(T[i][k] > T[i][j])
        return 0;

   }

   largetRow_clmIdx[i] = j;

   return 1;


}

int isColumnLargest(int i, int j)
{
   //cout <<  "largetClm_rowIdx[j] " <<largetClm_rowIdx[j]<<endl;

   if(largetClm_rowIdx[j] != 0xFFFF)
   {
      if(T[i][j] == T[largetClm_rowIdx[j]][j])
         return 1;
      else
        return 0;
   }

   for(int k=0;k<N;k++)
   {
      if(T[k][j] > T[i][j])
        return 0;

   }

   largetClm_rowIdx[j] = i;

   return 1;


}



void run(int casenr) {


    int i,j,k;
    int r;
    int c;

    fin >> N >> M;

    initRowClmArray();

    for(i=0;i<N;i++)
    {
      for (j=0;j<M;j++)
      {
           fin >> T[i][j];
      }
    }


    for (i=0;i<N;i++)
    {
     for (j=0;j<M;j++)
     {
        r = c = 0;
        r = isRowLargest(i,j);
        c = isColumnLargest(i,j);

      // if(i==6 & j ==1)
            //   cout << "I :: " << i << "  J ::"<<j << "   ::" ;
             //  cout << "R :: " << r << "  C ::"<<c <<endl;


       if(!(r||c))
        {
                fout <<"Case #"<<casenr<<": NO"<<endl;
                return;

        }
      }
     }

      fout <<"Case #"<<casenr<<": YES"<<endl;
        return;

}

int main() {
   	int n;
    //scanf("%d",&n);
    fin >> n;
    FORE(i,1,n) run(i);



    system("PAUSE");
	return 0;
}
