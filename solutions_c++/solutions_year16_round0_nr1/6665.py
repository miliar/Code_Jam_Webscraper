#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int D[10];

bool checkfornumbers()
{
    int i;
    bool flag=true;
    for(i=0;i<10;i++)
    {
        if(!(D[i]==i))
            flag=false;
    }
    return flag;
}

void extractnumbers(long int E)
{
    int number;
    while(E>0)
    {
        number=(int)E%10;
        D[number]=number;
        E=E/10;
    }
}

int main(){


    int T,i;
    long int N[100],m;
    fstream inputfile ("C:\\Users\\spars\\Downloads\\A-large.in");
    ofstream outputfile ("C:/Users/spars/Downloads/output1.1.in");
    if (inputfile.is_open())
        {
            i=0;
            inputfile>>T;
            while ( inputfile>>m )
            {
                N[i]=m;
                i++;
            }
        }
    else cout << "Unable to open file";


    for(i=0;i<T;i++)
    {
        int j;
        int multiplier=1;
        int calculated;
        string s;
        for(j=0;j<10;j++)
        {
            D[j]=100;
        }
        if(N[i]==0)
            outputfile<<"Case #"<<i+1<<": INSOMNIA"<<endl;
        else
        {
            do{
                    calculated=N[i]*multiplier;
                    extractnumbers(calculated);
                    multiplier++;
                    }
                while(!checkfornumbers());
            outputfile<<"Case #"<<i+1<<": "<<calculated<<endl;
        }
    }
    outputfile.close();
    return 0;
}
