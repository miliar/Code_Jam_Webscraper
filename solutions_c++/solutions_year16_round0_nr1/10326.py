#include<iostream.h>
#include<stdio.h>
#include<conio.h>


void main()
{
FILE fo, fi;
fi=*freopen("asd.txt","r",stdin);
fo=*freopen("asdf.txt","w+",stdout);

 int t,n,tt,i;

cin>>tt;

//while(t--)
for(int t=1;t<=tt;t++)
{int temp,b,c=0;
    int a[10]={0,0,0,0,0,0,0,0,0,0};
cin>>n;
if(n==0)
{cout<<"Case #"<<t<<": INSOMNIA\n";}
else {
for(i=1;c<1;i++)
{
    temp=n*i;
    while(temp>0)
    {
        b=temp%10;
        a[b]++;
        temp=temp/10;
    
    }
 
 for(int j=0;j<10;j++)
    {//cout<<a[j]<<" : "<<j<<"\n";
        if(a[j]==0)
        {c=0;
            j=10;
        }else c=1;
    }
    //cout<<"asdasdasdasdasdddddddddddd\n";
 }
 i--;
 long long o=n*i;
 
   cout<<"Case #"<<t<<": "<<n*i<<endl;

    
}
    
}

fclose(stdout);
fclose(stdin);


}