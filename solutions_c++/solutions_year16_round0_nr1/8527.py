#include <bits/stdc++.h>

using namespace std;

string func (int n)
{
    stringstream ss;
    ss<<n;
    string txt;
    ss>>txt;
    return txt;
}
set<int> s;
void insrt(string txt,int val)
{
    int ant=0;
    for(int a=txt.size()-1;a>=0;a--)
    {
        s.insert(((txt[a]-'0')*val+ant)%10);
        ant=((txt[a]-'0')*val+ant)/10;
    }
    while(ant>0)
    {
        s.insert(ant%10);ant/=10;
    }
}
int main()
{
    int casos,n,c;
     freopen ("out.txt","w",stdout);
    cin>>casos;
    string txt;
    for(int caso=1;caso<=casos;caso++)
    {
        cin>>n;
        txt=func(n);
        printf("Case #%d: ",caso);
        if (n==0)
        {
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        s.clear();
        c=1;
        while(s.size()!=10)
        {
            insrt(txt,c);
            c++;
        }
        cout<<n*(c-1)<<endl;

    }
}
