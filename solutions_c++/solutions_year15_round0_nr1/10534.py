#include<iostream>
using namespace std;
int t,smax;
string s;
int cnt=0,cou=0;
int a[1000];
int idex=0;
int main()
{
    cin>>t;
    for(int cases=1;cases<=t;cases++)
    {
        cin>>smax;
        cin>>s;
        for(int j=smax;j>=0;j--)
        {
            int y=s[j]-'0';
            if(y>0)
            {
                idex=j;
                break;
            }
        }
        for(int i=0;i<=idex;i++)
        {
            int x=s[i]-'0';
            if(x>0)
            {
                cnt=cnt+x;
            }
            else
            {
                if(cnt<=i)
                {
                    cnt++;
                    cou++;
                }
            }
        }
        cout<<"Case #"<<cases<<": "<<cou<<endl;
        cou=0;
        cnt=0;

    }
}
