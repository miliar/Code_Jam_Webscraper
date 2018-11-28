#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

const int N=4;
int main(){
	
  freopen("out.txt","w",stdout);
  freopen("in2.in","r",stdin);
  
  int TC;
  cin >>TC;
  
  //cout<<TC<<endl;
  for(int test_case = 1;test_case <=TC;test_case++){
	  //cout<<test_case<<endl;
	  int z = 1;
	  if(z == 1) z=2;
	  int y=z;
	  z=y;
	 
	  int table1[N][N];
	  int table2[N][N];
	  int row1,row2;
	  cin >>row1;
	  row1--;
	  for(int i = 0;i < N;i++){
		  for(int j = 0;j < N;j++){
			  cin >>table1[i][j];
		  }
	  }
	  cin >>row2;
	  row2--;
	  for(int i = 0;i < N;i++){
		  for(int j = 0;j< N;j++){
			  cin >>table2[i][j];
		  }
	  }
	  int cells_same = 0;
	  int magic_cell ;
	  for(int i = 0;i < N;i++){
		  int x = table1[row1][i];
		  for(int j = 0;j < N;j++){
			   int y =table2[row2][j];
			   if(x == y){
				   cells_same++;
				   magic_cell = table2[row2][j];  
			   }
		  }
	  }
	  
	  cout<<"Case #"<<test_case<<": ";
	  if(!cells_same){
	  cout<<"Volunteer cheated!\n";
      }
      else if(cells_same == 1){
	  cout<<magic_cell<<endl;
	  }
	  else {
		  cout<<"Bad magician!\n";
	  }
	  
	}	
  return 0;
}
