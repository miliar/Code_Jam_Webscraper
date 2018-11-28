#include <iostream>
#include <string.h>
#include <cstdio>

using namespace std;
bool bigArray[101];
int stringLength;
bool checkHappy()
{
    int count  = 0;
    for(int i=0;i<stringLength;i++)
    {
        if(bigArray[i] == false)
            return false;
    }
    return true;
}

void flip(int n)
{
    int i;
    for(i=0;i<n;i++)
        bigArray[i]=!bigArray[i];
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int inpNum;
    char input[100][101];
    int p1End;
    bool pCheck;
    int j,i,flipCount;
    cin>>inpNum;

    for(i=0;i<inpNum;i++)
    {
        cin>>(input[i]);
    }
    for(i=0;i<inpNum;i++)
    {
        stringLength = strlen(input[i]);
        for(j=0;j<stringLength;j++)
        {
            if(input[i][j] == '+')
                bigArray[j] = true;
            else
                bigArray[j] = false;
        }
        pCheck = false;
        flipCount = 0;
        if(i!=0)
            cout<<"\n";
        while(!checkHappy())
        {
            pCheck = false;
            for(j=1; j<stringLength; j++)
            {
 //               cout<<"bigArray[j] ="<<bigArray[j] == bigArray[0]<<"\n";
                if(bigArray[j]!=bigArray[0])
                {
                    p1End = j;
                    pCheck = true;
                    break;
 //                   cout<<"Broke at "<<j<<endl;
                }
            }
            if(pCheck == false)
            {
                flip(stringLength);

//                cout<<"\n\tpCheck == false\t";
            }
            else
            {
                flip(p1End);
 //               cout<<"\n\telse\t"<<stringLength;
            }
            flipCount++;
//            for(int l =0; l<stringLength; l++)
//                cout<<bigArray[l]<<" ";
//            cout<<endl;
        }
        cout<<"Case #"<<i+1<<": "<<flipCount;
    }
    return 0;
}
