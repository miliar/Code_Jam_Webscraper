#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

void megold(istream& in, ostream &out)
{
    int n;
    int c[102][102];//count
    char chrs[102], chr2[102];
    for(int i=0; i<102; i++) chr2[i]=0;
    int len;


    in>>n;
    for(int i=0; i<n; i++)
    {
        string s;
        in>>s;

        int j=0;
        chrs[j]=s[0];
        c[i][0]=1;
        for(int k=1; k<s.length(); k++)
        {
            if(s[k]==chrs[j]) c[i][j]++;
            else {
                j++;
                chrs[j]=s[k];
                c[i][j]=1;
            }
        }
        if(i!=0) {
            for(int k=0; k<=j; k++) {
                if(chr2[k]!=chrs[k] || len!=j)
                {
                    out<<"Fegla Won";
                    return;
                }
            }
        } else {
            memcpy(chr2, chrs, 101);
            len=j;
        }
    }

    len++;
    /*for(int i=0; i<n; i++)
    {
        for(int j=0; j<len; j++)
        {
            cout<<c[i][j]<<' ';
        }
        cout<<endl;
    }

    for(int j=0; j<len; j++)
    {
        cout<<chr2[j]<<' ';
    }
    cout<<endl;
    cout<<endl;*/

    int ret=0;
    for(int j=0; j<len; j++)
    {
        int minv;
        minv=1000000;
        for(int k=1; k<=100; k++)
        {
            int val=0;
            for(int i=0; i<n; i++) val+=abs(c[i][j]-k);

            if(val<minv) {
                minv=val;
            }
        }

        ret+=minv;
    }

    out<<ret;
}

int main()
{
    ifstream in("A-small-attempt0.in");
    ofstream out("equ.out");
    int n;
    in>>n;
    for(int i=1; i<=n; i++)
    {
        out<<"Case #"<<i<<": ";
        megold(in, out);
        out<<endl;
    }
    in.close();
    out.close();
    return 0;
}
