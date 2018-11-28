#include <bits/stdc++.h>

using namespace std;
typedef long long ll;


vector<ll> primos;

void criba(ll limite)
{
    ll tamano_criba;
    bitset<5000010> bs;
    tamano_criba = limite + 1;
    bs.set(); bs[0] = bs[1] = 0;
    for (ll i = 2; i <= tamano_criba; i++)
        if (bs[i])
        {
            for (ll j = i * i; j <= tamano_criba; j += i)
             bs[j] = 0;
            
            primos.push_back(i);
        }
            
       
}

int main()
{
    
    int n=16;
    int j=50;
    criba(10000);
    srand(time(NULL));
    int found=0;
    bool buffer[20];
    set<string> founded;
    printf("Case #1:\n");
    while(found<50)
    {
        buffer[0]=1;
        buffer[15]=1;
        
        for(int i=1;i<15;i++)
        {
            buffer[i] = rand()%2;
        }
        
        unsigned long long base[12];
        
        vector<long long> suertes= vector<ll>();
        for(int i=2;i<=10;i++)
        {
            base[i]=0;
            long long mult=1;
            for(int k=15;k>=0;k--)
            {
                base[i]+=mult*buffer[k];
                mult*=i;
            }
            
            long long OK=false;
            for(int k=0;k<primos.size();k++)
            {
                if(base[i]%primos[k]==0 && base[i]!=primos[k])
                {
                    OK = primos[k];
                    break;
                }
            }
            if(!OK)
                break;
            else
                suertes.push_back(OK);
        }
        
        if(suertes.size()==9)
        { char check[100];
            for(int i=0;i<16;i++)
            {
               
                check[i]=buffer[i]?'1':'0';
            }
            if(founded.find(check)==founded.end())
            {
                founded.insert(check);
            }
            else continue;
            for(int i=0;i<16;i++)
            {
                printf("%d",buffer[i]?1:0);
            }
            
            for(int i=0;i<9;i++)
                printf(" %lld",suertes[i]);
            printf("\n");
            found++;
        }
        else
        {
           // printf("gg\n");
        }
    }
    return 0;
    
}