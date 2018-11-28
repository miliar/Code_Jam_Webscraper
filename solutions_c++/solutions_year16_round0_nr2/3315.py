#include <iostream>

using namespace std;

int main() {
    int T,a,b;
    string S;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cout<<"Case #"<<t<<": ";

        cin>>S;

        if(S.size()==1)
        {
            if(S[0]=='+')
                cout<<0<<endl;
            else
                cout<<1<<endl;
            continue;
        }

        a=0;
        b=0;

        for(int i=0;i<S.size()-1;i++)
        {
            if(S[i]=='+' && S[i+1]=='-')
                a++;
            else if(S[i]=='-' && S[i+1]=='+')
                b++;
        }

        if(a==b+1)
            cout<<2*a<<endl;
        else if(b==a+1)
            cout<<a+b<<endl;
        else if(S[0]=='+')
            cout<<2*a<<endl;
        else
            cout<<2*a+1<<endl;
    }
    return 0;
}