#include <iostream>
#include <string.h>
#include <cstdio>


using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    char S[100][1001];

    cin>>T;
    cin.getline(S[0],1000);
    for(int i=0;i<T;i++)
    {
        cin.getline(S[i],1000);
    }

    char test[1001];
    int len,outLen;
    int start,end,inPlace;

    for(int i=0;i<T;i++)
    {
        outLen=0;
        strcpy(test,"");
        start = end = -1;
        len=strlen(S[i]);
        //cout<<endl<<endl<<len<<"\t"<<S[i];
        for(int j=0;j<len;j++)
        {
            outLen++;
            if((start == end)&&(end==-1))
            {

               start = 0;
               end = 0;
               inPlace = 0;
               test[0]= S[i][j];
            }
            else
            {
                if(S[i][j] >= test[start])
                {
                    end++;
                    inPlace = start;
                    for(int k=outLen-1;k>=0;k--)
                    {
                        test[k+1] = test[k];
                    }
                    test[inPlace]= S[i][j];
                }
                else
                {
                    end++;
                    inPlace = end;
                    test[inPlace]= S[i][j];
                }
            }
        }
        test[end+1] = '\0';
        if(i!=0)
            cout<<"\n";
        cout<<"Case #"<<i+1<<": "<<test;
    }


    return 0;
}
