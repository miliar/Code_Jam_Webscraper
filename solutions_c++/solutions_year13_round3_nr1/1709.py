#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");
    int T;
    in>>T;
    for ( int t = 0; t < T; t++)
    {
        string H; int n;
        in>>H>>n;
        for (int i = 0; i < H.length();i++)
        {
            if (int(H[i])== 97 ||int(H[i])== 101 ||int(H[i])== 105 ||int(H[i])== 111 ||int(H[i])== 117)
                H[i] = 'a';
            else
                H[i] = 'b';
        }
        string check = "";
        for ( int i = 0;i<n;i++)
        {
            check += "b";
        }
        int ctr = 0;
        for ( int i = 0; i < H.length();i++)
        {
            for(int j = 0; j < H.length()-i;j++)
            {
                string t =  H.substr(j,H.length()-i-j);
                if (t.find(check)!= -1)
                    ctr++;
            }
        }
        out<<"Case #"<<t+1<<": "<<ctr<<endl;
    }
    out.close();
}
