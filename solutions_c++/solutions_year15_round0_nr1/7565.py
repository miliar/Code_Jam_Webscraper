#include<iostream>
#include<algorithm>
#include<cstring>
#include<fstream>

using namespace std;

int main()
{
    int Test;
    ofstream fout("1out.txt");
    ifstream fin("A-large.in");

    fin>>Test;
    for(int t = 1 ; t <= Test ; t++)
    {
        int S;
        fin>>S;
        char st[1200];
        fin.getline(st , 1200);
        long long int c = 0 ;
        long long int total = 0;
        for(int j = 1 ; j < strlen(st) ; j++)
        {
            if(st[j] != 48)
            {
                if(total < j)
                {
                    c = c + j - total;
                    total = total + j - total;
                }
                total = total + st[j] - 48;
            }

        }
        fout<<"Case #"<<t<<": "<<c-1<<endl;
    }
    return 0;
}
