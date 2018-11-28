#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#define SIZE 10
using namespace std;
int main()
{
 int T, w, detect; 
 ifstream input;
 ofstream output;
 input.open("B-small-attempt3(1).in");
 output.open("output.txt");
 input >> T;
 for(w=1;w<=T; w++)
  {
    int Matrix[SIZE][SIZE] = {0};
    vector<int> index_min_x;
    vector<int> index_min_y;
    int N,M,x;
    int i,j, min;
    int sz = 0;
    input >> N;
    input >> M;
    for(i=0; i<N; i++)
      for(j=0; j<M; j++)
       {
        input >> x;
        Matrix[i][j] = x;
       }
      if(M == 1 || N == 1)
      {
        detect = 1;
      }
      else
      {
    min  = Matrix[0][0];
    for(i=0; i<N; i++)
       for(j=0; j<M; j++)
          {
            if(Matrix[i][j] < min)
                min = Matrix[i][j];
           }
     for(i=0; i<N; i++)
       for(j=0; j<M; j++)
          {
            if(Matrix[i][j] == min)
              {
                index_min_x.push_back(i);
                index_min_y.push_back(j);
              }
          }
       sz = index_min_x.size();
      detect = 0;
      for(i=0; i<sz; i++)
         {
           int row = index_min_x[i];
           int col = index_min_y[i];
           int row_count = 0;
           int col_count = 0;
           int k = 0;
           for(k=0; k<M; k++)
             {
               if(Matrix[row][k] == min)
                 row_count++;
               else{ 
                  row_count = 0;
                  break;}
             }

           for(k=0; k<N; k++)
            {
              if(Matrix[k][col] == min)
                col_count++;
              else{
               col_count = 0;
               break;}
            }
   if((row_count == M && col_count == 0) || (col_count == N && row_count == 0))
             detect = 1;
     else if((row_count == M && row == 0) || (row_count == M && row == N-1))
       {
         detect = 1;
       }
           else if(col_count == N && (col == 0 || col == M-1))
         detect = 1;
           else if(col_count == N)
            {
             int j;
             int count_sub;
             for(j=0; j<N-1; j++)
              {
               count_sub = 0;
              for(k=0; k<M; k++)
                 {
                   if(Matrix[j][k] == min)
                      count_sub++;
                   else
                      break; 
                 }
               }
                if(count_sub == M)
                 detect = 1;
             }
           else if(row_count == M)
            {
             int j;
             int count_sub;
             for(j=0; j<M-1; j++)
              {
               count_sub = 0;
              for(k=0; k<N; k++)
                 {
                   if(Matrix[k][j] == min)
                      count_sub++;
                   else
                      break;
                 }
               }
                if(count_sub == N)
                 detect = 1;
            }
      
       else if(row_count == M && col_count == N)
             {
               detect = 1;
              }
             else
             {
       
              detect = 0;
              break;}
          
         }
     } 
      if(detect == 1)
      output << "Case #" << w << ": " << "YES" << endl;
      else
       output << "Case #" << w<< ": " << "NO" << endl;
    
  } 
  input.close();
  output.close();
 return 0;
}
