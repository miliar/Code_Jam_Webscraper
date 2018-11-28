#include <iostream>

using namespace std;

int main()
{
    int T, sh;
    cin >> T;
    char ch;
    int cse = 0;
    while(T--)
    {
        int cnt = 0;
        int add = 0;
        cse++;
        cin >> sh;
        for(int i=0; i<=sh; i++)
        {
            cin >> ch;
            if(ch=='0');
            else if(i==0)
                cnt+=ch-'0';
            else if(i<=cnt)
                cnt+=ch-'0';
            else
            {
                add += i-cnt;
                cnt += i-cnt;
                cnt += ch-'0';
            }
        }
        cout<<"Case #" << cse <<": "<< add << endl;
    }
    return 0;
}
