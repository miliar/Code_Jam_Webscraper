#include <iostream>
using namespace std;

int main()
{
    int t,i,j,k,l;
    cin>>t;
    int N[t],M[t],h[t][100][100],o[t],a[100][100],max1,max2,flag1=0,flag2=0,min,n,m;
    for(i=0;i<t;i++)
    {
        cin>>N[i]>>M[i];
        for(j=0;j<N[i];j++)
        {
            for(k=0;k<M[i];k++)
            {
                cin>>h[i][j][k];
            }
        }
    }
    
    for(i=0;i<t;i++)
    {

        n=N[i];
        m=M[i];
        min=101;
            for(j=0;j<n;j++)
                for(k=0;k<m;k++)
                    if(h[i][j][k]<min)
                        min=h[i][j][k];
        max2=101;
        max1=101;
        while(max1>min && o[i]!=-1)
        {
            
            max1=0;
            for(j=0;j<n;j++)
                for(k=0;k<m;k++)
                    if(h[i][j][k]>max1 && h[i][j][k]<max2)
                        max1=h[i][j][k];
            
            for(j=0;j<n;j++)
                {
                    for(k=0;k<m;k++)
                    {
                        flag1=0;
                        flag2=0;
                        if(h[i][j][k]==max1)
                    {
                        for(l=0;l<n;l++)
                        {
                            if(h[i][l][k]>max1)
                                {
                                flag1=1;}
                        }
                        for(l=0;l<m;l++)
                        {
                            if(h[i][j][l]>max1)
                                {
                                flag2=1;}
                        }
                        if(flag1==1 && flag2==1)
                        {
                            o[i]=-1;
                            break;
                        }
                        else
                        {
                            a[j][k]=h[i][j][k];
                        }
                    }
                    }
                    if(o[i]==-1)
                        break;
                }

            max2=max1;
        }

        if(o[i]!=-1)
        {
            o[i]=1;
        }
     }
   for(i=0;i<t;i++)
  {
    cout<<"Case #"<<i+1<<": "; 
    switch(o[i])
    {
      case -1:
      	cout<<"NO";
      	break;
      case 1:
      	cout<<"YES";
      	break;
    }
   cout<<endl;
 }
}
