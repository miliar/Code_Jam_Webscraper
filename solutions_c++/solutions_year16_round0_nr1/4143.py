#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("INP.txt","r+",stdin);
    freopen("ANS.txt","w+",stdout);
    int t;cin>>t;
    for(int i=1;i<=t;i++){
        long long int n,j=1;
        cin>>n;
        int coun=0;
        map<long long int,int>M;
        int N[10];
        for(int i=0;i<10;i++)N[i]=0;
        long long int last_num;
        while(coun!=10){
            long long int num=n*j;
            last_num=num;
            j++;
            if(M[num])break;
            M[num]=1;
            while(num &&coun!=10){
                int res=num%10;
                num/=10;
                if(!N[res]){
                    N[res]=1;
                    coun++;
                }
            }

        }
        if(coun!=10)cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
        else cout<<"Case #"<<i<<": "<<last_num<<endl;
    }
    return 0;
}
