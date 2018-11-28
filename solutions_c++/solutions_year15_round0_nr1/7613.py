#include<iostream>
#include<algorithm>
#include<cstring>
#include<fstream>

using namespace std;

int main()
{
    int T;
    ofstream fout("1out.txt");
    ifstream fin("A-large.in");

    fin>>T;
    for(int t = 1 ; t <= T ; t++)
    {
        int S;
        fin>>S;
        char str[1200];
        fin.getline(str , 1200);
        long long int c = 0 ;
        long long int all = 0;
        for(int j = 1 ; j < strlen(str) ; j++)
        {
            if(str[j] != 48)
            {
                if(all < j)
                {
                    c = c + j - all;
                    all = all + j - all;
                }
                all = all + str[j] - 48;
            }

        }
        fout<<"Case #"<<t<<": "<<c-1<<endl;
    }
    return 0;
}
