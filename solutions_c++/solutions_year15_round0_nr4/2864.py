#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int a[4],b[4],caseNo=1,t,temp,i,j,x,r,c;
    ifstream input;
    ofstream output;
    output.open("output.txt");
    input.open("input.txt");
    input>>t;
    //cout<<t;
    while(caseNo<=t)
    {
        input>>x>>r>>c;
        switch(x)
        {
            case 1:
                output<<"Case #"<<caseNo<<": "<<"GABRIEL"<<endl;
                break;
            case 2:
                if((r*c)%2==0)
                    output<<"Case #"<<caseNo<<": "<<"GABRIEL"<<endl;
                else
                    output<<"Case #"<<caseNo<<": "<<"RICHARD"<<endl;
                break;
            case 3:
                if(r>1 && c>1 && (r*c)%3==0)
                    output<<"Case #"<<caseNo<<": "<<"GABRIEL"<<endl;
                else
                    output<<"Case #"<<caseNo<<": "<<"RICHARD"<<endl;
                break;
            case 4:
                if(r>2 && c>2 && (r*c)%4==0)
                    output<<"Case #"<<caseNo<<": "<<"GABRIEL"<<endl;
                else
                    output<<"Case #"<<caseNo<<": "<<"RICHARD"<<endl;
                break;
        }
        caseNo++;
    }
    input.close();
}
