//-_- Dpn -_-\\

#define TO_INT(a) a-'0'

#include<bits/stdc++.h>

using namespace std;

int main(void)
{
    int T,Smax,T2,c,i,j,sum;
    string S;
    cin>>T;
    T2 = T;
    while(T--)
    {
        c = 0;
        cin>>Smax>>S;
        for(i = 0; i<=Smax; i++)
        {
            sum = 0;
            for(j = 0; j < i; j++)
            {
                sum += TO_INT(S[j]);
            }
            if(sum+c < i)
                c++;
        }
        cout<<"Case #"<<T2-T<<": "<<c<<endl;
    }


 /*   while(T--)
    {
        c = 0;
        cin>>Smax>>S;
        int mem[Smax+1];
        mem[0] = TO_INT(S[0]);
        for(i = 1; i <= Smax; i++)
            mem[i] = mem[i-1] + TO_INT(S[i]);
        for(i = 0; i <= Smax; i++)
        {
            if(mem[i]+c < i)
            {
                c ++;
            }
        }
        for(i = 0; i <= Smax; i++) cout<<mem[i];
        cout<<"Ans: "<<c<<endl;
    }
*/
    return 0;
}





