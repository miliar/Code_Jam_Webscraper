#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

string s;
int c=0;

void cserel1()
{
    int i=0;
    while(s[i]=='+')
    {
        s[i]='-';
        i++;
    }
    if(i!=0) c++;

}

void cserel2()
{
    string seged=s;
for(int i=0; i<s.size(); ++i)
{
    s[i]=='-' ? seged[s.size()-1-i]='+' : seged[s.size()-1-i]='-';
}
s=seged;
}

void csonkol()
{
    int i=s.size()-1;
    while(s[i]=='+')
        {
        if(i==0) {s=""; return;}
        i--;
        }
        s=s.substr(0,i+1);
        c++;
}
bool kesz(vector<bool> v)
{
    for(int i=0; i<v.size(); ++i)
        {if(v[i]==false) return false;}
    return true;

}

/*void vegez(vector<bool> &v)
{
    int i=v.size()-1;
    while(v[i]) {i--;}
    for(int j=0; j<i;)

}*/
int main()
{
    ifstream f;
    ofstream g;
    string fname="2.txt";
    string gname="2_ki.txt";


    f.open(fname.c_str());
    g.open(gname.c_str());
    int n;
    getline(f,s);
    stringstream ss;
    ss<<s;
    ss>>n;
    for(int i=0;i<n; ++i)
    {
         c=0;
        s.clear();
        getline(f,s);
         csonkol();
        while(!s.empty())
        {
           cserel1();
           cserel2();
           csonkol();
        }
        cout<<"Case #"<<i+1<<": "<<c<<endl;
        g<<"Case #"<<i+1<<": "<<c<<endl;
















      /*  vector<bool> p(s.size());
        for(int j=0; j<p.size(); ++j)
            p[j] = (s[j]=='+' ? true : false);
        int c=0;
        while(true)
        {
            if(kesz(p))
            {
                cout<<"Case #"<<i+1": "<<c<<endl;
                break;
            }
            else
            {
            vegez(p);
            c++;
            }

        }*/

    }
    return 0;
}
