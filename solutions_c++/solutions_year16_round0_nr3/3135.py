#include<iostream>
#include<cmath>
#include<cstdio>

using namespace std;

long long int divisor(long long int num)
{
long long int square_root = (int) sqrt(num) + 1;
for (long long int i = 2; i < square_root; i++)
{
if(num%i==0)
return(i);
}
}

long long int prime(long long int num)
{long long int i;
long long int square_root = (int) sqrt(num) + 1;
for (i = 2; i < square_root; i++)
{
if(num%i==0)
break;
}
if(i==square_root)
return 0;
else
return 1;

}


long long int bina(long long int dec) {
	long rem,i=1,sum=0;
    
    do
    {
        rem=dec%2;
        sum=sum + (i*rem);
        dec=dec/2;
        i=i*10;
    }while(dec>0);

return(sum);

}

long long int base2(long long int num)

{

    long long int bin, dec = 0, rem, base = 1;

    bin = num;

    while (num > 0)

    {

        rem = num % 10;

        dec = dec + rem * base;

        base = base * 2;

        num = num / 10;

    }

   return(dec);


}

long long int base3(long long num)

{

    long long bin, dec = 0, rem, base = 1;

    bin = num;

    while (num > 0)

    {

        rem = num % 10;

        dec = dec + rem * base;

        base = base * 3;

        num = num / 10;

    }

   return(dec);


}

long long int base4(long long int num)

{

    long long int bin, dec = 0, rem, base = 1;

    bin = num;

    while (num > 0)

    {

        rem = num % 10;

        dec = dec + rem * base;

        base = base * 4;

        num = num / 10;

    }

   return(dec);


}

long long int base5(long long int num)

{

    long long int  bin, dec = 0, rem, base = 1;

    bin = num;

    while (num > 0)

    {

        rem = num % 10;

        dec = dec + rem * base;

        base = base * 5;

        num = num / 10;

    }

   return(dec);


}

long long int base6(long long int num)

{

    long long int  bin, dec = 0, rem, base = 1;

    bin = num;

    while (num > 0)

    {

        rem = num % 10;

        dec = dec + rem * base;

        base = base * 6;

        num = num / 10;

    }

   return(dec);


}

long long int base7(long int num)

{

    long long int bin, dec = 0, rem, base = 1;

    bin = num;

    while (num > 0)

    {

        rem = num % 10;

        dec = dec + rem * base;

        base = base * 7;

        num = num / 10;

    }

   return(dec);


}

long long int base8(long long int num)

{

    long long int  bin, dec = 0, rem, base = 1;

    bin = num;

    while (num > 0)

    {

        rem = num % 10;

        dec = dec + rem * base;

        base = base * 8;

        num = num / 10;

    }

   return(dec);


}

long long int base9(long long int num)

{

    long long int  bin, dec = 0, rem, base = 1;

    bin = num;

    while (num > 0)

    {

        rem = num % 10;

        dec = dec + rem * base;

        base = base * 9;

        num = num / 10;

    }

   return(dec);


}

long long int base10(long long int num)

{

    long long int bin, dec = 0, rem, base = 1;

    bin = num;

    while (num > 0)

    {

        rem = num % 10;

        dec = dec + rem * base;

        base = base * 10;

        num = num / 10;

    }

   return(dec);


}


int main()
{
long long  int n,J,a[100],m,p,i,j,x,y,z,k,s,r,u,T,f,count;

freopen("tempo.in", "r", stdin);

freopen("tempo.out", "w", stdout);

cin>>T;
for(f=1;f<=T;f++)
{cin>>n>>J;
cout<<"Case #"<<f<<":"<<endl;
m=0,p=0,s=0,u=0,count=0;

a[0]=1,a[n-1]=1;
for(i=1;i<n-1;i++)
a[i]=0;

for(i=1;i<n-1;i++)
m=m*10+a[i];

for(j=1;j<n-1;j++)
a[j]=1;

for(j=1;j<n-1;j++)
p=p*10+a[j];

for(x=base2(m);x<=base2(p);x++)
{
k=bina(x);
//cout<<k;
s=1*pow(10,n-1)+k*10+1;
//cout<<x<<s<<endl;
if((prime(base2(s))) && (prime(base3(s))) && (prime(base4(s))) && (prime(base5(s))) && (prime(base6(s))) && (prime(base7(s))) && (prime(base8(s))) && (prime(base9(s))) && (prime(base10(s))))
{
cout<<s<<" "<<divisor(base2(s))<<" "<<divisor(base3(s))<<" "<<divisor(base4(s))<<" "<<divisor(base5(s))<<" "<<divisor(base6(s))<<" "<<divisor(base7(s))<<" "<<divisor(base8(s))<<" "<<divisor(base9(s))<<" "<<divisor(base10(s));
cout<<endl; 
count++;
}
if(count==J)
break;
}

}
return 0;
}
