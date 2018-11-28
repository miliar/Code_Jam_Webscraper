#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdlib>
using namespace std;

long long res;

void check(vector<string*>& v)
{
    int occured[100];
    for(int i=0; i<('z'-'a'+20); i++) occured[i]=0;
    char prev=' ';

    for(int i=0; i<v.size(); i++) {
        for(int j=0; j<(*v[i]).size(); j++)
        {
            if(occured[(*v[i])[j]-'a']) {
                if(prev!=' ' && prev!=(*v[i])[j]) {

                    //cout<<" "<<i<<" "<<j<<endl;
                    return;
                }
            }
            prev=(*v[i])[j];
            occured[(*v[i])[j]-'a']=1;
        }
    }
    res++;
    res=res % 1000000007;
}

void permute(vector<string*>& v, const int n)
{
  if(n<1)
  {
    check(v);
    /*for(int i=0; i<v.size(); i++) {
        for(int j=0; j<(*v[i]).size(); j++)
        {
            cout<<(*v[i])[j];
        }
    }
    cout<<endl;*/
    return;
  }


    for (int i = 0; i<=n; i++) {
        string* t;
          t = v[i];
          v[i] = v[n];
          v[n] = t;
        permute(v, n-1);
        t = v[i];
          v[i] = v[n];
          v[n] = t;
    }

}

void megold(istream& in, ostream &out)
{
    int n;
    in>>n;
    vector<string*> v;
    res=0;
    for(int i=0; i<n; i++)
    {
        string *s=new string;
        v.push_back(s);
        in>>(*s);
    }
    permute(v, n-1);

    out<<res;
}

int main()
{
    ifstream in("B-small-attempt1.in");
    //ifstream in("test.in");
    ofstream out("cons.out");
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
