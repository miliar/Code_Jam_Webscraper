#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void process()
{
    int groupCount = 1,i = 1;
    string S;

    cin >> S;

    while(i < (int)S.length())
    {
        if(S[i-1] != S[i])
        {
            groupCount++;
        }
        i++;
    }
    if(S[i-1] == '+')
    {
        groupCount--;
    }
    cout << groupCount << endl;
}

int main(int argc, char* argv[])
{
    int numberOfTestCases = 0;

    scanf("%d", &numberOfTestCases);

    for(int i = 0 ; i< numberOfTestCases ; i++)
    {
        printf("Case #%d: ", i + 1);
        process();
    }
}
