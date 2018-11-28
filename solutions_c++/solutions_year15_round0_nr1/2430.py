#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("A-large.in");
    ofstream out("A-large.out");
    int i, j,T, s, c, stdup;
    char arr[1010];
    in>>T;
    for(i=1; i<=T; i++)
    {
        stdup=0;
        s=0;
        c=0;
        for(j=0; j<1010; j++)
        {
            arr[j]=0;
        }
        in>>s;
        for(j=0; j<s+1; j++)
        {
            in>>arr[j];
        }


        for(j=0; j<s+1; j++)
        {
            if(j>stdup && arr[j]!='0')
            {
                c+= (j-stdup);
                stdup+=((arr[j]-48)+(j-stdup));
            }
            else
                stdup+=(arr[j]-48);
        }
        out<<"Case #"<<i<<": "<<c<<endl;
    }
    return 0;
}
