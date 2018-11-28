#include <iostream>  
#include <fstream>  
using namespace std;  
#define N 5  
  
int judge(int f[N][N],int o,int s[N][N],int t,int* a)  
{  
    int pos = -1;  
    for(int i = 1; i < N; i++)  
        for(int j = 1; j < N; j++)  
            if(f[o][j] == s[t][i])  
            {  
                (*a) = f[o][j];  
                pos++;  
            }  
    return pos;  
}

int main() {

    //ifstream cin("D:\\A-small-attempt1.in");  
    //ofstream cout("D:\\A-small-attempt1.out"); 
    
    int k;  
    cin >> k;  
  
    for(int s = 1; s <= k; s++)  
    {  
        int first[N][N], second[N][N], one, two, result;  
        cin >> one;  
        for(int i = 1; i < N ; i++)  
            for(int j = 1; j < N ; j++)  
                cin >> first[i][j];  
        cin >> two;  
        for(int i = 1; i < N ; i++)  
            for(int j = 1; j < N ; j++)  
                cin >> second[i][j];  
        cout << "Case #" << s << ": ";  
        int pos = judge(first, one, second, two, &result);  
        if(pos == -1)  
            cout << "Volunteer cheated!";  
        else  
        {  
            if(pos)  
                cout << "Bad magician!";  
            else  
                cout << result;  
        }  
        cout << endl; 
    }  
    return 0;  
}  
