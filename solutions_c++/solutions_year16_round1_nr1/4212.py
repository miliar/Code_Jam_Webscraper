#include<cstdio>
#include<string>
#include<iostream>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int t, c=0;
    string str, str2;

    scanf("%d", &t);
    getchar();
    while(t--)
    {
        str.clear();
        str2.clear();
        getline(cin, str);
        int len = str.length();

        for(int i=0; i<len; i++)
        {
            if(i == 0)
                str2.push_back(str[i]);
            else
            {
                if(str[i] >= str2[0])
                    str2.insert(0, 1, str[i]);
                else
                    str2.push_back(str[i]);
            }
        }

        cout << "Case #" << ++c << ": " << str2 << endl;
    }

    return 0;
}
