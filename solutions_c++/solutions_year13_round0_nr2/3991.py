#include <iostream>
using namespace std;

int maxRow(int** data, int i, int total);
int maxColumn(int** data, int i, int total);
int min(int a, int b); 

int main()
{
    int numTest;
    cin>>numTest;

    for(int k=0;k<numTest;++k)
    {
        cout<<"Case #"<<k+1<<": ";

        int N,M;
        cin>>N>>M;
    
        bool result=true;
    
        int** data;
        data = new int*[N];
        for(int i=0;i<N;++i)
        {
            data[i]=new int[M];
        }

        for(int i=0;i<N;++i)
        {
            for(int j=0;j<M;++j)
            {
                cin>>data[i][j];
            }
        }

        int row[N];
        for(int i=0;i<N;++i)
        {
            row[i]=maxRow(data,i,M);
        }

        int column[M];
        for(int i=0;i<M;++i)
        {
            column[i]=maxColumn(data,i,N);
        }

        for(int i=0;i<N;++i)
        {
            for(int j=0;j<M;++j)
            {
                if(data[i][j]!=min(row[i],column[j]))
                {
                    result=false;
                     break;
                }
            }   
        }

        if (result == true)
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
    }
    return 0;
}

int maxRow(int** data,int i,int total)
{
    int result = -1;
    for(int temp=0;temp<total;++temp)
    {
        if(data[i][temp]>result)
            result=data[i][temp];
    }

    return result;
}

int maxColumn(int** data, int i, int total)
{
    int result = -1;
    for(int temp=0;temp<total;++temp)
    {
        if(data[temp][i]>result)
            result=data[temp][i];
    }
    return result;
}
 int min(int a, int b)
{
    if(a<b)
        return a;
    else
        return b;
}

