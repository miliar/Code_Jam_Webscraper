#include<iostream>
using namespace std;
int main()
{
    int test,matrix1[4][4],matrix2[4][4],t1,t2,i,j;
    cin>>test;
    int z=0;
    int temp[test];
    char arr[test][10];
    int ck[test];
    int k=0;
    while(z<test)
    {
        int count=0;
        cin>>t1;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
               {
                  cin>>matrix1[i][j];
               }
        }

         cin>>t2;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                {
                    cin>>matrix2[i][j];
                }
        }
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {if(matrix1[t1-1][i]==matrix2[t2-1][j])
            {
             count++;
              temp[z]=  matrix1[t1-1][i];
            }}

        }


     /*   if(count==0)
            char array[k]="Case #3: Volunteer cheated!";
        else if(count==1)
            char array[k]=temp;
            else
              char array[k]="Case #2: Bad magician!" */
              ck[k++]=count;
              z++;

    }
    for(i=0;i<test;i++)
    {
        if(ck[i]==0)
            cout<<"Case #"<<i+1<<": Volunteer cheated!\n";
        else if(ck[i]==1)
            cout<<"Case #"<<i+1<<": "<<temp[i]<<"\n";
            else
                cout<<"Case #"<<i+1<<": Bad magician!\n";
    }
}
