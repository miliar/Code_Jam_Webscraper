#include <iostream>
#include <string.h>
using namespace std;

void maneuver(string * PS, int P)
{
    string Top;
    for(int i=0; i<P; i++)Top+=PS[0][i];
    for(int i=0; i<P; i++)
    {
        if(Top[i]=='+') PS[0][P-1-i]='-';
        else PS[0][P-1-i]='+';
    }
}

int main()
{
    int T;//the number of test cases
    cin>>T;
    string S[T];
    //read all inputs
    for(int i=0; i<T; i++)
        cin>>S[i];
    //calculate and print all outputs
    for(int x=0; x<T; x++)
    {
        cout<<"\nCase #"<<x+1<<": ";
        int y=0;
        for(int i=1; i<S[x].size(); i++)
        {
            if(S[x][i]!=S[x][i-1])
            {
                //execute the maneuver
                maneuver(&S[x],i);
                y++;
            }
        }
        if(S[x][0]=='-')
        {
            maneuver(&S[x],S[x].size());
            y++;
        }
        cout<<y;
    }
    cin.get();
    cin.get();
    cin.get();
}
