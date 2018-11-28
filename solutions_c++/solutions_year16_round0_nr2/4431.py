#include <iostream>
#include <bits/stdc++.h>
using namespace std;


#define READ(filename)  freopen(filename, "r", stdin);
#define WRITE(filename)  freopen(filename, "w", stdout);



int main()
{
    READ("inputlarge.txt");
    WRITE("outputlarge.txt");
    int t,counter=1;
    char st[105];
    cin>>t;
    while(t--)
    {
        cin>>st;
        int answer=0;
        for(int i=0;i<strlen(st);i++)
        {
            if(st[i]=='-')
                if(i==0)
                    answer+=1;
                else if(st[i-1]=='+')
                    answer+=2;
                else
                    continue;
        }
        cout<<"Case #"<<counter<<": "<<answer<<endl;
        counter++;
    }

    return 0;
}
