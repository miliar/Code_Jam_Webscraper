#include <iostream>
#include <string>
using namespace std;

int main()
{

  string aa;
  int a[1000];
  int S,T, sum, num;
  cin >> T;

  for(int i=0; i<T; i++){
    cin >> S;
    cin >> aa;
    for (int j=0; j<S+1; j++){
      a[j]=aa[j]-'0';
      //cout << a[j] << endl;
    }
    sum=0;
    num=0;
    for (int j=0; j<S+1; j++){
      if (a[j]>0)
      {
      if (sum>=j)
      {
        sum=sum+a[j];
        //cout << "sum:" << sum << endl;
      }
      else
      {
        num=num+j-sum;
        sum=j+a[j];
        //cout << "num:" << num << endl;
      }
      }
    }
    cout << "Case #" << i+1 << ": "<<num << endl;
  }
  return 0;
}
