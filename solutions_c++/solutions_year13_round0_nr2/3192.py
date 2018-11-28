 /* Copyright NTU GIEE 2012. All Rights Reserved. */
 /* =====================================================================================
 *       Filename:  B.cpp
 *    Description:  
 *        Created:  04/14/2012 12:42:55 PM CST
 *         Author:  Bo-Han Gary Wu (NTU GIEE), researchgary@gmail.com
 * ===================================================================================== */

#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <cassert>
#include <vector>
#include <algorithm>

using namespace std;

int getSmallest(const vector<vector<int> >& L){
   int smallest = 1000;
   for ( uint32_t j = 0 ; j < L.size() ; ++j ){
      for ( uint32_t k = 0 ; k < L[j].size() ; ++k ){
         if ( smallest > L[j][k] )
            smallest = L[j][k];
      }
   }
   return smallest;
}

bool check(const vector<vector<int> >& L, int x, int y, int smallest, vector<vector<bool> >& state){
   int path = false;
   int nS = 0;
   for ( uint32_t k = 0 ; k < L[x].size() ; ++k ){
      nS += (L[x][k]==smallest);
   }
   path = (nS==L[0].size());
   if ( nS == L[0].size() )
      for ( uint32_t k = 0 ; k < L[x].size() ; ++k )
         state[x][k]=true;

   nS = 0;
   for ( uint32_t j = 0 ; j < L.size() ; ++j ){
      nS += (L[j][y]==smallest);
   }
   path = path || (nS==L.size());
   if ( nS == L.size() )
      for ( uint32_t j = 0 ; j < L.size() ; ++j )
         state[j][y]=true;

   return path;
}

void updateL(vector<vector<int> >& L, int from, int to){
   for ( uint32_t i = 0 ; i < L.size() ; ++i ){
      for ( uint32_t j = 0 ; j < L[i].size() ; ++j ){
         if ( L[i][j] == from )
            L[i][j] = to;
      }
   }
}

int main(int argc, char* argv[]){
   ifstream ifile(argv[1]);
   if ( argc != 2 ){
      cout << "Error" << endl;
      return 0;
   }

   ofstream ofile("B.out");
   int T;
   ifile >> T;
   for ( uint32_t i = 0 ; i < T ; ++i ){
      int N, M;
      ifile >> N >> M;
      vector<vector<int> > L(N);
      vector<int> sortL;
      for ( uint32_t j = 0 ; j < N ; ++j ){
         for ( uint32_t k = 0 ; k < M ; ++k ){
            int n; ifile >> n;
            L[j].push_back(n);
            sortL.push_back(n);
         }
      }
      std::sort(sortL.begin(),sortL.end());

      int index = 0;
      while (1){
         int smallest = sortL[index]; 
         vector<vector<bool> > state(L.size());
         for( uint32_t j = 0 ; j < L.size() ; ++j){
            for ( uint32_t k = 0 ; k < L[j].size() ; ++k ){
               state[j].push_back(false);
            }
         }
         bool rst = true;
         for( uint32_t j = 0 ; j < L.size() ; ++j){
            for ( uint32_t k = 0 ; k < L[j].size() ; ++k ){
               if ( L[j][k] == smallest && state[j][k]==false ){
                  rst = check(L,j,k,smallest,state);
                  if ( !rst )
                     break;
               }
            }
            if ( !rst )
               break;
         }
         if ( !rst ){ // NO
            ofile << "Case #" << i+1 << ": NO" << endl;
            cout << "Case #" << i+1 << ": NO"  << endl;
            break;
         }
         ++index;
         if ( index == sortL.size() ){
            //YES
            ofile << "Case #" << i+1 << ": YES" << endl;
            cout << "Case #" << i+1 << ": YES"  << endl;
            break;
         }else{
            updateL(L,smallest,sortL[index]);
         }
      }
   }

   ofile.close();
   ifile.close();
   return 0;
}
