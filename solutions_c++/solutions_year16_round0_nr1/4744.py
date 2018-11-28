#include<iostream>
#include<string>

using namespace std;

int main()
{
  unsigned long long Test;
  cin >> Test;
  for(int tt=1 ; tt<=Test ; tt++)
  {
    unsigned long long Input;
    cin >> Input;
    bool Data[10] = {0};
    bool IsDone = true;
    for(int ii = 1 ; ii < 10000 ; ii++)
    {
      string Number = to_string(Input*ii);
  //    cout << "\t\t" << Number << endl;
  //    cout << "Size" << Number.size() << endl;
      for(int jj = 0 ; jj < Number.size() ; jj++)
        Data[Number[jj] - 48  ] = true;

/*      for(int jj = 0 ; jj < 10 ; jj++)
        cout << Data[jj] << " ";
*/
      IsDone = true;
      for(int jj = 0 ; jj < 10 ; jj++)
        if(!Data[jj])
          IsDone = false;
      if(IsDone)
      {
        cout << "Case #"<< tt << ": " << Number << endl;
        break;
      }
    }
    if(!IsDone)
    cout << "Case #"<< tt << ": " << "INSOMNIA" << endl;
  }
  return 0;
}
