#include <iostream>
using namespace std;
#include <cstdlib>
#include <cstring>
#include <fstream>
int print(int t)
{
    ofstream fout;
    fout.open("tttt.txt",ios::out|ios::app);
    int** ary=new int*[4];
    int i=0;
    for(i=0;i<4;i++)
    {
        ary[i]=new int[4];
    }
    for(i=0;i<4;i++)
    {
        string str;
        string substr;
        int j=0;
        cin>>str;
        for(j=0;j<4;j++)
        {
            substr=str.substr(j,1);
            if(substr=="X")
            {
                ary[i][j]=1;
            }
            else if(substr=="O")
            {
                ary[i][j]=2;
            }
            else if(substr=="T")
            {
                ary[i][j]=3;
            }
            else
            {
                ary[i][j]=4;
            }
        }
    }
    /*
    for(i=0;i<4;i++)
    {
        int j=0;
        for(j=0;j<4;j++)
        {
            cout<<ary[i][j];
        }
        cout<<endl;
    }*/
    /*Check if any column is X-dominant or T-dominant*/
    int* x_rows=new int[4];
    int* o_rows=new int[4];
    int* x_columns=new int[4];
    int* o_columns=new int[4];
    int* t_rows=new int[4];
    int* t_columns=new int[4];
    int* dot_rows=new int[4];
    int* dot_columns=new int[4];
    for(i=0;i<4;i++)
    {
            x_rows[i]=0;
            o_rows[i]=0;
            x_columns[i]=0;
            o_columns[i]=0;
            t_rows[i]=0;
            t_columns[i]=0;
            dot_rows[i]=0;
            dot_columns[i]=0;
    }
    int x_ld=0;
    int o_ld=0;
    int t_ld=0;
    int dot_ld=0;            
    int x_rd=0;
    int o_rd=0;
    int t_rd=0;
    int dot_rd=0;
    for(i=0;i<4;i++)
    {
        int j=0;
        for(j=0;j<4;j++)
        {
            if(ary[i][j]==1)
            {
                x_columns[j]++;
                x_rows[i]++;
                if(i==j)
                {
                    x_ld++;
                }
                if(i+j==3)
                {
                    x_rd++;
                }
            }
            if(ary[i][j]==2)
            {
                o_columns[j]++;
                o_rows[i]++;
                if(i==j)
                {
                    o_ld++;
                }
                if(i+j==3)
                {
                    o_rd++;
                }
            }
            if(ary[i][j]==3)
            {
                t_columns[j]++;
                t_rows[i]++;
                if(i==j)
                {
                    t_ld++;
                }
                if(i+j==3)
                {
                    t_rd++;
                }
            }
            if(ary[i][j]==4)
            {
                dot_columns[j]++;
                dot_rows[i]++;
                if(i==j)
                {
                    dot_ld++;
                }
                if(i+j==3)
                {
                   dot_rd++;
                }
            }
        }
    }
    /*Now check for the victory condition*/
    int x_victory=0;
    int o_victory=0;
    for(i=0;i<4;i++)
    {
        if((x_rows[i]==4)||((x_rows[i]==3)&&(t_rows[i]==1)))
        {
            x_victory=1;
            break;
        }
         if((x_columns[i]==4)||((x_columns[i]==3)&&(t_columns[i]==1)))
        {
            x_victory=1;
            break;
        }
         if((o_rows[i]==4)||((o_rows[i]==3)&&(o_rows[i]==1)))
        {
            o_victory=1;
            break;
        }
         if((o_columns[i]==4)||((o_columns[i]==3)&&(o_columns[i]==1)))
        {
            o_victory=1;
            break;
        }
    }
    if(x_victory==1)
    {
        fout<<"Case #"<<t<<":X won"<<endl;
        return 0;
    }
    else if(o_victory==1)
    {
        fout<<"Case #"<<t<<":O won"<<endl;
        return 0;
    }
    if((o_ld==4)||((o_ld==3)&&(t_ld==1)))
    {
            o_victory=1;
    }
    if((o_rd==4)||((o_rd==3)&&(t_rd==1)))
    {
        o_victory=1;
    }
    if((x_ld==4)||((x_ld==3)&&(t_ld==1)))
    {
        x_victory=1;
    }
    if((x_rd==4)||((x_rd==3)&&(t_rd==1)))
    {
            x_victory=1;
    }
    if(x_victory==1)
    {
        fout<<"Case #"<<t<<":X won"<<endl;
        return 0;
    }
    else if(o_victory==1)
    {
        fout<<"Case #"<<t<<":O won"<<endl;
        return 0;
    }
    int nodots=1;
    for(i=0;i<4;i++)
    {
        if(dot_rows[i]>0)
        {
            nodots=0;
            break;
        }
    }
    if(nodots==0)
    {
        fout<<"Case #"<<t<<":Game has not completed"<<endl;
        return 0;
    }
    else
    {
        fout<<"Case #"<<t<<":Draw"<<endl;
        return 0;
    }
    return 0;
}
int main()
{
    int t;
    cin>>t;
    //ofstream fout;
    //fout.open("tttt.txt");
    int i=1;
    for(i=1;i<=t;i++)
    {
        print(i);
    }
    return 0;
}
