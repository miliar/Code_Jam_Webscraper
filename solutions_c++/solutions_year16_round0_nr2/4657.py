#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<map>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    long long int n,t,cpt;
    string S,S1;
    cin>>t;
    int k=1,x=0;
    while(t--)
    {
        S.clear();
        x=0;
        cpt=0;

        cin>>S1;
        S.push_back(S1[0]);
        for(int i=0;i<S1.size();i++)
        {
            if(S[x]!=S1[i])
            {
                x++;
                S.push_back(S1[i]);
            }
        }
        //cout<<S<<"\t"<<S1<<endl;
        cout<<"Case #"<<k<<": ";
        k++;
        bool b=false;
        if(S[0]=='-' && S.size()==1)
            cpt++;

        for(int i=0;i<S.size()-1;i++)
        {
                if(S[i]!=S[i+1])
                    b=true;

            if(b)
            {
                if(S[i]=='-')
                    cpt++;
                else
                {
                    cpt+=2;
                    i++;
                }
                b=false;
            }
        }
        cout<<cpt<<endl;
    }

}
