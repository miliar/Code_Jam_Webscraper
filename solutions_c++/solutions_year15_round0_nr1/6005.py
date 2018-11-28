#include <vector>
#include <iostream>
#include <string>

using namespace std;

int main()
{
    int N,i,j,k=0; cin>>N;

    for(i=0; i<N; i++)
    {
        int s;
        string a;

        cin>>s>>a;

        int aud=0;
        int inc=0;

        for(j=0; j<a.size(); j++)
        {
            int c = a[j]-'0';
            int d = max(0, j-aud);
            //cout << "j: " << j << "\taud: " << aud << endl;
            aud += c;
            if(c>0)
            {
                //cout << "c: " << c << "\td: " << d << endl;
                aud += d;
                inc += d;
            }
        }
        
        cout << "Case #" << ++k << ": " << inc << endl;
    }

    return 0;
}

