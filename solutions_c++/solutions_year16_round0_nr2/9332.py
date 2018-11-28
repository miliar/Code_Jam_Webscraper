#include<bits/stdc++.h>
using namespace std;
char ar[110];

int main()
{

    int t,t1,i,j,res;
    cin>>t;


    for(t1=1;t1<=t;t1++)
    {
        scanf("%s",ar);

        res=0;
            if(ar[0]=='-')
            res=1;

            for(i=1;ar[i]!='\0';i++)
            {
                if(ar[i]=='-'&&ar[i-1]=='+')
                res+=2;

            }

         cout<<"Case #"<<t1<<":  ";
        cout<<res<<endl;


    }

    return 0;
}

