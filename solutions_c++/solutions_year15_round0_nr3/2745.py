#include<iostream>
using namespace std;
int main()
{
    int T;
    char * mat[5][5]={"0","1","i","j","k",
                      "1","1","i","j","k",
                      "i","i","-1","k","-j",
                      "j","j","-k","-1","i",
                      "k","k","j","-i","-1"};
    
    cin>>T;
    for(int i=1;i<=T;i++)
    {
            int L,x;
            cin>>L>>x;
          
            char *temp=new char[L+1];
            cin>>temp;
           // cout<<L<<" "<<x<<" "<<temp;
            char *ch=new char[L*x+1];
             cout<<"Case #"<<i<<": ";
            for(int k=0;k<x;k++)
            {
                    for(int j=0;j<L;j++)
                    {
                            ch[k*L+j]=temp[j];
                    }
            }
           // delete temp;
            int l=0;
            int r=L*x-1;
            if(r-l<2)
            {
                     cout<<"NO\n";
                     continue;
            }
            if(L*x==3)
            {
                   if(ch[0]=='i'&&ch[1]=='j'&&ch[2]=='k')
                        {
                                                              cout<<"YES\n";
                                                              continue;
                        }
                        else
                        {
                            cout<<"NO\n";
                            continue;
                        }   
            }
           while(ch[l]!='i'&&l<r)
           {
                            int row,col;
                            for(int j=0;j<5;j++)
                            {
                                    if(ch[l]==mat[j][0][0])
                                    row=j;
                            }
                            for(int j=0;j<5;j++)
                            {
                                    if(ch[l+1]==mat[0][j][0])
                                    col=j;
                            }
                            if(mat[row][col][0]=='-')
                            {
                                                     ch[l]='-';
                                                     ch[++l]=mat[row][col][1];
                            }
                            else
                            {
                                ch[l]='0';
                            ch[++l]=mat[row][col][0];
                            }
           }
             while(ch[r]!='k'&&r>0)
           {
                            int row,col;
                            for(int j=0;j<5;j++)
                            {
                                    if(ch[r-1]==mat[j][0][0])
                                    row=j;
                            }
                            for(int j=0;j<5;j++)
                            {
                                    if(ch[r]==mat[0][j][0])
                                    col=j;
                            }
                            if(mat[row][col][0]=='-')
                            {
                                                     ch[r]='-';
                                                     ch[--r]=mat[row][col][1];
                            }
                            else
                            {
                                ch[r]='0';
                            ch[--r]=mat[row][col][0];
                            }
           }
           int m = l+1;
            while(ch[m]!='j'&&m<r)
           {
                            int row,col;
                            for(int j=0;j<5;j++)
                            {
                                    if(ch[m]==mat[j][0][0])
                                    row=j;
                            }
                            for(int j=0;j<5;j++)
                            {
                                    if(ch[m+1]==mat[0][j][0])
                                    col=j;
                            }
                            if(mat[row][col][0]=='-')
                            {
                                                     ch[m]='-';
                                                     ch[++m]=mat[row][col][1];
                            }
                            else
                            {
                                ch[m]='0';
                            ch[++m]=mat[row][col][0];
                            }
           }
           int mn=m+1;
               while(mn<r-1)
           {
                            int row,col;
                            for(int j=0;j<5;j++)
                            {
                                    if(ch[mn]==mat[j][0][0])
                                    row=j;
                            }
                            for(int j=0;j<5;j++)
                            {
                                    if(ch[mn+1]==mat[0][j][0])
                                    col=j;
                            }
                            if(mat[row][col][0]=='-')
                            {
                                                     ch[mn]='-';
                                                     ch[++mn]=mat[row][col][1];
                            }
                            else
                            {
                                ch[mn]='0';
                            ch[++mn]=mat[row][col][0];
                            }
           }
          // cout<<" "<<l<<m<<mn<<r<<" ";
           //cout<<ch<<"\n";
           if(ch[mn]=='1')
           {
                        if(ch[l]=='i'&&ch[m]=='j'&&ch[r]=='k')
                        {
                            int minus=0;
                        for(int j=0;j<L*x;j++)
                        {
                                if(ch[j]=='-')
                                {
                                              ++minus;
                                }
                        }
                        if(((float)minus)/2-minus/2==0)
                        {
                                cout<<"YES\n";
                                continue;               
                        }
                        else
                        {
                            cout<<"NO\n";
                        }                                  
                        }
                       
           }
           else
           {
               cout<<"NO\n";
           }
            
    }
}

