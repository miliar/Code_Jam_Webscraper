#include<iostream>
#include<fstream>
#include<string>
using namespace std;
#define ll long long int

string reverse(int l, int u, string &s);

ll parse(string &s)
{
    int len = s.length();
//    out << len;
    ll iter = 0;
    char prev = s[0];
    if(len>1)
      {
        for(int i=1; i<len; i++)
        {
            if(s[i]==prev)
            {
                ;// move ahead
            }
            else
            {
                s = reverse(0, i-1, s);
                iter++;
                prev = s[i];
            }
           // out << "length = " << len << endl;
            if(i==(len-1) && s[i]=='-')
            {
                s = reverse(0,len-1,s);
                iter++;
            }
        }
    }
    else
    {
       if(len==1 && s[0]=='-')
       {
           s = reverse(0,len-1, s);
           iter++;

       }
    }
    //out << s << " ";
    //out << "iter = " << iter << endl;
    return iter;
}

inline string reverse(int l, int u, string &s)
{
    for(int i=l; i<u+1; i++)
    {
        if(s[i]=='-') s[i] = '+';
        else s[i] = '-';
    }

    return s;
}

int main()
{
    ifstream file;
    ofstream out("/Users/Az/Dropbox/codejam/16_2/out");
    file.open ("/Users/Az/Dropbox/codejam/16_2/inp");
    int n;
    string s;
    file >> n;
    int counter = 1;
    while(n--)
    {
        file >> s;
        ll res = parse(s);
        out << "Case #"<<counter++<<": "<<res << "\n";
    };
}
