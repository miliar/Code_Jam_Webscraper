#include<iostream>
#include<cstdio>
#include<string>
#define mp make_pair

using namespace std;

int main()
{
    int i,j,k,t,Case,X,R,C;
    freopen("Input_3.in","r",stdin);
    freopen("Output.txt","w",stdout);
    string s;
    cin>>t;
    Case=0;
    while(t--)
    {
        Case++;
        cin>>X>>R>>C;
        if(R<C) swap(R,C);
        if(X>R&&X>C)
        {
            s="RICHARD";
        }
        else if((R*C)%X!=0)
        {
            s="RICHARD";
        }
        else
        {
            if(X<=2)
            {
                s="GABRIEL";
            }
            else if(X==3)
            {
                if(C<=1)
                {
                    s="RICHARD";
                }
                else
                {
                    s="GABRIEL";
                }
            }
            else if(X==4)
            {
                if(C<=2)
                {
                    s="RICHARD";
                }
                else
                {
                    s="GABRIEL";
                }
            }
        }
        cout<<"Case #"<<Case<<": "<<s<<endl;
    }
    return 0;
}

