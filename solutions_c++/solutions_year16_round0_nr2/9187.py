#include<iostream>

using namespace std;

int main()
{
    int t,t1;
    cin>>t;
    t1=t;
    while(t--)
    {
        string s;
        cin>>s;
        int i=0,l=s.length(),c=-1,flag=-1;
        while(i<l)
        {
            if(s[i]=='+' && flag!=1)
            {
                flag=1;
                c++;
            }
            if(s[i]=='-' && flag!=0)
            {
                flag=0;
                c++;
            }
            i++;
        }
        if(flag==0)
        {
            c++;
        }
        cout<<"Case #"<<t1-t<<": "<<c<<endl;
    }

    return 0;
}

