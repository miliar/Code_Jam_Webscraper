#include <iostream>
#include<fstream>
using namespace std;

int main() {
	ofstream fout;
	fout.open("out.txt");
    int t,tempi,smax,sum;
    t=0;
    char *temp;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        smax=tempi=sum= 0;
        
        cin>>smax;
        temp = new char[smax+1];
        cin>>temp;
        for(int i = 0;i<smax;i++)
        {
            tempi=(int)(temp[i]-'0');
            sum+=tempi;
        }
        if(smax<=sum)
        fout<<"Case #"<<j<<": 0\n";
        else
        fout<<"Case #"<<j<<": "<<smax-sum<<"\n";
        delete temp;
    }
    fout.close();
    return 0;
}

