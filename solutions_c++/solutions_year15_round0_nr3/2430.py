#include <iostream>
using namespace std;
const int I = 2;
const int J = 3;
const int K = 4;

int m1[][5] = {
    {0,0,0,0,0},
    {0,1,I,J,K},
    {0,I,1,K,J},
    {0,J,K,1,I},
    {0,K,J,I,1},
};

int m2[][5] = {
    {1,1,1,1,1},
    {1,1,1,1,1},
    {1,1,-1,1,-1},
    {1,1,-1,-1,1},
    {1,1,1,-1,-1},
};

int a[100000];
void solve()
{
    int n,m;
    cin >> n >> m;
    int value = 1;
    int sign = 1; 
    int sv[] = {I,J,K};
    int ss[] = {1,1,1};
    int index  = 0;
    char ch;
    for (int i = 0; i < n; i++)
    {
        cin >> ch;
        int k;
        switch(ch){
            case 'i': k = I;
                      break;
            case 'j': k = J;
                      break;
            case 'k': k = K;
                      break;
        }
        a[i] = k;
    } 
    if (m > 12){
    m = m % 4;
    m = m + 8;                            
    }
    if (m == 8){
        cout << "NO"<<endl;
        return;
    }
    int i = 0;
    while (i < m*n){
        int k = a[i % n]; i++;
        sign = sign * m2[value][k];
        value = m1[value][k];
        
        if (index < 3 && sign == ss[index] && value == sv[index]){
            index ++;
            if(index <3){
            value = 1;
            sign = 1;
            }
        }
    }
    if (index == 3 && (value == K) && sign == 1)
    {
        cout << "YES"<<endl;
    }
    else {
        cout << "NO"<<endl;
    }
}

int main()
{
    cin.sync_with_stdio(false);
    int cases;
    cin >> cases;
    for (int i = 1; i <= cases; i++)
    {
        cout << "Case #"<<i<<": ";
        solve();
    }
    return 0;
}
