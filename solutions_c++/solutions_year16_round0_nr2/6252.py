#include<iostream>

using namespace std;

int main()
{
//    freopen("c:\\users\\raman\\desktop\\in.in","r",stdin);
//    freopen("c:\\users\\raman\\desktop\\out.txt","w",stdout);

    int t; cin>>t;
    for(int i=1;i<=t;i++)
    {
        string s,tmp; cin>>s;
        int len=s.length(),cnt=0,aa=0;
        bool a;

        for(int j=0;j<len;j++)
            if(s[j]=='+')
                aa++;


        while(1)
        {
            if(aa==len)
            {
                cout<<"Case #"<<i<<": "<<cnt<<endl;
                break;
            }
            if(s[0]=='+')
            {
                int k=0;
                while(s[k]=='+')
                    {
                        s[k++]='-';
                        aa--;
                    }
                cnt++;
            }
            else
            {
                int k=0;
                while(s[k]=='-')
                    {
                        s[k++]='+';
                        aa++;
                    }

                cnt++;
            }
        }
    }
}
