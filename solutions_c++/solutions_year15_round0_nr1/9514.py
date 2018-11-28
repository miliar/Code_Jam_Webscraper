
#include<cstdlib>
#include<iostream>
#include<fstream>

using namespace std;

int main() {
    int i,j,s_max,t,clapping,added;
    char audience[1002],t_max[3],period,s[6];
    ifstream in ("A-large.in");
    ofstream out ("outputs.out");
    in>>t_max;
    t=atoi(t_max);
    for(j=1;j<=t;j++)
    {
        in>>s_max;
        //s_max=atoi(s);
        in>>audience;
        i=0;
        clapping=0;
        added=0;
        while(i<=s_max)
        {
            if(clapping>=i)
            {
                clapping+=(audience[i]-48);
                i++;
            }
            else
            {
                added++;
                clapping++;
            }
                            
        }
        out<<"Case #"<<j<<": "<<added<<"\r\n";
    }
    in.close();
        
    return 0;
}
