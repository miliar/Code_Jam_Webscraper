#include<bits/stdc++.h>
using namespace std;
int main()
{
    int T;
    long long N,loop;
    cin>>T;
    for(loop=1;loop<=T;loop++)
    {
        
        cin>>N;
        if(N==0)
        {
          cout<<"Case #1: INSOMNIA"<<endl;
          continue;
        }
        long long i,d,c,j,no,store;
        int A[10];
        for(i=0;i<10;i++)
        A[i]=0;
        for(i=1;i<=1000;i++)
        {
            store=N*i;
            no=N*i;
            while(no!=0)
            {
                d=no%10;
                A[d]++;
                no/=10;
            }
            c=0;
           for(j=0;j<10;j++)
            {
             if(A[j]>0)
             c++;
             }
            if(c==10)
            break;
        }
        cout<<"Case #"<<loop<<": "<<store<<" "<<endl;
        
    }
    
    return 0;
}