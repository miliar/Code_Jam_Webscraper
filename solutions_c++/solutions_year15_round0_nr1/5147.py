#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    //freopen("a_input.txt","r",stdin);
    //freopen("a_output.txt","w",stdout);
    int NumberOfCases;
    cin>>NumberOfCases;
    int maxShy,friendNeeded,attendee;
    string shyString;
    for(int caseNo=1;caseNo<=NumberOfCases;caseNo++)
    {
        cin>>maxShy>>shyString;
        friendNeeded=0;
        attendee=shyString[0]-48;
        for(int i=1;i<=maxShy;i++)
        {
            if(attendee>=i)
            {
                attendee+=(shyString[i]-48);
            }
            else
            {
                friendNeeded+=(i-attendee);
                attendee+=(i-attendee)+(shyString[i]-48);
            }
        }
        cout<<"Case #"<<caseNo<<": "<<friendNeeded<<endl;
    }
}
