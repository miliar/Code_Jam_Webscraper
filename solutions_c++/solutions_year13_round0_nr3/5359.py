#include <iostream>
#include <fstream>
#include <stack>

using namespace std;

int main()
{
    ifstream in;
    ofstream ou;
    int testcase;
    int fairsq[]={1,4,9,121,484,1001};
    int a, b, id1, id2,i,j;
    in.open("C.in", ifstream::in);

    if(in.is_open())
    {
        ou.open("result2.out");
        if(ou.is_open())
        {
            in>>testcase;
            cout<<testcase<<endl;
            for(i=0;i<testcase;i++)
            {
                id1=id2=0;
                in>>a>>b;
                cout<<a<<" "<<b<<endl;
                for(j=0;j<5;j++){
                    cout<<"CEK "<<a<<" "<<fairsq[j]<<endl;
                    if(a<fairsq[j]){id1=j;break;}}
                for(j=0;j<5;j++){
                    cout<<"CEK "<<b<<" "<<fairsq[j]<<endl;
                    if(b<fairsq[j]){id2=j;break;}}
                cout<<id1<<" "<<id2<<endl;
                cout<<"Case #"<<i+1<<": "<<id2-id1<<endl;
                ou<<"Case #"<<i+1<<": "<<id2-id1<<endl;
            }
           ou.close();
        }
        in.close();
    }


    return 0;
}
