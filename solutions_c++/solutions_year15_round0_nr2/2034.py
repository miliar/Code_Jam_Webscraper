#include <iostream>

using namespace std;

int T[1005];

int ilepodzialow(int n, int kawalek)
{
    int podzialy = 0;
    for(int i=0; i<n; i++)
    {
      //  cout << (T[i] + kawalek - 1) << " " << kawalek << "A\n";
        podzialy += (T[i] -1)/kawalek;
    }
 //   if (podzialy + kawalek < 4)
    //    cout <<"A" << podzialy << " " << kawalek << endl;
    return (podzialy + kawalek);
}

int main()
{
    int testy;
    cin>>testy;
    for(int i=1; i<=testy; i++)
    {
        int n, mini = 0;
        cin>>n;
        for(int j=0; j<n; j++)
        {
            cin>>T[j];
            mini = max(mini, T[j]);
        }
        for(int j=1; j<mini; j++)
        {
            mini = min(ilepodzialow(n, j), mini);
        }
        cout <<"Case #" << i << ": " << mini <<endl;
    }
    
  //  system("PAUSE");
    
    return 0;
}
