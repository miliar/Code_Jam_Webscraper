#include<stdio.h>
#include<math.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#define pi 2*acos(0)
#define inf INT_MAX
#define eps 0.00000001
using namespace std;

main()
{
    long long int i,res,from,to,t;
    FILE *read,*write;
    read=fopen("fairlargein.txt","r");
    write=fopen("fairlargeout.txt","w");
    fscanf(read," %lld",&t);
    for(i=1;i<=t;i++)
    {
        fscanf(read," %lld %lld",&from,&to);
        res=0;
        if(from<=1&&to>=1)
        res++;
        if(from<=4&&to>=4)
        res++;
        if(from<=9&&to>=9)
        res++;
        if(from<=121&&to>=121)
        res++;
        if(from<=484&&to>=484)
        res++;
        if(from<=10201&&to>=10201)
        res++;
        if(from<=12321&&to>=12321)
        res++;
        if(from<=14641&&to>=14641)
        res++;
        if(from<=40804&&to>=40804)
        res++;
        if(from<=44944&&to>=44944)
        res++;
        if(from<=1002001&&to>=1002001)
        res++;
        if(from<=1234321&&to>=1234321)
        res++;
        if(from<=4008004&&to>=4008004)
        res++;
        if(from<=100020001&&to>=100020001)
        res++;
        if(from<=102030201&&to>=102030201)
        res++;
        if(from<=104060401&&to>=104060401)
        res++;
        if(from<=121242121&&to>=121242121)
        res++;
        if(from<=123454321&&to>=123454321)
        res++;
        if(from<=125686521&&to>=125686521)
        res++;
        if(from<=400080004&&to>=400080004)
        res++;
        if(from<=404090404&&to>=404090404)
        res++;
        if(from<=10000200001&&to>=10000200001)
        res++;
        if(from<=10221412201&&to>=10221412201)
        res++;
        if(from<=12102420121&&to>=12102420121)
        res++;
        if(from<=12345654321&&to>=12345654321)
        res++;
        if(from<=40000800004&&to>=40000800004)
        res++;
        if(from<=1000002000001&&to>=1000002000001)
        res++;
        if(from<=1002003002001&&to>=1002003002001)
        res++;
        if(from<=1004006004001&&to>=1004006004001)
        res++;
        if(from<=1020304030201&&to>=1020304030201)
        res++;
        if(from<=1022325232201&&to>=1022325232201)
        res++;
        if(from<=1024348434201&&to>=1024348434201)
        res++;
        if(from<=1210024200121&&to>=1210024200121)
        res++;
        if(from<=1212225222121&&to>=1212225222121)
        res++;
        if(from<=1214428244121&&to>=1214428244121)
        res++;
        if(from<=1232346432321&&to>=1232346432321)
        res++;
        if(from<=1234567654321&&to>=1234567654321)
        res++;
        if(from<=4000008000004&&to>=4000008000004)
        res++;
        if(from<=4004009004004&&to>=4004009004004)
        res++;
        fprintf(write,"Case #%lld: %lld\n",i,res);
    }
    fclose(read);
    fclose(write);
    return 0;
}

