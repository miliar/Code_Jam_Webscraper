#include <iostream>

using namespace std;


int control(int* f,int* s)
{
    int last[4],i,j,x,a;
    for(i=0;i<4;i++)
    {
        last[i]=-1;
    }
    x=0;
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(f[i]==s[j])
            {
                last[x]=f[i];
                x++;
                break;
            }
        }
    }
    if(last[1]!=-1)
    {
        return -1;
    }
    else if(last[0]==-1)
    {
        return -2;
    }
    else
    {
        return last[0];
    }
}

int main()
{
    int test, lines[6][4], f, s,i,j,x,a;
    cin>>test;
    i=0;
    
    while(0<test)
    {
		test--;
        cin>>f;
        for(j=0;j<4;j++)
        {
            for(a=0;a<4;a++)
            {
                cin>>lines[j][a];
            }
        }
        for(j=0;j<4;j++)
        {
           lines[5][j]=lines[f-1][j];
        }
        cin>>s;
        for(j=0;j<4;j++)
        {
            for(a=0;a<4;a++)
            {
                cin>>lines[j][a];
            }
        }

        for(j=0;j<4;j++)
        {
           lines[6][j]=lines[s-1][j];
        }
        x=control(lines[5],lines[6]);
        i++;
        cout<<"Case #"<<i<<": " ;
        if(x==-1)
        {
            cout<<"Bad magician!"<<endl;
        }
        else if(x==-2)
        {
            cout<<"Volunteer cheated!"<<endl;
        }
        else
        {
            cout<<x<<endl;
        }
    }
    return 0;
}
