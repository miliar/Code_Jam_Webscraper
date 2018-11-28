#include<iostream>
#include<iomanip>
#include<string.h>
using namespace std;
int main()
{
    short int T = 0,i = 0,j = 0,count = 0,answer=0,c = 1;
    short int choice1,choice2;
    short int mat[4][4]={0};
    bool numbers[17] = {false};
    cin>>T;
    while(T--)
    {
        count = 0;
        memset(numbers,false,17);
        cin>>choice1;
        for(i = 0;i<4;i++)
        {
            for(j = 0 ;j<4;j++)
            {
                cin>>mat[i][j];
            }
        }
        choice1--;//0 indexing
        for(i = 0;i<4;i++)
        {
            numbers[mat[choice1][i]] = 1;
        }
        cin>>choice2;
        for(i = 0;i<4;i++)
        {
            for(j = 0 ;j<4;j++)
            {
                cin>>mat[i][j];
            }
        }
        choice2--;//0 indexing
        for(i = 0;i<4;i++)
        {
            if(numbers[mat[choice2][i]]==1)
            {
                answer = mat[choice2][i];
                count++;
            }
        }
        switch(count)
        {
        case 1:
            cout<<"Case #"<<c<<": "<<answer<<endl;
            c = c + 1;
            break;
        case 0:
            cout<<"Case #"<<c<<": Volunteer cheated!"<<endl;
            c = c + 1;
            break;
        default:
            cout<<"Case #"<<c<<": Bad magician!"<<endl;
            c = c + 1;
            break;
        }
    }
}
