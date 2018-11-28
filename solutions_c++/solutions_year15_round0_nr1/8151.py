#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

int main()
{
    long int T,w,y,z,ds=0,smax,v,count;
    char ch;
    ifstream f1;
	f1.open("C:\\Dev-Cpp\\Snehil\\Google Code Jam '15\\Input2.in");
	ofstream f2;
	f2.open("C:\\Dev-Cpp\\Snehil\\Google Code Jam '15\\Output2.out");
	f1>>T;
	for(w=1;w<=T;w++)
    {
        f1>>smax;
        v=0;
        count=0;
        for(y=0;y<=smax;y++)
        {
            f1>>ch;
            z=(int)ch-48;
            if(v>=y)
                v+=z;
            else if(z!=0)
            {    
                count+=(y-v);
                v+=(y-v);
                v+=z;
            }
        }
        if(w==1)
            f2<<"Case #"<<w<<": "<<count;
        else
            f2<<"\nCase #"<<w<<": "<<count;
    }
    f1.close();
	f2.close();
	return 0;
}
