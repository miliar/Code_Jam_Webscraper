#include<iostream>
#include<cstdio>
#include<string>
#include<algorithm>

using namespace std;

int main()
{
    freopen("input.in", "r", stdin);
    freopen ("output.txt","w",stdout);
    int Test,k=0;
    scanf("%d",&Test);
    while(Test--)
    {
        string S,R="",T="";
        int len;
        cin>>S;
        printf("Case #%d: ",++k);
        int i,j=0;
        len=S.length();
        R+=S[0];
        for(i=1;i<len;i++)
        {
            if(S[i]>=R[j])
            {
                R+=S[i];
                j++;
            }
            else
            {
                T+=S[i];
            }
        }
        reverse(R.begin(),R.end());
        cout<<R<<T<<endl;
    }
    fclose(stdout);
    return 0;
}
