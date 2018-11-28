#include<cstring>
#include<fstream>
#include<iostream>
using namespace std;

char rev(char c)
{
    if(c=='+')
        return '-';
    return '+';
}

int check(char *s,int n)
{
    int flag=1;
    for(int i=0;i<n;i++)
    {
            if(s[i]=='-')
            {
                flag=0;
                break;
            }

    }
    return flag;
}

int main()
{
        std::ifstream infile("B-small-attempt0.in");

        int T;
        infile>>T;
        int *ans=new int[T];
        for(int i=0;i<T;i++)
        {
            char s[100];
            char firstchar;
            infile>>s;
            int j,length=strlen(s);

            for(j=0;!(check(s,length));j++)
            {
                firstchar=s[0];
                s[0]=rev(s[0]);
                for(int k=1;s[k]==firstchar && s[k]!='\0';k++)
                {
                    s[k]=rev(s[k]);
                    if(s[k+1]!=firstchar)   break;
                }
            }
            ans[i]=j;
        }
        ofstream outfile;
        outfile.open("test.txt");
        for(int i=0;i<T;i++)
            outfile<<"Case #"<<(i+1)<<": "<<ans[i]<<endl;

        return 0;
}
