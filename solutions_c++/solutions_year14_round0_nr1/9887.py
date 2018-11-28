#include <iostream>
#include <fstream>
using namespace std;
//ifstream cin("a.in");
//ofstream cout("a.out");
void input(int a[5][5], int &n){
     ::cin>>n;
     for (int i=1; i<=4; i++)
          for (int j=1; j<=4; j++) ::cin>>a[i][j];
}
void  solved(int test){
      int a[5][5], b[5][5];
      int n, m;
      int k;
      input(a, n);
      input(b,m);
      
      int count = 0;
      for (int i=1; i<=4; i++)
          for (int j=1; j<=4; j++)
              if (a[n][i] == b[m][j]){
                 k = a[n][i];
                 count++;
              }
      ::cout<<"Case #"<<test<<":";
      if (count == 0) ::cout<<" Volunteer cheated!";
         else if (count > 1) ::cout<< " Bad magician!";
              else ::cout<<" "<<k;
      
}
int main(){
    int t;
    ::cin>>t;
    for (int i=1; i<=t; i++){
        solved(i);
        if (i<t) ::cout<<endl;
    }
    //system("pause");
    return 0;
}
