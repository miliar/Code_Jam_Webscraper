#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool l[101];

void flip(int t)
{
    for(int i=1;i<=t;i++) l[i] = !l[i];
}

int convert(string t)
{
    for(int i=0;i<t.length();i++)
    {
        if (t[i] == '+') l[i+1] = true;else l[i+1] = false;
    }
    return t.length();
}

int main()
{
    int test;
    ofstream opf;
    ifstream ipf;
    ofstream opf2;
    ipf.open("B-large.in");
    opf2.open("output2.txt");
    opf.open("output.txt");
    ipf >>test;
    ipf.ignore();
    for (int j =1;j<=test;j++)
    {
    string t;
    getline(ipf,t);
    opf2 << j << " " << t <<endl;
    int n = convert(t);
    int res =0;
    int co =0;
    for(int i=1;i<=n;i++) if (l[i]) co++;
    if (co == n) opf << "Case #" <<j<< ": " <<0<<endl;
    while(co!=n)
    {
        if (!l[1])
        {
            int c =1;
            while (!l[c] && c<n) c++;
            if (c == n && !l[c])
            {
                opf << "Case #" <<j<< ": " <<res +1<<endl;
                break;
            }
            c= c-1;
            flip(c);
            res++;
            co =0;
            for(int i=1;i<=n;i++) if (l[i]) co++;
            if (co == n)
            {opf << "Case #" <<j<< ": " <<res<<endl;break;}
        }
        else
        {
            int c =1;
            while (l[c] && c<n) c++;
            if ( c == n && l[c]){
                opf << "Case #" <<j<< ": " <<res<<endl;
                break;
            }
            c= c-1;
            flip(c);
            res++;
        }
        co =0;
        for(int i=1;i<=n;i++) if (l[i]) co++;
    }
    }
}
