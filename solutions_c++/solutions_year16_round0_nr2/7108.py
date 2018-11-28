#include <iostream>
#include <string>
using namespace std;

int main()
{
    int t=0,nt=0;
    cin>>t;
    nt=t;
    while(t--)
    {

    string str;
    cin>>str;
    int val=0;
    char prev,cur;
    prev=str.at(0);
    if(prev=='-')
        val=1;
    int l = str.length();
    //cout<<str<<endl;
    //cout<<l<<endl;
    for(int i=1;i<l;i++)
    {
        cur=str.at(i);
        //cout<<"cur : "<<cur;
        if(cur=='+')
            {
                prev=cur;
                //cout<<" now its plus so nothing!"<<endl;
                continue;
            }
        if(prev=='-')
            {
                prev=cur;
                //cout<<" two minus in a row..."<<endl;
                continue;
            }
        if(prev=='+')
        {
            //cout<<" val plussed by two , prev = "<<prev<<endl;
            val+=2;
        }
        prev=cur;
    }
    cout<<"Case #"<<(nt-t)<<": "<<val<<endl;
    //cout << "Hello world!" << endl;
    }
    return 0;
}
