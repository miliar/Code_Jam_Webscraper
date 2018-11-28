#include<iostream>
#include<algorithm>
#include<cstring>
#include<fstream>

using namespace std;

int main()
{
    int T;
    ofstream fout("1out.txt");
    ifstream fin("A-small-attempt1.in");

    fin>>T;
    for(int t = 1 ; t <= T ; t++)
    {
        int S;
        fin>>S;
        char str[1200];
        fin.getline(str , 1200);
        long long int c = 0 ;
        long long int total = 0;
        for(int j = 1 ; j < strlen(str) ; j++)
        {
            if(str[j] != 48)
            {
                if(total < j)
                {
                    c = c + j - total;
                    total = total + j - total;
                }
                total = total + str[j] - 48;
            }

        }
        fout<<"Case #"<<t<<": "<<c-1<<endl;
    }
    return 0;
}
