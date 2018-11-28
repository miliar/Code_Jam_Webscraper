#include<stdio.h>
#include<iostream>
using namespace std;

main()
{
    int t,n,m,**lawn,**check,i,j,k,l,z,prevz,flag=0,hash[101];
    char *result;
    cin>>t;

    for(k=0;k<t;k++)
    {
        z=1;
        for(i=0;i<=100;i++)
            hash[i]=0;

        cin>>n>>m;
        lawn = new int*[n];
        check = new int*[n];
        for(i = 0; i < n; ++i)
        {
            lawn[i] = new int[m];
            check[i] = new int[m];
        }

        result = "YES";

        for(i = 0; i < n; i++)
            for(j = 0; j < m; j++)
            {
                 cin>>lawn[i][j];
                 hash[lawn[i][j]]=1;
            }


        while(z<=100)
        {

        if(hash[z]==1)
        {

        if(z>1)
        {
            for(i = 0; i < n; i++)
            for(j = 0; j < m; j++)
            {
                 if(lawn[i][j]==prevz)
                    lawn[i][j]=z;
            }
        }

        for(i = 0; i < n; i++)
            for(j = 0; j < m; j++)
            {
                 check[i][j]=0;
            }

        for(i = 0; i < n; i++)
        {
            for(j = 0; j < m; j++)
            {
                if(lawn[i][j]==z && check[i][j]==0)
                {
                    flag = 1;
                    for(l=0; l<m; l++)
                    {
                        if(lawn[i][l]!=z)
                        {
                            flag = 0;
                            break;
                        }
                    }

                    if(flag==0){

                    flag = 2;
                    for(l=0; l<n; l++)
                    {
                        if(lawn[l][j]!=z)
                        {
                            flag = 0;
                            break;
                        }
                    }
                    }

                    if(flag==0)
                    {
                        result="NO";
                        break;
                    }

                    if(flag==1)
                    {
                        for(l=0; l<m; l++)
                        {
                            check[i][l]=1;
                        }
                    }

                    else if(flag==2)
                    {
                        for(l=0; l<n; l++)
                        {
                            check[l][j]=1;
                        }
                    }

                }
            }
            if(result=="NO")
                break;
        }

        prevz=z;
        }

        if(result=="NO")
                break;

        z++;

        }
        cout<<"\nCase #"<<k+1<<": "<<result;

        for(int i = 0; i < n; ++i) {
            delete [] lawn[i];
            delete [] check[i];
        }
        delete [] lawn;
        delete [] check;

    }
}
