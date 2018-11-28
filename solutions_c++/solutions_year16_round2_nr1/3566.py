#include <iostream>
#include <bits/stdc++.h>
using namespace std;


#define READ(filename)  freopen(filename, "r", stdin);
#define WRITE(filename)  freopen(filename, "w", stdout);
int main()
{
    READ("inp.txt");
    WRITE("OUTPUT.txt");
    int t;
    cin>>t;
    char st[2010];
    int count1[30];
    int counter=0;
    int ans[20];
    while(t--)
    {
        counter++;

        cin>>st;
        memset(count1, 0 ,sizeof count1);
        for(int i=0;i<strlen(st);i++)
        {
            count1[int(st[i])-65]++;
        }
        ans[0]=count1[int('Z')-65];
        ans[2]=count1[int('W')-65];
        ans[4]=count1[int('U')-65];
        ans[6]=count1[int('X')-65];
        ans[8]=count1[int('G')-65];
        ans[7]=count1[int('S')-65]-ans[6];
        ans[5]=count1[int('F')-65]-ans[4];
        ans[3]=count1[int('H')-65]-ans[8];
        ans[1]=count1[int('O')-65]-ans[0]-ans[2]-ans[4];
        ans[9]=count1[int('I')-65]-ans[5]-ans[6]-ans[8];

        cout<<"Case #"<<counter<<":"<<" ";
        for(int i=0;i<10;i++)
        {
            while(ans[i]>0){
                cout<<i;
                ans[i]=ans[i]-1;
                }
        }
        cout<<endl;

        /*
        if(count[int('Z')-65]!=0)
            ans[0]=0;
        if(count[int('R')-65]!=0)
            ans[0]=4;
        if(count[int('X')-65]!=0)
            ans[0]=6;
        if(count[int('G')-65]!=0)
            ans[0]=8;
        if(count[int('W')-65]!=0)
            ans[0]=2;
        if(count[int('H')-65]==)
        if(count[int('V')-65]!=0)
            ans[0]=7 or 5;
        if(count[int('N')-65]==1)
            ans[0]=1;
        if(count[int('N')-65]==2)
            ans[0]=9;
        if(count[int('N')-65]==3)
            ans[0]=1 and 9;*/
    }
    return 0;
}
