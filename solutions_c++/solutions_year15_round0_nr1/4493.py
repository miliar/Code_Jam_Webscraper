#include <iostream>
#include <fstream>
#include <string>

using namespace std;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out2.txt", "w", stdout);
    int t, x=1;
    cin >> t;

    while(t--)
    {
        int shy;
        string str;

        cin >> shy >> str;
        int answer = 0, bek = 0;
        

        for(int i = 0; i < shy+1; i++)
        {
            
            if(bek < i)
            {
                int z= (i - bek);
				answer+=z;
                bek = i;
            }
            int y= (str[i] - '0');
			bek+=y;
           
        }
        cout <<"Case #"<< x <<": "<< answer << endl;
        x=x+1;
    }
    return 0;
}