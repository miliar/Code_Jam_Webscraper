#include<fstream>
#include<iostream>
using namespace std;
int main()
{
    ifstream fin;
    ofstream fout;
    int T,Smax,x,standing,k,required;
    string S;
    fin.open("A-large.in");
    fout.open("out.txt");

    fin>>T;
    for(int l=0;l<T;l++)
    {
        fin>>Smax;
        fin>>S;
        k = 0;
        standing = 0;
        required = 0;
        while(k<=Smax)
        {
            if(k<=standing+required) {
                standing+=(int)S[k]-48;
                k++;
            }
            else {
                required++;
            }
        }
        fout<<"Case #"<<l+1<<": "<<required<<endl;
    }
    return 0;
}
