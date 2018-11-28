
#include<iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int k=0;k<t;k++)
    {

        string str;
        cin>>str;
cout<<"Case #"<<(k+1)<<": ";
        int swaps=0;
        if(str[0]=='-')
        swaps+=1;
        int n=str.size();
        int j=0;
        while(str[j]=='-')
        j++;

        for(int i=j;i<n;i++)
        {
            if(str[i]=='-')
            swaps+=2;
           // cout<<swaps<<" "<<i<<endl;
            while(str[i]=='-')
            i++;
        }

        cout<<swaps<<endl;

    }
}
