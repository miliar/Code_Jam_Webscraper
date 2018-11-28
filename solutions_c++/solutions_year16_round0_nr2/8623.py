#include <bits/stdc++.h>

using namespace std;
map<string,int> peso;
string nuevo;
string func(string algo,int rev)
{
    for(int a=0;a<rev;a++)
    {
        if (algo[a]=='+')algo[a]='-';
        else algo[a]='+';
    }
    reverse(algo.begin(),algo.begin()+rev);
    return algo;
}
int main()
{
    int casos,n,c;
     freopen ("out.txt","w",stdout);
    cin>>casos;
    string txt,txt2;int a,resp;
    for(int caso=1;caso<=casos;caso++)
    {
        cin>>txt;
        txt2=string(txt.size(),'+');
        a=0;resp=0;
        while(a<txt.size())
        {
            while(a<txt.size() && txt[a]==txt[a+1])
            {
                a++;
            }

            //cout<<txt<<endl;
            if (txt==txt2)
            break;
            resp++;
            a++;
            txt=func(txt,a);
            //cout<<txt<<endl;
        }
        if (txt!=txt2)
            resp++;
        printf("Case #%d: %d\n",caso,resp);
    }
}
