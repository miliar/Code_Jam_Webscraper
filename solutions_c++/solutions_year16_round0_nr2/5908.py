#include <iostream>

using namespace std;

int main()
{
    int t,T=0; cin>>t;

    while(t--)
    {
T++;

    string ipt;
    cin>>ipt;
    int i,j[101],k=0,l=0;
    j[0]=-2;
    for(i=0;ipt[i]!='\0';i++)
    {
        if(ipt[i]=='-')
        {
            k++;
            j[k]=i;
        }
        }
        int shifts=0;
        for(l=1;l<=k;l++)
        {

            int diff= j[l]-j[l-1];
            if(j[l]==0) shifts++;
            else {if(diff==1 or diff==-2) shifts=shifts;
                 else shifts=shifts+2;}
        }
             cout<<"Case #"<<T<<": "<<shifts<<endl;
    }
             }


