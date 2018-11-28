#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main()
{
    int T,i,j;
    string s;
    ofstream file1;
    file1.open("D.txt");
    cin >>T;

    for(j=1;j<=T;j++)
    {
        cin >>s;
        long long int count=0;

        int len=s.length();
        for(i=0;i<len-1;)
        {
            if(s[i]==s[i+1])
                i++;
            else
            {
                count++;
                i++;
            }
        }
        if(s[i]=='-')
            count++;
        file1<<"Case #"<<j<<": ";
        file1 <<count<<endl;
    }

    return 0;
}
