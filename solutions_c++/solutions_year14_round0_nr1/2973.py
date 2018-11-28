#include<stdio.h>
#include<iostream>
using namespace std;
int ans1,ans2;
int a1[4][4],a2[4][4], r[4];
void input(int inp[4][4])
{
    int i,j=0;
    for (i=0;i<4;i++)
    {
        for (j=0;j<4;j++)
        {
            cin>>inp[i][j];
        }
    }
}
/*void output(int inp[4][4])
{
    int i,j=0;
    for (i=0;i<4;i++)
    {
        for (j=0;j<4;j++)
        {
            cout<<inp[i][j];
            cout<<" ";
        }
        cout<<endl;
    }
}*/
void compare(int a1[4][4],int a2[4][4], int ans1,int ans2,int case_no)
{
    int i,j,k =0;
    for(i=0;i<4;i++)
    {
        for (j=0;j<4;j++)
        {
            if(a1[ans1-1][i]==a2[ans2-1][j])
            {
                r[k]= a1[ans1-1][i];
                k++;
                //cout<<"\n"<<case_no<<" "<< k<<" "<<r[k-1]<<endl;

            }
        }
    }
    if (k==0)
    {
        cout<<"Case #"<<case_no<<": Volunteer cheated!\n";
    }
    if (k>1)
    {
        cout<<"Case #"<<case_no<<": Bad magician!\n";
    }
    if (k==1)
    {
        cout<<"Case #"<<case_no<<": "<<r[0]<<endl;
    }


}
int main()
{
    int test;
    freopen("a.txt","r",stdin);
    freopen("aout.txt","w",stdout);
    cin>>test;
    int case_no=0;
    while (case_no<test)
    {
        case_no++;

        cin>>ans1;
        input(a1);

        cin>>ans2;
        input(a2);
        compare(a1,a2,ans1,ans2,case_no);

        //cout<<"output\n";
        //output(a1);
        //output(a2);
    }


}
