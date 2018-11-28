#include<bits/stdc++.h>
using namespace std;

int solve(char* arr)
{
    int len = strlen(arr);
    int res=0;
    for(int i = 1; i<len; i++)
    {
        if(arr[i]!=arr[i-1])
            res++;
    }

    if(arr[len-1]=='-')
        res++;

    return res;
}

int main()
{
    int t,test;
    char arr[110];

    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);

    cin>>test;

    for(t=1;t<=test;t++)
    {
        cin>>arr;

        cout<<"Case #"<<t<<": ";

        cout<<solve(arr)<<endl;
    }

    fclose(stdin);
    fclose(stdout);

    return 0;
}
