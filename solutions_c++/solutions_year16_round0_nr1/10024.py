#include<iostream>
#include<cmath>


using namespace std;


int main ()
{   int T;cin>>T;long c[T];
    for(int q=0;q<T;q++)
    {
    long N,U,m,cnt,j;
    cin >>N;
    int b[10];
    for( m=0;m<10;m++)
    {
        b[m]=77;
        
    }
    if(N==0)
    {c[q]=0;}
    else
    {
for(int l=1;l<(l+1);l++)
{
    U=N*l;
    int x=0;
    for(int i=0;i<=10;i++)
    {
        if((int)(U/(pow(10,i)))!=0)
            x++;
    }
    
    int a[x];long M=U;
    for( j=0,cnt=x;j<x;j++)
    {
        a[j]=(int)(M/pow(10,cnt-1));
        M=fmod(M,pow(10,cnt-1));
        cnt--;
    }
    
    for( j=0;j<x;j++)
    {
        b[a[j]]=a[j];
    }
    
    int flag=0;
    for(int h=0;h<10;h++)
    {
        if(b[h]==h)
            flag++;
    
        }

    
    if(flag==10)
    {c[q]=U;break;}
}
}
    }
     for(int q=0;q<T;q++)
     {      if(c[q]!=0)
                cout<<"Case #"<<q+1<<":"<<" "<<c[q]<<endl;
            if(c[q]==0)
                cout<<"Case #"<<q+1<<":"<<" "<<"insomnia"<<endl;

}
}






