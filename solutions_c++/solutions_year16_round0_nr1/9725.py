#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{


    int t;
    cin>>t;
    int et=1;
    freopen("new.txt","w",stdout);
    while(t--){
    int A[10]={0};
        long long int n;
        cin>>n;

        int c=1;
        long long int u=n;
        int re=1000;

    while((c==1)&&(re>0)){

        long long int e=u;
        while(e!=0)
        {
           int r=e%10;
            e=e/10;
            A[r]=1;

        }
        int i,cn=0;
        for(i=0;i<=9;i++)
            if(A[i]==1)
            cn++;
        if(cn==10)
            c=0;
        u=u+n;

        re--;
    }

    if(c==0)
        cout<<"Case "<<"#"<<et<<": "<<(u-n)<<endl;
    else
        cout<<"Case "<<"#"<<et<<": "<<"INSOMNIA"<<endl;
et++;
    }

fclose(stdout);
    return 0;
}
