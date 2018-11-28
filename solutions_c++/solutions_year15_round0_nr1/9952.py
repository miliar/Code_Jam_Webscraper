#include<iostream>
#include<stdio.h>
using namespace std;


int main()
{
    string str;
    int tc,maxShynessLevel,additionalGuests,tot;
    freopen("A-small-attempt1.in","r",stdin);
    freopen("result.txt","w",stdout);
    cin>>tc;
    for(int counter=0;counter<tc;counter++)
    {
        cin>>maxShynessLevel;
        cin>>str;
        tot=0;
        additionalGuests=0;
        tot+=(str[0]-'0');
        for(int counterS=1;counterS<=maxShynessLevel;counterS++)
        {

            //cout<<tot<<"-"<<counterS<<endl;
            if((counterS>tot)&&(str[counterS]!='0'))
            {
                additionalGuests+=(counterS-tot);
                tot+=additionalGuests;
            }
            //cout<<tot<<"-"<<additionalGuests<<endl;
            tot+=(str[counterS]-'0');
            //cout<<tot<<endl;
        }
        cout<<"Case #"<<counter+1<<": "<<additionalGuests<<endl;
    }
    return 0;
}
