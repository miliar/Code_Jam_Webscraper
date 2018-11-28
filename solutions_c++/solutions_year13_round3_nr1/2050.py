#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;





int solve(char* name, int n)
{
    int d = strlen(name);
    int cons = 0;

    int answer = 0;

    int start = 0;
    int endn;

    for(start = 0; start <= d - n; start++)
    {
        cons = 0;
        endn = d + 1;

        for(int i = start; i < d; i++)
        {

            if(name[i] == 'a' || name[i] == 'o' || name[i] == 'u' || name[i] == 'i' || name[i] == 'e')
            {
                cons = 0;
                endn = d + 1;
            }
            else cons++;

            if(cons == n)
            {
                endn = i + 1;
                break;
            }
        }

        answer += (d - endn + 1);

        //cout << "debug: " << start << " " << endn << endl;

    }

    /*if(name[d-1] == 'a' || name[d-1] == 'o' || name[d-1] == 'u' || name[d-1] == 'i' || name[d-1] == 'e')
    {
        answer -= 2;
    }*/

    return answer;

}


int main()
{
    int T;
    char* a = new char[101];
    int b;

    cin >> T;

    for(int i = 0; i < T; i++)
    {
        scanf("%s %d", a, &b);

        cout << "Case #" << i+1 << ": "<< solve(a, b) << endl;
    }

}
