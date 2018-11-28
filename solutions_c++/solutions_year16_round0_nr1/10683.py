#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <sstream>
#include <fstream>
#include <string>
#include <cstring>
#include <vector>

using namespace std;

unsigned long long toi64(string s) {unsigned long long v;istringstream sin(s);sin>>v;return v;}
template<class T> string tostring(T x) {ostringstream sout;sout<<x;return sout.str();}
template<class T> int toint( T s ) {int v;istringstream sin( tostring(s) );sin>>v;return v;}
inline int s2i( string a ){return atoi( a.c_str() );}
double todouble(string s) {double v;istringstream sin(s);sin>>v;return v;}


vector<string> tokenize(const string& str, const string& d = " "){vector <string> t;int up  = str.find_first_not_of(d, 0);int pos = str.find_first_of(d, up);while (string::npos != pos || string::npos != up){t.push_back(str.substr(up, pos - up));up = str.find_first_not_of(d, pos);pos = str.find_first_of(d, up);}return t;}


void trim( string& c ){if( c.size() == 0 ) return;int i , p = -1 , q = -1;for( i = 0; i < c.size(); ++ i )if( int(c[i])%255 > int(' ') ){p = i;break;}for( i = c.size()-1; i >= 0; -- i )if( int(c[i])%255 > int(' ') ){q = i;break;}c = p == -1 ? "" : c.substr(p,q-p+1);}
inline string trimm( string c ){string s(c);trim(s);return s;}
int v[10]={0};
bool numbers(int x)
{
    string s = tostring(x);
    for(int i = 0 ;i<s.size(); i++)
    {
        if(v[int(s[i]-48)]==0)
            v[int(s[i]-48)]=1;
        //cout<<v[i]<<" ";
    }
   // cout<<endl;
    for(int i = 0 ;i<10; i++)
    {
        if(v[i]!= 1)
            return 0;
    }

    return 1;
}

int main()
{
    freopen("A-larg.in","r",stdin);
    freopen("out.txt","w",stdout);

    unsigned long long n,x,i=1,m=1;
    cin>>n;
    while(n--)
    {
        cin>>x;
        for(int i = 0 ;i<10; i++)
        {
            v[i]=0;
        }

        if(x==0)
        {
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
        }
        else
        {
            m=1;
            while(!numbers(x*m))
            {
                m++;
                //cout<<x*m<<endl;
            }
            cout<<"Case #"<<i<<": "<<x*m<<endl;

        }
        i++;

    }

    return 0;
}
