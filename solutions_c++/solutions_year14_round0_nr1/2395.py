
#include<stdio.h>
#include<string>
#include<conio.h>
#include<iomanip>
#include <iostream>
#include <iomanip>
using namespace std;
int main(int argc, char* argv[])
{
			int cases,row1,row2,a1=0,a2=0,a3=0,ans=0;
            int mat1[4][4],mat2[4][4];
            int select1[4],select2[4];
			int mycount=0;
			cin>>cases;
			for(int i=1;i<=cases;i++)
			{
				a1=0,a2=0,a3=0,ans=0;
				mycount=0;
				cin>>row1;
                for (int i = 0; i < 4; i++)
                {
                    for(int j=0;j<4;j++)
                    {
                        cin>>mat1[i][j];
                    }
                }
                cin>>row2;
                for (int i = 0; i < 4; i++)
                {
                    for(int j=0;j<4;j++)
                    {
                        cin>>mat2[i][j];
                    }
                }
				for (int j = 0; j < 4; j++)
                {
                        select1[j]=mat1[row1-1][j];
                }
                for (int j = 0; j < 4; j++)
                {
                    select2[j] = mat2[row2-1][j];
                }
                for (int j = 0; j < 4; j++)
                {
                    for (int k = 0; k < 4; k++)
                    {
						if (select1[j] == select2[k])
						{
							mycount++;
						}
					}

                }
                for (int j = 0; j < 4; j++)
                {
                    for (int k = 0; k < 4; k++)
                    {

                        if (select1[j] == select2[k])
                        {
                        
                            a2 = 1;
                            ans = select1[j];
							
                        }
                        else
                        {
                        
                            a3 = 1;
                        }
                    }
                }
				if(mycount>1)
					printf("Case #%d: Bad magician!\n",i); 
				else if(a2==1)
					printf("Case #%d: %d\n",i,ans); 
                else
					printf("Case #%d: Volunteer cheated!\n",i); 

			}
			   //getch();
	return 0;
}