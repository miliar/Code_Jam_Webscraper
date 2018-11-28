#include<iostream>
#include<cstdio>

using namespace std;

int solve(int buf_1[],int buf_2[])
{
    int no,count=0;
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            if(buf_1[i]==buf_2[j])
            {
                count++;
                no=buf_1[i];
            }
    if(count==0)
        return 0;
    else if(count>1)
        return -1;
    else
        return no;
}
int main()
{
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	int i,j;
	int t,ans,deck[4][4];
	int buf_1[4],buf_2[4];
	int c=1;
	cin>>t;
	while(t--)
    {
        cin>>ans;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin>>deck[i][j];
        for(i=0;i<4;i++)
            buf_1[i]=deck[ans-1][i];

        cin>>ans;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin>>deck[i][j];
        for(i=0;i<4;i++)
            buf_2[i]=deck[ans-1][i];

        int f=solve(buf_1,buf_2);
        cout<<"Case #"<<c<<": ";
        if(f==-1)
            cout<<"Bad magician!";
        else if(f==0)
            cout<<"Volunteer cheated!";
        else
            cout<<f;
        cout<<"\n";
        c++;
    }
	return 0;
}
