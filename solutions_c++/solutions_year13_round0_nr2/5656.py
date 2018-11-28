#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
using namespace std;


int findMin(int a[], int size)
{
  int res = 9999;
  for(int i = 0; i < size; i++)
  {
    if(a[i] < res)
    {
      res = a[i];
    }
  }
  return res;
}

bool allEqual(int a[], int size, int e)
{
  for(int i = 0; i < size; i++)
  {
    if(a[i] != e)
      return false;
  }
  return true;
}


int main()
{
  int nCase;
  string inputFileName = "input.txt";
  string outputFileName = "output.txt";
  ifstream infile;
  ofstream ofile;

  //Loading information
  infile.open(inputFileName.c_str());
  ofile.open(outputFileName.c_str());
  if (!infile.is_open())
  {
    cout <<"Unable to open file \""<< inputFileName.c_str() << "\"."<<endl;
    exit(1);
  }

  infile >> nCase;
  //char sstring[100];
  //infile.getline(sstring, 100);

  for(int numCase = 0; numCase < nCase; numCase++)
  {
    cout<<"Case #"<<numCase + 1<<""<<": ";
    ofile << "Case #"<<numCase + 1<<""<<": ";

    int N,M;
    bool flag = false;
    infile >> N;
    infile >> M;

    int** map = new int*[N];
    for(int i = 0; i < N; ++i)
      map[i] = new int[M];

    for(int i = 0; i < N; i++)
    {
      for(int j = 0; j < M; j++)
      {
        infile >> map[i][j];
      }
    }



    for(int i = 0; i < N; i++)
    {
      int minElem = findMin(map[i], M);
      if(allEqual(map[i], M, minElem))
      { // All equal elements, legal
        continue;
      }
      for(int j = 0; j < M; j++)
      {
        if(minElem == map[i][j])
        {
          for(int k = 0; k < N; k++)
          {
            if(map[k][j] > minElem)
              flag = true;
          }
        }
        
      }
      
    }

    
    
    
    if(!flag)
    {
      cout<<"YES"<<endl;
      ofile<<"YES"<<endl;
    }
    else
    {
       cout<<"NO"<<endl;
       ofile<<"NO"<<endl;
    }
    
    for(int i = 0; i < N; ++i)
      delete [] map[i];
    delete [] map;


  }
  infile.close();
  ofile.close();
  return 0;
}