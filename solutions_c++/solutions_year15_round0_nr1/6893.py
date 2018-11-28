#include<iostream>
#include <fstream>
#include <math.h>
#include <unistd.h>
#include <stdlib.h>
using namespace std;
int main()
{

     freopen("input.in","r",stdin);
     freopen("output.out","w",stdout);
    int t;
    cin>>t;
    int temp = 1;
    while(t--)
    {
        int m;
        char s[10000];
        cin>>m>>s;
        int standing = 0,cnt = 0;
        for(int i=0; i<=m; i++)
        {
            int c = s[i]-'0';
            if(c>0)
            if(standing >= i)
            {

                    standing = standing +  c;


            }
            else
            {
                if(c>0)
                {
                    int remaining = abs(i-standing);
                    cnt = cnt + remaining ;
                    standing = standing + remaining;
                    standing = standing + c;
                //    cout<<remaining<<" ";
                }
            }
        //    cout<<standing<< " "<<cnt<<" ";
        }


         cout<<"Case #"<<temp<<": "<<cnt<<endl;
        temp++;
    }

    return 0;
}
