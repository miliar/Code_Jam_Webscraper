# include<iostream>
# include<cstdio>
# include<fstream>
# include<sstream>
using namespace std;
int main()
{
    int t,m,n,i,j,d,css=0,k;
    freopen("B-large.in","r",stdin);
    cin>>t;
    cin.ignore();
    ofstream m1;
    m1.open("op1.txt");
    while(t--)
    {
              cin>>m>>n;
              int arr[m][n];
              d=1;
              for(i=0;i<m;++i)
              for(j=0;j<n;++j)
              cin>>arr[i][j];
              for(i=0;i<m;++i)
              {
                    for(j=0;j<n;++j)
                    {
                                    for(k=0;k<n;++k)
                                    {
                                                    if(arr[i][j]<arr[i][k])
                                                    {
                                                                           d=0;
                                                                           //cout<<i<<" "<<j<<endl;
                                                                           break;
                                                    }
                                    }
                                    if(!d)
                                    {
                                     d=1;
                                     for(k=0;k<m;++k)
                                     {
                                                    if(arr[i][j]<arr[k][j])
                                                    {
                                                                           d=0;
                                                                           //cout<<i<<" "<<j<<endl;
                                                                           break;
                                                    }
                                     }
                                    }
                                    if(!d)
                                    break;
                    }
                                    if(!d)
                                    break;
                    
              }
              m1<<"Case #"<<++css<<": ";
              if(d)
              m1<<"YES";
              else
              m1<<"NO";
              m1<<endl;
              cin.ignore();
    }
    m1.close();
    return 0;
}
              
