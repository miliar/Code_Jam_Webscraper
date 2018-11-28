#include<bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
int A[11],B[11],Ans=0,C[11];
void Reccur(int X , int Y)
{
    if(X==-1)
    {
        int cnt=0,i=0;
        for (i=1 ; i<Y ; i++)
        {
            //cout<<B[i]<<" ";
            int a=i+1,b=i-1;
            a%=Y;
            b+=Y;
            b%=Y;
            //cout<<b<<" "<<i<<" "<<a<<endl;
            if(B[a]==A[B[i]-1] || B[b]==A[B[i]-1])
                cnt++;
            else
                break;
        }
        if(i==Y)
        {
            while(A[B[0]-1]!=B[Y-1] && A[B[0]-1]!=B[1] && i>0)
            {
                i--;
                cnt--;
            }
            if(i!=0)
                cnt++;
        }
        else
        {
            if((A[B[0]-1]==B[1] || A[B[0]-1]==B[i]) && B[0]==A[B[i]-1])
                cnt+=2;
            else
            {
                i--;
                while (((A[B[0]-1]!=B[1] && A[B[0]-1]!=B[i])||(A[B[i]-1]!=B[0] && A[B[i]-1]!=B[i-1]))&&i>0)
                {
                    i--;
                    cnt--;
                }
                if(i!=0)
                    cnt++;
            }
        }
        //cout<<endl;

        if(cnt>Ans)
        {
            /*cout<<cnt<<endl;
            for (int i=0 ; i<Y ; i++)
                cout<<B[i]<<" ";
            cout<<endl;*/
            Ans=cnt;
        }
        return;
    }
    else
    {
        for (int i=1 ; i<=Y ; i++)
        {
            if(C[i]==0)
            {
                C[i]=1;
                B[X]=i;
                Reccur(X-1,Y);
                C[i]=0;
            }
        }
        return;
    }
}
int main()
{
    std:ios::sync_with_stdio(false);
    ifstream infile;
    ofstream outfile;
    infile.open("input.txt");
    outfile.open("output.txt");
    int T;
    //cin>>T;
    infile>>T;
    for (int i=0 ; i<T ; i++)
    {
        Ans=0;
        memset(A,0,sizeof(A));
        memset(B,0,sizeof(B));
        memset(C,0,sizeof(C));
        int N;
        //cin>>N;
        infile>>N;
        for (int j=0 ; j<N ; j++)
        {
            //cin>>A[j];
            infile>>A[j];
        }
        Reccur(N-1,N);
        //cout<<"Case #:"<<i+1<<": "<<Ans<<endl;
        outfile<<"Case #"<<i+1<<": "<<Ans<<endl;
    }
}
