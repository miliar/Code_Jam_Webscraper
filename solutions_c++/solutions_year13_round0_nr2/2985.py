#include <iostream>
using namespace std;
int main()
{
    int N = 0;
    cin >> N;
    int array[100][100];
    for (int k=0;k<N;++k)
    {
       int n, m;
       cin >> n >> m;
       for (int i=0;i<n;++i)
       {
          for (int j=0;j<m;++j)
             cin >> array[i][j];
       }   

       bool wrong = false;
       for (int i=0;i<n;++i)
       {
         for (int j=0;j<m;++j)
         {
             //for any element 
             bool rowFailed = false;
             bool colFailed = false;
             for (int s=0;s<n;++s)
             { 
                if (array[s][j]>array[i][j]) {rowFailed = true; break;}
             }
             for (int s=0;s<m;++s)
             { 
                if (array[i][s]>array[i][j]) {colFailed = true; break; }
             }
             if (rowFailed && colFailed ) 
             {
                i=n;j=m;
                wrong = true;
             }
         }
       }
       cout << "Case #" << k+1 << ": ";
       if (wrong) cout << "NO" << endl;
       else cout << "YES" << endl;
    }


}
