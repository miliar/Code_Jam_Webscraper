#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    int t=0,nt=0;
    cin>>t;
    nt=t;
    while(t--)
    {
        char str[20];
        char inp[20];
        cin>>inp;
        int pos = 0;
        char c;
        int l = strlen(inp);
        for(int i = 0 ; i<l ; i++,pos++)
        {
            c=inp[i];
            if(pos == 0)
            {
                str[pos]=c;
                continue;
            }
            if(c>str[pos-1] && c<str[0])
            {
                str[pos]=c;
            }
            else if(c>=str[0])
            {
                int k=pos-1;
                for(;k>=0;k--)
                {
                    str[k+1]=str[k];
                }
                str[0]=c;
            }
            else
                str[pos]=c;
            //cout<<"just put "<<c<<" in place and str is : "<<str<<endl;
        }
        str[pos]='\0';
        cout<<"case #"<<(nt-t)<<": "<<str<<endl;
    }
    //cout << "Hello world!" << endl;
    return 0;
}
