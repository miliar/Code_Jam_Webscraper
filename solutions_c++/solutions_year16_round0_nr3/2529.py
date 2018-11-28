
#include <cstdio>
#include <stdio.h>
#include <iostream>
#include <cstdlib>
#include <string.h>
#include <cstring>
#include <cmath>
#include <math.h>

using namespace std;

int jamcoins=0, N, jc;
unsigned long long divisor=0;
unsigned long long sum, d[9], temp;
//unsigned long long temp;

short int is_prime()
{
    unsigned long long i;
    unsigned long long root=sqrt(sum);
    root+=1;
    for(i=2;i<=root;i++)
    {
        if(sum%i==0)
        {
            divisor=i;
            return 0;
        }
    }
    return 1;
}

short int is_jamcoin(int array[])
{
    
    int i;
 
    for(i=0;i<9;i++)
        d[i]=0;
    
    sum=1;
    for(i=0;i<N-1;i++)
        sum*=2;
    sum+=1;
    for(i=0;i<N-2;i++)
    {
        if(array[i]==1)
        {
            temp=1;
            for(int j=0;j<=i;j++)//2^i+1 as i is indexed one lower than what it stands for.
                temp*=2;
            sum+=temp;
            
        }
    }
    
    if((is_prime())==1)
        return 0;
    else
    {
        d[0]=divisor;
        divisor=0;
    }
    
    sum=1;
    for(i=0;i<N-1;i++)
        sum*=3;
    sum+=1;
    for(i=0;i<N-2;i++)
    {
        if(array[i]==1)
        {
            temp=1;
            for(int j=0;j<=i;j++)
                temp*=3;
            sum+=temp;
        }
    }
    
    if((is_prime())==1)
        return 0;
    else
    {
        d[1]=divisor;
        divisor=0;
    }
    
    sum=1;
    for(i=0;i<N-1;i++)
        sum*=4;
    sum+=1;
    for(i=0;i<N-2;i++)
    {
        if(array[i]==1)
        {
            temp=1;
            for(int j=0;j<=i;j++)
                temp*=4;
            sum+=temp;
        }
    }
    
    if((is_prime())==1)
        return 0;
    else
    {
        d[2]=divisor;
        divisor=0;
    }
    
    sum=1;
    for(i=0;i<N-1;i++)
        sum*=5;
    sum+=1;
    for(i=0;i<N-2;i++)
    {
        if(array[i]==1)
        {
            temp=1;
            for(int j=0;j<=i;j++)
                temp*=5;
            sum+=temp;
        }
    }
    
    if((is_prime())==1)
        return 0;
    else
    {
        d[3]=divisor;
        divisor=0;
    }
    
    sum=1;
    for(i=0;i<N-1;i++)
        sum*=6;
    sum+=1;
    for(i=0;i<N-2;i++)
    {
        if(array[i]==1)
        {
            temp=1;
            for(int j=0;j<=i;j++)
                temp*=6;
            sum+=temp;
        }
    }
    
    if((is_prime())==1)
        return 0;
    else
    {
        d[4]=divisor;
        divisor=0;
    }
    
    sum=1;
    for(i=0;i<N-1;i++)
        sum*=7;
    sum+=1;
    for(i=0;i<N-2;i++)
    {
        if(array[i]==1)
        {
            temp=1;
            for(int j=0;j<=i;j++)
                temp*=7;
            sum+=temp;
        }
    }
    
    if((is_prime())==1)
        return 0;
    else
    {
        d[5]=divisor;
        divisor=0;
    }
    
    sum=1;
    for(i=0;i<N-1;i++)
        sum*=8;
    sum+=1;
    for(i=0;i<N-2;i++)
    {
        if(array[i]==1)
        {
            temp=1;
            for(int j=0;j<=i;j++)
                temp*=8;
            sum+=temp;
        }
    }
    if((is_prime())==1)
        return 0;
    else
    {
        d[6]=divisor;
        divisor=0;
    }
    
    sum=1;
    for(i=0;i<N-1;i++)
        sum*=9;
    sum+=1;
    for(i=0;i<N-2;i++)
    {
        if(array[i]==1)
        {
            temp=1;
            for(int j=0;j<=i;j++)
                temp*=9;
            sum+=temp;
        }
    }
    if((is_prime())==1)
        return 0;
    else
    {
        d[7]=divisor;
        divisor=0;
    }
    
    sum=1;
    for(i=0;i<N-1;i++)
        sum*=10;
    sum+=1;
    for(i=0;i<N-2;i++)
        {
        if(array[i]==1)
        {
            temp=1;
            for(int j=0;j<=i;j++)
                temp*=10;
            sum+=temp;
        }
    }
    
    if((is_prime())==1)
        return 0;
    else
    {
        d[8]=divisor;
        divisor=0;
    }
    
    
    for(i=0;i<9;i++)
        if(d[i]==0)
            return 0;
     
 
    cout<<"1";
    for(int i=N-3;i>=0;i--)
        cout<<array[i];
    cout<<"1"<<" "<<d[0]<<" "<<d[1]<<" "<<d[2]<<" "<<d[3]<<" "<<d[4]<<" "<<d[5]<<" "<<d[6]<<" "<<d[7]<<" "<<d[8]<<endl;
    
    return 1;    
}

void generate_perm(int no_of_bits, const int bit, int array[])
{
    if(no_of_bits==(N-3))
    {
        array[no_of_bits]=bit;
        if(jamcoins!=jc)
        {
            
            if(is_jamcoin(array)==1)
                jamcoins++;
        }
        return;
    }
    
    array[no_of_bits]=bit;
    generate_perm(no_of_bits+1,0,array);
    generate_perm(no_of_bits+1,1,array);
}

int main()
{
    int t, u, i, array[14];
    freopen("C.in", "rt", stdin);
    freopen("C.out", "wt", stdout);
    cin>>t;
    cin>>N>>jc;
    u=1;
    while(u<=t)
    {   cout<<"Case #"<<u<<":"<<endl;
        u++;
        jamcoins=0;
        generate_perm(0,0,array);
        for(i=0;i<N-2;i++)
            array[i]=-1;
        if(jamcoins<jc)
        generate_perm(0,1,array);
    }
    return 0;
}

/**/

