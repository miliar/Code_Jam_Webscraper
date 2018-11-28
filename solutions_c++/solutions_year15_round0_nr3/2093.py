#include<iostream>
#include<algorithm>
using namespace std;

int a[5][5] = {{0 , 0 , 0 , 0 , 0} , {0 , 1 , 2 , 3, 4} , {0 , 2 , -1 , 4 , -3} , {0 , 3  , -4 , -1 , 2} , {0 , 4 , 3 , -2 , -1}};
int mul(int A , char c)
{
    int q = 0;
    if(c == 'i')
        q = 2;
    else if(c == 'j')
        q = 3;
    else if(c == 'k')
        q = 4;
    if(A > 0)
        return a[A][q];
    return -a[abs(A)][q];
}
int main()
{
    int T;
    cin >> T;
    for(int test = 0;test < T;test ++)
    {
        int L;
        cin >> L;
        long long X;
        cin >> X;
        string s;
        cin >> s;
        
        string t;
        for(int i = 0;i < X;i ++)
            t += s;
        
        int tmp = 1;
        
        int posi = -1;
        for(int j = 0;j < (int)t.length();j ++)
        {
            tmp = mul(tmp , t[j]);
            if(tmp == 2)
            {
                posi = j;
                break;
            }
        }
       // for(int i = 0;i < X;i ++)
         //   t += s;
        
        int posj = -1;
        tmp = 1;
        for(int j = 0;j < (int)t.length();j ++)
        {
            tmp = mul(tmp , t[j]);
            if(tmp == 4)
                posj = j;
        }

        tmp = 1;
        for(int j = 0;j < (int)t.length();j ++)
            tmp = mul(tmp , t[j]);
        

/*        X = (X % 4ll);
        if(X == 1)
            tmp = tmp;
        else if(X == 2)
            tmp = -1;
        else if(X == 3)
            tmp = -tmp;
        else if(X == 0)
            tmp = 1;*/
        
        if(posi != -1 && posj != -1 && posj > posi && tmp == -1)
            cout << "Case #" << test + 1 << ": " <<  "YES" << endl;
        else
            cout << "Case #" << test + 1 << ": " <<  "NO" << endl;
            
    }
    return 0;
}
