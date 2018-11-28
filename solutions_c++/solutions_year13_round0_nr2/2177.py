#include<iostream>
using namespace std;

#include<fstream>
ifstream fin ("B-large.in");
ofstream fout ("out.txt");
#define cin fin 
#define cout fout


int main (){
  int t;
  cin>>t;
  for (int num_t = 0;num_t < t;++ num_t){
    int n, m;
    cin>>n>>m;
    int arr[105][105];
    for (int i=0;i<n;++i){
      for (int j=0;j<m;++j){
	cin>>arr[i][j];
      }
    }

    bool poss [100][100];
   for (int  i=0;i<n;++i){
      for (int  j=0;j<m;++j){
	poss[i][j] = 0;
      }
    }
  
   for (int i=0;i<n;++i){
      int max = arr[i][0];
      for (int j=1;j<m;++j){
	if (arr[i][j] > max)max = arr[i][j];
      }
      for (int j=0;j<m;++j){if (arr[i][j] == max)poss[i][j] = 1;}
    }
    for (int j=0;j<m;++j){
      int max = arr[0][j];
      for (int i=1;i<n;++i){
	if (arr[i][j] > max)max = arr[i][j];
      }
      for (int i=0;i<n;++i){if (arr[i][j] == max)poss[i][j] = 1;}
    }
    int i, j;
    bool flag = 1;
    for ( i=0;i<n;++i){
      for ( j=0;j<m;++j){
	if (poss[i][j] == 0)flag = 0;
      }
    }
    cout<<"Case #"<<num_t + 1<<": ";
    if (flag== 0)cout<<"NO\n";
    else cout<<"YES\n";
  }
  return 0;
}

