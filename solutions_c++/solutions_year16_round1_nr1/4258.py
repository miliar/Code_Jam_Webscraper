#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main(){


    int T,i,j;
    string S[100],m;
    fstream inputfile ("C:\\Users\\spars\\Downloads\\A-large.in");
    ofstream outputfile ("C:/Users/spars/Downloads/A-largeOutput.in");
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
        string s;
        s=S[i].at(0);
        if(S[i].length()>1)
        {
            for(j=1;j<(S[i].length());++j)
        {
            if(S[i].at(j)>=s.at(0)){
                s=(S[i].at(j))+s;
            }
            else{
                s=s+(S[i].at(j));
            }
        }

        }

        outputfile<<"Case #"<<i+1<<": "<<s<<endl;
    }
    outputfile.close();
    return 0;
}
