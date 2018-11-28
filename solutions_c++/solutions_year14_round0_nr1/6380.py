#include <iostream>
using namespace std;
int result[4];
int checkCard( int * a, int * b )
{ 
  int count=0;
  for (int i=0; i<4; i++){
    for (int j=0; j<4; j++){
      if (a[i]==b[j]) {
        result[count]=a[i];
	count++;	
      }
    }
  }
  return count;
}

int main(){
  int cases;
  int count;

  cin >> cases;
  int a[4][4];
  int b[4][4];
  int m,n,dummy;
  for (int cc=0; cc<cases; cc++){
    cin >> m;
    for (int i=0; i<4; i++){
      for (int j=0; j<4; j++){
        cin >> a[i][j];
      }
    }

    cin >> n;
    for (int i=0; i<4; i++){
      for (int j=0; j<4; j++){
        cin >> b[i][j];
	}
    }


   count=checkCard(a[m-1],b[n-1]);
   cout << "Case #" << cc+1 << ": ";
   switch(count)
   {
   case 0: 
     cout << "Volunteer cheated!";
     break;
   case 1:
     cout << result[0];
     break;
   default:
     cout<< "Bad magician!" ;
     break;
   }
   cout << endl;

 }// for cases
}//main
