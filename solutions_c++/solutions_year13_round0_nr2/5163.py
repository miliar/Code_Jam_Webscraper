#include<iostream>
#include<stdio.h>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
#include<list>
#include <stack>

using namespace std;
void printLawnState(vector< vector<int> >lawn, int N, int M){
   for(int i=0;i<N;i++){
      for(int j=0;j<M;j++){               
         cout<<lawn[i][j]<<" ";   
      }//for j
      cout<<endl;
    }//for i
}

pair<bool, vector< vector<int> > > areAllMinInRowCol(int minI, int minJ, int rows, int cols, vector< vector<int> > lawn){
   bool allMinInRow = true;
   int min = lawn[minI][minJ];
   //check the row
   for(int i=0;i<cols;i++){
     if(!(lawn[minI][i] == min || lawn[minI][i] == -1)){
        allMinInRow = false;break;           
     }      
   }   
   //if all elements in row are min
   if(allMinInRow){
     for(int i=0;i<cols;i++){
       lawn[minI][i] = -1;      
     }
     //cout<<"allMinInRow "<<allMinInRow<<" - "<<min<<" at"<<minI<<", "<<minJ<<endl;
     //printLawnState(lawn, rows, cols);
     return make_pair(allMinInRow, lawn);
   }
   
   bool allMinInCol = true;
   //check the col
   for(int i=0;i<rows;i++){     
     if(!(lawn[i][minJ] == min || lawn[i][minJ] == -1)){
        allMinInCol = false;break;           
     }      
   }
   //if all elements in col are min
   if(allMinInCol){
     for(int i=0;i<rows;i++){
       lawn[i][minJ] = -1;      
     }     
   }
   //cout<<"allMinInCol "<<allMinInCol<<" - "<<min<<" at"<<minI<<", "<<minJ<<endl;
   //printLawnState(lawn, rows, cols);
   return make_pair(allMinInCol, lawn);
}

pair<int, int> getMinIJInTheLawn(vector< vector<int> >lawn, int N, int M){
    int min = 101, minI = 0, minJ = 0;
    for(int i=0;i<N;i++){
      for(int j=0;j<M;j++){               
         if(lawn[i][j] < min && lawn[i][j] != -1){min = lawn[i][j];minI = i;minJ = j;}    
      }//for j
    }//for i
    return make_pair(minI, minJ);              
}

int coutOfDeletedCells(vector< vector<int> >lawn, int N, int M){
    int count=0;
    for(int i=0;i<N;i++){
      for(int j=0;j<M;j++){               
         if(lawn[i][j] == -1){count++;}    
      }//for j
    }//for i
    return count;              
}

int main()
{
    long long int T=0;
    cin>>T;
    for(int z=1;z<=T;z++)
    {
       int N,M;
       cin>>N>>M;
       vector< vector<int> > lawnFinal(N);  
       for(int i=0;i<N;i++)            
                lawnFinal[i].resize(M);        
        
        int min = 101, minI = 0, minJ = 0;
        for(int i=0;i<N;i++){
           for(int j=0;j<M;j++){
               int temp;
               cin>>temp;
               lawnFinal[i][j] = temp;
               if(temp<min){min = temp;minI = i;minJ = j;}    
           }//for j
        }//for i        
        pair<bool, vector< vector<int> > >checkLawnState = areAllMinInRowCol(minI, minJ, N, M, lawnFinal);
        bool isLawnValid = checkLawnState.first;
        lawnFinal = checkLawnState.second;
        int countOfDeletedCellsFromLawn = coutOfDeletedCells(lawnFinal, N, M);
        while(isLawnValid && countOfDeletedCellsFromLawn < (N*M)){
             pair<int, int>minIndex =  getMinIJInTheLawn(lawnFinal, N, M);
             checkLawnState = areAllMinInRowCol(minIndex.first, minIndex.second, N, M, lawnFinal);
             isLawnValid = checkLawnState.first;
             lawnFinal = checkLawnState.second;
             countOfDeletedCellsFromLawn = coutOfDeletedCells(lawnFinal, N, M);                    
        }
        if(isLawnValid)
          cout<<"Case #"<<z<<": YES"<<endl;
        else
          cout<<"Case #"<<z<<": NO"<<endl;
    }//for testcase
    //int temp; cin>>temp;
    return 0;
}
