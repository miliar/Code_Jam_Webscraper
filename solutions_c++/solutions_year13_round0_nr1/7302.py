#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>
#include<vector>

using namespace std;

char arr[5][5];

vector<string > w;

int main()
{
    int T;
    
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d",&T);
    
    w.push_back("XXXX");
    w.push_back("XXXT");
    w.push_back("OOOO");
    w.push_back("OOOT");
    
    for(int i = 0; i<4; i++)
    {
        sort(w[i].begin(), w[i].end());
    }
    
    for(int t = 0; t<T; t++)
    {
        string r = "";
        string c = "";
        string d = "";
        getchar();
        for(int i = 0; i<4; i++)
        {
            gets(arr[i]);
        }
        
        
        printf("Case #%d: ", t + 1);
        
        string res = "Draw";
        for(int i = 0; i<4; i++)
        {
            r = "";
            for(int j = 0; j<4; j++)
            {
                r += arr[i][j];
            }
            sort(r.begin(), r.end());
            int ind = -1;
            for(int s = 0; s<4; s++)
            {
                if(r == w[s])
                {
                    ind = s;
                    break;
                }
            }
            if(ind>=0 && ind<2)
            {
                res = "X won";
                break;
            }
            else if(ind>=2)
            {
                res = "O won";
                break;
            }
            
            c = "";
            for(int j = 0; j<4; j++)
            {
                c += arr[j][i];
            }
            sort(c.begin(), c.end());
            for(int s = 0; s<4; s++)
            {
                if(c == w[s])
                {
                    ind = s;
                    break;
                }
            }
            
            if(ind>=0 && ind<2)
            {
                res = "X won";
                break;
            }
            else if(ind>=2)
            {
                res = "O won";
                break;
            }
            
            d += arr[i][i];
        }
        sort(d.begin(), d.end());
        for(int s = 0; s<4; s++)
        {
            if(d == w[s])
            {
                if(s<2)
                    res = "X won";
                else
                    res = "O won";
                break;
            }
        }
        d = "";
        int a = 0;
        for(int j = 3; j>=0; j--)
        {
            d += arr[j][a];
            a++;
        }
        sort(d.begin(), d.end());
        for(int s = 0; s<4; s++)
        {
            if(d == w[s])
            {
                if(s<2)
                    res = "X won";
                else
                    res = "O won";
                break;
            }
        }
        if(res == "Draw")
        for(int i = 0; i<4; i++)
        {
            for(int j = 0; j<4; j++)
            {
                if(arr[i][j] == '.')
                {
                    res = "Game has not completed";
                    break;
                }
            }
        }
        cout << res << endl;
        
    }
    return 0;
}
