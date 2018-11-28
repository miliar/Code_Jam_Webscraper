#include<iostream>
#include<string>
using namespace std;
int main()
{
    int t;
    string s,s1,s2;
    cin>>t;
    // cout<<t<<endl;
    int l,i;
    long long int c;
    int x=0;
    while(t--)
    {
        cin>>s;
        c=0;
        x++;
        s1=s2="";

        l=s.length();
        // cout<<s<<' '<<l<<endl;
        for(i=0;i<l;i++)
        {
            s1=s1+"-";
            s2=s2+"+";
        }
        // cout<<s1<<"\n"<<s2<<endl;
        if(s1.compare(s)==0)
            cout<<"Case #"<<x<<": "<<1<<endl;
        else
            if(s2.compare(s)==0)
            cout<<"Case #"<<x<<": "<<0<<endl;
        else
        {
            s1="";
            while(s2.compare(s)!=0)
            {
            int posp=-1;
            for(i=0;i<l;i++)
            {
                if(s[i]!='+')
                break;
                else
                    posp=i;
            }
            // cout<<posp<<endl;
            if(posp!=-1)
            {
                for(i=0;i<=posp;i++)
                    s1+='-';
                for(i=posp+1;i<l;i++)
                    s1+=s[i];
                s=s1;
                c++;
                s1="";// changing initial +s
            }
            int posln=-1;
            for(i=l-1;i>=0;i--)
                {if(s[i]=='-')
                {posln=i;break;}
                }
                // cout<<posln<<endl;
            for(i=0;i<=posln;i++)           //reversing till last -ve
            {
                if(s[posln-i]=='+')
                    s1+='-';
                else
                    s1+='+';
            }
            c++;
            for(i=posln+1;i<l;i++)
                s1+=s[i];
            s=s1;
            s1="";
            // cout<<s<<endl;
            }
            cout<<"Case #"<<x<<": "<<c<<endl;
        }

    }
    return 0;
}
