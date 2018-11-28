#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int testCases;
    cin >>testCases;
    string rep;
    int maxN;
    for (int a=0; a<testCases; a++)
    {
        cin >> maxN >> rep;
        int totalSoFar=0;
        int requiredAdd=0;
        for (int b=0; b<=maxN; b++)
        {
            int dd=(int)rep[b]-48;
            int toAdd=(b-totalSoFar>=0?b-totalSoFar:0);
            requiredAdd+=toAdd;
            totalSoFar+=toAdd;
            totalSoFar+=dd;

        }
        printf("Case #%d: %d\n", a+1,requiredAdd);
    }

}
