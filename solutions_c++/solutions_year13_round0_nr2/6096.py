#include<iostream>
#include<cstdio>
using namespace std;
 
int main()
{
    int test,m,max_num,n,flag;
    int lawn[110][110],temp[110][110];
    cin>>test;
//int x = t;
    int total =  1;
    for(int t = 1;t<=test;t++)
    {
              
              cin>>n>>m;

//cout<<"Case #"<<x-t<<": ";
              for(int i = 0;i < n;i++)
              for(int j = 0;j < m;j++)
              	
              scanf("%d",&lawn[i][j]);
              
              for(int i=0;i<n;i++)
              for(int j=0;j<m;j++)
              	temp[i][j]=-1;
              
              flag = 1;
              
              for(int i=0;i<n;i++)
              {
                              max_num=0;
                              
                              for(int j=0;j<m;j++)

                              max_num = max(lawn[i][j],max_num);
                              
                              
                              for(int j=0;j<m;j++)
                              {
                                       if(temp[i][j]==-1)
                                       {
                                                 if(max_num!=lawn[i][j])
                                                 {
                                                              for(int k=0;k<n;k++)
                                                              {
                                                                              if(temp[k][j]==-1)
                                                                              {
                                                                                              temp[k][j]=lawn[i][j];
                                                                              }
                                                                              else if(temp[k][j]!=lawn[i][j])
                                                                              flag=0;
                                                              }
                                                 }
                                                 
                                                 else
                                                 temp[i][j]=lawn[i][j];   
                                       }
                                       else
                                       if(temp[i][j]!=lawn[i][j])
                                       flag=0;                             
                              }
            /*  for(int x=0;x<n;x++)
              {
			for(int y=0;y<m;y++)
             			cout<<temp[x][y]<<" ";
		cout<<endl;
			
              }*/

}
              //cout<<"Case #"<<total<<": ";
	printf("Case #%d: ",t);
	if(flag==true)
		{
		printf("YES\n");	
		}
	else
		{
		printf("NO\n");	
		}
            
    }
          return 0;
}
