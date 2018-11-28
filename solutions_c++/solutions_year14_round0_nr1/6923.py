#include<iostream>
#include<map>
using namespace std;

int init[4][4],fin[4][4],row[4];

int findrow(int x)
{
    int i,j;
    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
            if(fin[i][j]==x)
                return i;
}

bool find(int x, int row)
{
    int i;
    for(i=0;i<4;i++)
        if(fin[row][i]==x)
            return true;
    return false;
}

int main()
{
    int i,j,b,a,t,w,x,y,z,c=0;
    //map<int,int>m;
    cin>>t;
    while((++c)<=t)
    {
        cin>>a;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin>>init[i][j];

        for(i=0;i<4;i++)
            row[i]=init[a-1][i];

        cin>>b;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin>>fin[i][j];

        w=findrow(row[0]);
        //m[w]++;
        x=findrow(row[1]);
        //m[x]++;
        y=findrow(row[2]);
        //m[y]++;
        z=findrow(row[3]);
        //m[z]++;

        bool flag =false;
        for(i=0;i<4;i++)
            flag=flag || find(row[i],b-1);

        if(!flag)
        {
            cout<<"Case #"<<c<<": Volunteer cheated!"<<endl;
            continue;
        }
        if(w==x || w==y || w==z || x==y || x==z || y==z)
        {
            int count=0;
            if(b-1==w)
                count++;
            if(b-1==x)
                count++;
            if(b-1==y)
                count++;
            if(b-1==z)
                count++;
            if(count>1)
            {
                cout<<"Case #"<<c<<": Bad magician!"<<endl;
                continue;
            }
        }
        for(i=0;i<4;i++)
            if(find(row[i],b-1))
            {
                cout<<"Case #"<<c<<": "<<row[i]<<endl;
                break;
            }
    }
    return 0;
}
