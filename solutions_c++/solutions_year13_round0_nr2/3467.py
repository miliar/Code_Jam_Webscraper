#include <iostream>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int main()
{
  int T;
 ofstream output_large ("out_large.txt");
 ifstream given_input("A-small-attempt0.in");
 given_input >> T;
int m, n;
 bool break_loops = false;

   for(int tc_count=1; tc_count<= T; tc_count++){
 //fetch data_input
       given_input >>n>>m;
      int** lawn_square = new int*[n];
 for(int i=0; i<n; i++){
       lawn_square[i]= new int[m];
       for(int j=0; j<m; j++){
           given_input >> lawn_square[i][j] ;
           cout <<i <<" " << j << "  =  " << lawn_square[i][j]<<endl;
        }

   }

   //Analysis

   for(int i=0; i<n; i++){
      for(int j=0; j<m; j++){
        //  cout <<i <<"   " << j << "=" << lawn_square[i][j]<<endl;
          for(int k=0; k<m; k++){
              if(lawn_square[i][j] < lawn_square[i][k]){
                  for(int l=0; l<n; l++){
                      if(lawn_square[i][j] < lawn_square[l][j]){
                          output_large << "Case #"<< tc_count <<": "<< "NO"<< endl;
                          cout <<"imposible"<<endl;
                          cout << "------------->>>" << lawn_square[i][j] << " and " << lawn_square[l][j];
                          break_loops = true;
                        break;
                      }

                  }
              }
       if(break_loops)break;
          }
       if(break_loops)break;
  //    }
     if(break_loops)break;
   }

}
   if(!break_loops) {
       output_large << "Case #"<< tc_count <<": "<< "YES"<< endl;
       cout <<"Yes /n";
   }
   cout <<"---------------->"<< tc_count <<endl;
   break_loops = false;
 }
   return 0;
}

