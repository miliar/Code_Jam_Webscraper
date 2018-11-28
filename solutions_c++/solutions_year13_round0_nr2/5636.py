#include<iostream>
#include<vector>
#include<algorithm>
#include<string>

using namespace std;

int main()
{
    int t=0,c;
    
    char *ans;
    
    cin>>c;

    while(++t<=c)
    {
        int n,m;
        int **matrix,**done;
        int check=0;
        
        cin>>n>>m;
        
        matrix = new int*[n];
        done = new int*[n];
        
        for(int i = 0; i < n; ++i)
        {
            matrix[i] = new int[m];
            done[i] = new int[m];
        }

        ans = "YES";

        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
            {
                 cin>>matrix[i][j];
                 done[i][j]=0;
            }

        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < m; j++)
            {
                if(matrix[i][j]==1 && done[i][j]==0)
                {
                    check = 0;
                    for(int l=0; l<m; l++)
                    {
                        if(matrix[i][l]!=1)
                        {
                            check = 1;
                            break;
                        }
                    }

                    if(check==1)
                    {
                    check = 2;
                    for(int l=0; l<n; l++)
                    {
                        if(matrix[l][j]!=1)
                        {
                            check = 1;
                            break;
                        }
                    }
                    }

                    if(check==1)
                    {
                        ans="NO";
                        break;
                    }

                    if(check==0)
                    {
                        for(int l=0; l<m; l++)
                        {
                            done[i][l]=1;
                        }
                    }

                    else if(check==2)
                    {
                        for(int l=0; l<n; l++)
                        {
                            done[l][j]=1;
                        }
                    }

                }
            }
            if(ans=="NO")
                break;
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;

    }
    return 0;
}
