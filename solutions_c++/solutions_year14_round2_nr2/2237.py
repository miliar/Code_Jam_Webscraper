#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
    fstream file;
    ofstream output;
    file.open("B-small-attempt0.in");
    output.open("answer.txt");

    int n=0;

    file>>n;

    for(int i=0;i<n;i++)
    {
        int a,b,k;
        long long ans=0;

        file>>a;
        file>>b;
        file>>k;

        for(int j=0;j<a;j++)
        {
            for(int l=0;l<b;l++)
            {
                if((j&l)<k)
                {
                    ans++;
                }
            }
        }

        output<<"Case #"<<i+1<<": "<<ans<<endl;
    }


}
