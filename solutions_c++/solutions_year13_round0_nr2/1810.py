/*
    https://code.google.com/codejam/contest/dashboard?c=2270488#s=p1
*/
#include <iostream>
#include <string>
#include <cmath>

#define mix(a, b) ((a > b) ? b : a)

using namespace std;

int main()
{
    int T;
    
    cin >> T;    

    for (int i = 0; i < T; i++) {
        int N, M;
        
        cin >> N;
        cin >> M;
        
        int **a = new int*[N];
        int *n = new int[N];
        int *m = new int[M];
        
        for (int j = 0; j < N; j++) {
            a[j] = new int[M];
            n[j] = 0;
        }
                
        for (int j = 0; j < M; j++)
            m[j] = 0;
        
        for (int j = 0; j < N; j++) { // rows
            for (int k = 0; k < M; k++) { // columns
                cin >> a[j][k];

                if (a[j][k] > m[k])
                    m[k] = a[j][k];
                
                if (a[j][k] > n[j])
                    n[j] = a[j][k];
            }        
        }  
        
        bool result = true;
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < M; k++) {
                if (min(n[j], m[k]) != a[j][k]) {
                    result = false;
                    break;
                }
            }
            if (!result)
                break;
        }
        
        cout << "Case #" << (i + 1) << ": ";
        
        if (result)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    
        for (int j = 0; j < N; j++) 
            delete a[j];
        delete a, n, m;
    }    
    return 0;
}
