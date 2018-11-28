#include<bits/stdc++.h>
#include<string.h>
#include<fstream>
using namespace std;
main()
{
        unsigned long long T;
        ifstream in("in.in");
        ofstream out("output.out");
        in>>T;
        for(int z=0;z<T;z++)
        {
                string s,s1;
                int coun[10]{};
                in>>s;
                coun[0]=count(s.begin(),s.end(),'Z');
                coun[6]=count(s.begin(),s.end(),'X');
                coun[4]=count(s.begin(),s.end(),'U');
                coun[2]=count(s.begin(),s.end(),'W');
                coun[8]=count(s.begin(),s.end(),'G');
                coun[5]=count(s.begin(),s.end(),'F')-coun[4];
                coun[3]=count(s.begin(),s.end(),'R')-coun[0]-coun[4];
                coun[7]=count(s.begin(),s.end(),'S')-coun[6];
                coun[1]=count(s.begin(),s.end(),'O')-coun[0]-coun[2]-coun[4];
                coun[9]=count(s.begin(),s.end(),'I')-coun[5]-coun[6]-coun[8];
                out<<"Case #"<<z+1<<": ";
                for(int j=0;j<10;j++)
                        for(int k=0;k<coun[j];k++)
                                out<<j;
                out<<"\n";
        }
        in.close();
        out.close();
}
