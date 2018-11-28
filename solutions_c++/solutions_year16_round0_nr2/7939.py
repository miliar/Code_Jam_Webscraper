#include<bits/stdc++.h>
using namespace std;
string A,temp;
int allplus(string X)
{
    //cout<<"Checking motherfucker "<<X<<"\n";
    int n=X.length();
    int i;
    for(i=0;i<n;i++)
    {
       if(X[i]=='-')
        break;
    }
    if(i==n)
    {
        //cout<<"All positive\n";
        return 1;
    }
    else
    {
        //cout<<"All not positive\n";
        return 0;
    }
}
int main()
{
    ios_base::sync_with_stdio(0);
    int t,n,j,i,l;
    freopen("E:/B-large.in", "r", stdin);
	freopen("E:/output.txt", "w", stdout);
    cin>>t;
    long long int ctr;
    for(l=1;l<=t;l++)
    {
        cin>>A;
        n=A.length();
        ctr=0;
        while(allplus(A)==0)
        {
            temp.clear();
            //cout<<A<<"\n";
            //getchar();
            if(A[0]=='+')
            {
                j=0;
                while(A[j]=='+'&&j<n)
                {
                    j++;
                }
                //cout<<j<<"\n";
                for(i=0;i<j;i++)
                    A[i]='-';
            }
            else
            {
                j=n-1;
                while(A[j]=='+'&&j>=0)
                {
                    j--;
                }
                for(i=j;i>=0;i--)
                {
                    if(A[i]=='-')
                        temp+='+';
                    else
                        temp+='-';
                }
                for(i=j+1;i<n;i++)
                    temp+='+';
                A=temp;
            }
            ctr++;
        }
        cout<<"Case #"<<l<<": "<<ctr<<"\n";
    }
    return 0;
}
