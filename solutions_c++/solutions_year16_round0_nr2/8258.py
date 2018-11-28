#include<bits/stdc++.h>
using namespace std;
bool d=false;
string change(string A)
{
    string B;
    int b=0,j,i=A.size()-1,S,flag2=0,flag=0,g;
    char f;
    S=i;

    for(j=i; j>=0; j--)
    {
        if(A[j]=='-')
        {
            b=1;
            break;
        }
    }
    int k=j;
    //cout<<"b"<<d<<endl;
    if(b==0)d=true;

    else if(A=="-")B+='+';
    else
    {
        for(i=1;;i++)
        {
            if(A[i]!=A[i-1])break;
        }
        f=A[i];
        //cout<<f<<endl;
        for(j=0;j<=i;j++)
        {
            B+=f;
        }
        for(j=(i+1);j<=S;j++)
        {
            B+=A[j];
        }

    }
    return B;
}
int main()
{
    ofstream myfile;
    myfile.open ("exampleB.txt");
    string L,res;
    int c=-1,n,i;
    while(cin>>n)
    {
        i=0;
        while(n--)
        {
            i++;
            cin>>L;
            d=false;
            c=-1;
            while(d!=true)
            {

                res=change(L);
                L=res;
          //      cout<<L<<endl;

                c++;
            }


            cout<<"Case #"<<i<<": "<<c<<endl;
            myfile<<"Case #"<<i<<": "<<c<<endl;


        }

    }


}




