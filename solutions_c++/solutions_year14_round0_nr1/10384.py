#include<iostream>
using namespace std;
int main()
{
	int t,a[4][4],b[4][4],x,y,i,j,z=1,flag=0,ele;
	cin>>t;
	point:
	while(z<=t)
	{
            flag=0;
            cin>>x;
            for(i=0;i<4;i++)
                    for(j=0;j<4;j++)
                                    cin>>a[i][j];
            cin>>y;
            for(i=0;i<4;i++)
                    for(j=0;j<4;j++)
                                    cin>>b[i][j];
            for(j=0;j<4;j++)
            {
                    for(i=0;i<4;i++)
                    {
                                    if(a[x-1][j]==b[y-1][i])
                                    {
                                            flag++;
                                            ele=a[x-1][j];
                                    }
                    }
            }
            if(flag==0)
                       cout<<"Case #"<<z<<": Volunteer cheated!"<<endl;
            else 
                 if(flag==1)
                            cout<<"Case #"<<z<<": "<<ele<<endl;
                 else
                            cout<<"Case #"<<z<<": Bad magician!"<<endl;     
            z++;
      }
      return 0;
}                                                                                 
