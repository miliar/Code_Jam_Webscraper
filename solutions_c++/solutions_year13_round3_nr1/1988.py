#include<iostream>
#include<string.h>
using namespace  std;
int main()
{
    int t;
    int cas=1;
    int alpha[26]={0};
    alpha[0]=alpha[4]=alpha[8]=alpha[14]=alpha[20]=1;
    cin>>t;
    while(t--)
    {
        char A[101];
        int n;
        cin>>A;
        cin>>n;
        int count=0;
        for(int i=0;i<strlen(A)-n+1;i++)
        {
            for(int j=i+n-1;j<strlen(A);j++)
            {
                int cnt=0;
                for(int k=i;k<=j;k++)
                {
                    if(alpha[A[k]-97]==0)
                    {
                        cnt++;
                    }
                    else
                    {
                        cnt=0;
                    }
                    if(cnt>=n)
                    {
                        count++;
                        break;
                    }
                }
            }
        }
        cout<<"Case #"<<cas<<": "<<count<<endl;
        cas++;
    }
    return 0;
}
