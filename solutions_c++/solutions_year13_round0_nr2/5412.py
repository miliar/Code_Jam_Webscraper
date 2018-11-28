#include <iostream>
#include <fstream>

using namespace std;

#define MAX 10

int N, M;
unsigned char arr[MAX+1][MAX+1];

int judge(int i, int j);
int main()
{
    ifstream in("B-small-attempt4.in");


    if(!in)
    {
        cout<<"can't open in file."<<endl;
    }
    ofstream out("B-small-attempt4.out");
    if(!out)
    {
        cout<<"can't open out file."<<endl;
    }

    int T;

    int i, j, count=1;

    in>>T;
    for(count=1; count<=T; count++)
    {
        in>>N>>M;

        int flag;
        for(i=1; i<=N; i++)
        {
            for(j=1; j<=M; j++)
            {
                in>>arr[i][j];
            }
        }

        if(N==1||M==1)
        {
            out<<"Case #"<<count<<": YES"<<endl;
            continue;
        }
        for(i=1; i<=N; i++)
        {
            for(j=1; j<=M; j++)
            {
                flag=judge(i, j);
                cout<<flag<<endl;
                if(flag==0)
                    break;
            }
            if(flag==0)
                break;
        }
        if(flag==0)
        {
            out<<"Case #"<<count<<": NO"<<endl;
            continue;
        }
        else
        {
            out<<"Case #"<<count<<": YES"<<endl;
            continue;
        }
    }

    return 0;
}

int judge(int i, int j)
{
    int ci=i, cj=j;
    while(ci>0&&(arr[ci][cj]<=arr[i][j])){ci--;};
    if(ci==0)
    {
        ci=i;
        cj=j;
        while(ci<=N&&(arr[ci][cj]<=arr[i][j])){ci++;};
        if(ci>N)
            return 1;
    }

//ÏÂÃæ¿´×óÓÒ
    ci=i;
    cj=j;
    while(cj>0&&(arr[ci][cj]<=arr[i][j])){cj--;};
    if(cj==0)
    {
        while(cj<=M&&(arr[ci][cj]<=arr[i][j])){cj++;};
        if(cj>M)
            return 1;
    }

    return 0;
}
