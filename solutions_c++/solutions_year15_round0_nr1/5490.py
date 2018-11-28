#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

int getgap(vector<int> slevs, int smax)
{
    int maxgap=0;
    int standing=0;
    for(int i=0;i<=smax;i++)
    {
        maxgap=max(maxgap,i-standing);
        standing+=slevs[i];
    }
    return maxgap;
}

int digtoint(char c)
{
    switch(c)
    {
        case '1':
            return(1);
        case '2':
            return(2);
                case '3':
            return(3);
                    case '4':
            return(4);
                    case '5':
            return(5);
                    case '6':
            return(6);
                    case '7':
            return(7);
                    case '8':
            return(8);
                    case '9':
            return(9);
                    case '0':
            return(0);

    }
    return -1;
}

int main()
{
//    vector<int> slevs{1,1,0,0,1,1};
//    cout<<getgap(slevs,5);
    ifstream inputt("in.in");
    if (!inputt)
        cerr << "no file\n";
    ofstream outputt("out.txt");
    string line;
    vector<int> ccase;
    getline(inputt,line);
    //cout<<line;
    int T=stoi(line);
    int pos;
    int smax;
    int res=0;
    for(auto i=0;i<T;i++)
    {
        ccase.clear();
        getline(inputt,line);
        pos=line.find_first_of(' ');
        smax=stoi(line.substr(0,pos).c_str());
        for(auto j=pos+1;j<line.length();j++)
        {
            ccase.push_back(digtoint(line[j]));
        }
        res=getgap(ccase,smax);
        outputt<<"Case #"<<i+1<<": "<<res<<endl;
    }
}
