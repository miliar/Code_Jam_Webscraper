#include<bits/stdc++.h>

using namespace std;

int main()
{
    int t,i=1,sum,n,sol,j,x;
    string input;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>n;
        cin.ignore();
        getline(cin,input);
        sum=input[0]-48;
        sol=0;
        for(j=1;j<=n;j++)
        {
            x=input[j]-48;
            if(x>0)
            {
                if(j<=sum){sum+=x;}
                else{sol+=(j-sum);sum+=x+(j-sum);}
            }

        }
        cout<<"Case #"<<i<<": "<<sol<<endl;
        input.clear();
    }


    return 0;
}
