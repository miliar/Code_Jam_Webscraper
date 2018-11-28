#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int T,x=1;
    cin>>T;
    while(T--)
    {
        string S="";
        cin>>S;
        int count=0;
        for(int i=0;i<S.length()-1;i++)
        {
            if(S[i]!=S[i+1])
            {
                for(int j=0;j<=i;j++)
                    S[j]=S[i+1];
                count++;
            }
        }
        if(S[0]=='-')
            count++;
        cout<<"Case #"<<x++<<": "<<count<<endl;
    }
    return 0;
}
