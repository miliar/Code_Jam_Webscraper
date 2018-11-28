#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int A[4][4];
    int B[4][4];
    int TT=1;
    while(t--)
    {
        int n,k;
        cin>>n;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++) cin>>A[i][j];
        }
        cin>>k;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++) cin>>B[i][j];
        }
        int nk=0;
        int p;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
              if(A[n-1][i]==B[k-1][j])
              {
                  p=A[n-1][i];
                  nk++;
              }
            }
        }
        if(nk==1) cout<<"Case #"<<TT<<": "<<p<<endl;
        else if(nk>1) cout<<"Case #"<<TT<<": Bad magician!"<<endl;
        else if(nk==0) cout<<"Case #"<<TT<<": Volunteer cheated!"<<endl;
        TT++;

    }
    return 0;
}
