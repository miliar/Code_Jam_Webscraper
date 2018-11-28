#include<cstdio>
#include<iostream>
#include<math.h>
#include<fstream>
using namespace std;


int main()
{
    int a,b,test,num,count,sum,sum2,temp,div;
    // freopen("codejamc.in","r",stdin);
    //freopen("codejamc.txt","w",stdout);


    ofstream f("codejamc.txt");
    ofstream f2("codejamc.out");
    ifstream f1("codejamc.txt");
    scanf("%d",&test);
    f<<test<<endl;
   f1>>test;


    for(int j=1; j<=test; j++)
    {
        scanf("%d %d",&a,&b);
        f<<a<<" "<<b<<endl;
        f1>>a>>b;
        count=0;
        for(int i=a; i<=b; i++)
        {
            sum=0,sum2=0;
            for(num=i; num!=0; num=num/10)
            {
                div=num%10;
                sum=sum*10+div;
            }
            if(i==sum)
            {
                temp=floor(sqrt(i));
                if(pow(temp,2)==i)
                {
                    for(num=temp; num!=0; num=num/10)
                    {
                        div=num%10;
                        sum2=sum2*10+div;
                    }
                    if(temp==sum2)
                    {

                        count=count+1;
                    }
                }


            }

        }

       // printf("Case #%d: %d\n",j,count);
        f2<<"Case #"<<j<<": "<<count<<endl;

    }
    return 0;
}

