#include<iostream>
using namespace std;

int main()
{

int T,s, nof, cno;
char *nos;
cin>>T;
for (int j=1; j<=T; j++)
{
    cin>>s;
    nos = new char(s+1);
    cin>>nos;
    nof = 0; cno = nos[0] - '0';
    for (int i=1; i<=s; i++)
    {
        if (cno >= i)
            cno = cno + (nos[i]  - '0');
        else
        {
            nof = nof + 1;
            cno = cno + 1;
            cno = cno + (nos[i]  - '0');
        }
    }
    cout<<"Case #"<<j<<": "<<nof<<"\n";
    delete nos;
}
}
