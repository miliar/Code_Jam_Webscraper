#include<iostream>
using namespace std;

int main()
{
    int T,ch1,ch2,m[4][4],r1[4],r2[4];
    int y;
    int i,j,k,p,q,testcase[100],num[100];
    cin>>T;
    for(y=0;y<T;y++)
    {
        cin>>ch1;
        ch1--;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            cin>>m[i][j];

        for(p=0;p<4;p++)
            r1[p]=m[ch1][p];


        cin>>ch2;
        ch2--;

        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            cin>>m[i][j];

        for(p=0;p<4;p++)
            r2[p]=m[ch2][p];


        for(i=0,testcase[y]=0,p=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(r1[i]==r2[j])
                {
                    q=r1[i];
                    num[y]=q;
                    p++;
                    testcase[y]=p;
					break;
                }

            }
        }




    }
    for(y=0;y<T;y++)
    {
        cout<<"Case #"<<y+1<<": ";

        if(testcase[y]==0)
            cout<<"Volunteer cheated!";

        else if(testcase[y]==1)
             cout<<num[y];

        else if(testcase[y]>1)
             cout<<"Bad magician!";

        if(y+1<T)
            cout<<"\n";
    }
	return 0;
}
