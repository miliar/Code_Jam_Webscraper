#include <iostream>
#define MAXN 120

using namespace std;

int matrix[MAXN][MAXN];
int N,M;

bool isRowContained[MAXN];
bool isColumnContained[MAXN];

bool canCutAtHeight(int height){
  //we consider the subset where matrix[i][j]<=height
  //this should be an union of rows and columns
  
  for(int i=0;i<N;i++)
    isRowContained[i]=true;
  for( int j=0;j<M;j++)
    isColumnContained[j]=true;

  for(int i=0;i<N;i++)
    for(int j=0;j<M;j++)
      if(matrix[i][j]>height){
	isRowContained[i]=false;
	isColumnContained[j]=false;
      }

  for(int i=0;i<N;i++)
    for(int j=0;j<M;j++)
      if(matrix[i][j]<=height &&
	 isRowContained[i]==false &&
	 isColumnContained[j]==false)
	return false;

  return true;  
}

int main(){
  int T;
  cin>>T;
  for(int test=0;test<T;test++){
    cin>>N>>M;
    for(int i=0;i<N;i++)
      for(int j=0;j<M;j++)
	cin>>matrix[i][j];

    bool canCut=true;
    for(int height=100;height>=1;height--)
      if(!canCutAtHeight(height)){
	canCut=false;
	break;
      }

    cout<<"Case #"<<test+1<<": ";
    if(canCut)
      cout<<"YES"<<endl;
    else
      cout<<"NO"<<endl;
    
  }
}
