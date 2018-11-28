# include<iostream>
using namespace std;

int main()
{
    long a[4][4],b[2][4],r[100],nos[100];
    long n,no,c=0,i,j,k;
    cin>>n;
    for(i=0;i<n;i++)
    {
    c=0;
    cin>>no;
    no--;
    for(j=0;j<4;j++)
    for(k=0;k<4;k++)
    cin>>a[j][k];
    for(j=0;j<4;j++)
    b[0][j]=a[no][j];
    cin>>no;
    no--;
    for(j=0;j<4;j++)
    for(k=0;k<4;k++)
    cin>>a[j][k];
    for(j=0;j<4;j++)
    b[1][j]=a[no][j];
    for(j=0;j<4;j++)
    for(k=0;k<4;k++)
    {
                    if((b[1][j]-b[0][k])==0)
                    {
                    c++;
                    nos[i]=b[1][j];
                    }
                    
    }
    r[i]=c;
    }
    for(i=0;i<n;i++)
    {
                    cout<<"CASE #"<<i+1<<": ";
                    if(r[i]==1)
                    cout<<nos[i];
                    else if(r[i]>1)
                    cout<<"Bad magician!";
                    else
                    cout<<"Volunteer cheated!";
                    cout<<endl;
    }
    return 0;
}
    
    
    
    
    
    