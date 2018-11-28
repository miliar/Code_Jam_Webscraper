#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

int T, N, M;
int a[200][200];


int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
  //  freopen("B.in", "r", stdin);
  //  freopen("B.out", "w", stdout);
    
    int up[200][200];
    int down[200][200];
    int left[200][200];
    int right[200][200]; 
    
    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cin >> N >> M;
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                cin >> a[i][j];
        
      //  memset(up, 0, sizeof(up));
     //   memset(down, 0, sizeof(down));
     //   memset(left, 0, sizeof(left));
     //   memset(right, 0, sizeof(right));
        
        for (int i = 0; i < N; i++)
        {
            left[i][0] = 0;
            for (int j = 1; j < M; j++)
                left[i][j] = max(left[i][j - 1], a[i][j - 1]);
           // left[i][0] = 0;
        }
                
        for (int i = 0; i < N; i++)
        {
            right[i][M - 1] = 0;
            for (int j = M - 2; j >=0; j--)
                right[i][j] = max(right[i][j + 1], a[i][j + 1]);
           //  right[i][M - 1] = 0;    
        }
        
        for (int j = 0; j < M; j++)
        {
            up[0][j] = 0;
            for (int i = 1; i < N; i++)
                up[i][j] = max(up[i - 1][j], a[i - 1][j]);
          //  up[0][j] = 0;
        }
                
        for (int j = 0; j < M; j++)
        {
            down[N - 1][j] = 0;
            for (int i = N - 2; i >= 0; i--)
                down[i][j] = max(down[i + 1][j], a[i + 1][j]);
           // down[N - 1][j] = 0;
        }
                
       /*
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
                cout << left[i][j] << " ";
            cout << endl;
        }      
        cout << endl;  
        
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
                cout << right[i][j] << " ";
            cout << endl;
        }
        cout << endl;
        
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
                cout << up[i][j] << " ";
            cout << endl;
        }
        cout << endl;
        
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
                cout << down[i][j] << " ";
            cout << endl;
        }
        cout << endl;
                */
                
        bool ok = true;        
                
        for (int i = 0; i < N; i++)
        {
            if (!ok) break;
            for (int j = 0; j < M; j++)
            {
                if (up[i][j] <= a[i][j] && down[i][j] <= a[i][j]) continue;
                if (left[i][j] <= a[i][j] && right[i][j] <= a[i][j]) continue;
              //  cout << i << " " << j << endl;
                ok = false;
                break;
            }
        }
        
        if (ok) 
            printf("Case #%d: YES\n", t);
        else
            printf("Case #%d: NO\n", t);
    
    }
    return 0;
}
