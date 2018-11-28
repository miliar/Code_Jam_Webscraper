#include<iostream>


using namespace std;

int main()
{
    int T,N,P;
    int A[20000];
    cin>>T;
    for(int z=1;z<=T;z++)
    {
        cin>>N>>P;
        A[0]=0;A[1]=1;
        for(int i=1;i<N;i++)
        {
            for(int j=0;j<(1<<i);j++)
            {
                A[j]=2*A[j];
                A[j+(1<<i)]=A[j]+1;
            }
        }
        int min=A[P];
        for(int i=P;i<(1<<N);i++)
            if(min>A[i])
                min=A[i];

        int max=A[0],ans=A[0];
        for(int i=0;i<P;i++)
        {
            if(max<A[i])
                max=A[i];
            if(A[i]<min&&ans<A[i])
                ans=A[i];
        }
        if(P==(1<<N))
        cout<<"Case #"<<z<<": "<<(1<<N)-1<<" "<<max<<endl;
        else
        cout<<"Case #"<<z<<": "<<ans<<" "<<max<<endl;
    }
    return 0;
}
