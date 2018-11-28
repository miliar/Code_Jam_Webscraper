#include<iostream>
#include<cmath>


using namespace std;


int main ()
{   int T;cin>>T;long c[T];
    for(int w=0;w<T;w++)
    {
    long X,Y,m,cnt,j;
    cin >>X;
    int b[10];
    for( m=0;m<10;m++)
    {
        b[m]=77;
        
    }
    if(X==0)
    {c[w]=0;}
    else
    {
for(int l=1;l<(l+1);l++)
{
    Y=X*l;
    int x=0;
    for(int i=0;i<=10;i++)
    {
        if((int)(Y/(pow(10,i)))!=0)
            x++;
    }
    
    int a[x];long M=Y;
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
    {c[w]=Y;break;}
}
}
    }
     for(int w=0;w<T;w++)
     {      if(c[w]!=0)
                cout<<"Case #"<<w+1<<":"<<" "<<c[w]<<endl;
            if(c[w]==0)
                cout<<"Case #"<<w+1<<":"<<" "<<"insomnia"<<endl;

}
}






