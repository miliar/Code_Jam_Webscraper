#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int flips;

void flip(string &s,int pos,char value)
{
    int i;
    for(i=0;i<=pos;i++)
        s.at(i)=value;
    flips++;
}

int main(){


    int T,i;
    string S[100],m;
    fstream inputfile ("C:\\Users\\spars\\Downloads\\gcj\\B-large.in");
    ofstream outputfile ("C:/Users/spars/Downloads/gcj/B-largeoutput.in");
    if (inputfile.is_open())
        {
            i=0;
            inputfile>>T;
            while ( inputfile>>m )
            {
                S[i]=m;
                i++;
            }
        }
    else cout << "Unable to open file";


    for(i=0;i<T;i++)
    {
        flips=0;
        int j=1;

        for(j=1;j<S[i].length();j++)
        {
            if(S[i].at(j-1)!=S[i].at(j))
                flip(S[i],j-1,S[i].at(j));
        }

        if(S[i].at(j-1)=='-')
            flip(S[i],j-1,'+');

        outputfile<<"Case #"<<i+1<<": "<<flips<<endl;
    }
    outputfile.close();
    return 0;
}
