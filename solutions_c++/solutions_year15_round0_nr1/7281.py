#include <iostream>
#include<fstream>

using namespace std;


int main()
{
    int t,smax,ch[1001],ans[100],n=0;
    char s[1001];
    fstream file;
    file.open("inputl.in",ios::in);
    file>>t;
    for(int i=0;i<t;i++)
    {
        file>>smax;
        for(int j=0;j<=smax;j++)
        {
            file>>s[j];
            ch[j]=s[j]-48;
        }


        ans[i]=0;n=0;
        for(int j=0;j<=smax;j++)
        {
            if(n>=j)
            n=n+ch[j];
            else
            {
                ans[i]=ans[i]+(j-n);
                n=n+ch[j]+(j-n);
            }
        }


        }

    file.close();
    file.open("uotputl.out",ios::out);
    for(int i=0;i<t;i++)
    file<<"Case #"<<i+1<<": "<<ans[i]<<endl;
    file.close();
    return 0;
}
