#include<iostream>
#include<stdlib.h>
#include<cstring>
#include<fstream>
using namespace std;
int main()
{
    int a[4],b[4],caseNo=1,t,i,j,s;
    int shy,st,ne;
    char l[1005],no[5];
    ifstream input;
    ofstream output;
    output.open("output.txt");
    input.open("input.txt");
    input>>t;
    //cout<<t;
    while(caseNo<=t)
    {
        input>>s;
        input>>l;
        st=0;
        no[0]=l[0];
        shy=atoi(no);
        st=shy;
        ne=0;
        for(i=1;i<strlen(l);i++)
        {
            no[0]=l[i];
            shy=atoi(no);
            if(st<i)
            {
                ne+= i-st;
                st+= i-st;
            }
            st+=shy;
        }
        output<<"Case #"<<caseNo<<": "<<ne<<endl;
        caseNo++;
    }
    input.close();
}
